from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.db.models import Q, Count, Sum
from productos.models import Producto, Categoria, Marca
from pedidos.models import Carrito, ItemCarrito, Orden, DetalleOrden
from usuarios.models import Usuario, DireccionEnvio
from .serializers import (
    ProductoSerializer, CategoriaSerializer, MarcaSerializer,
    CarritoSerializer, ItemCarritoSerializer, OrdenSerializer,
    DireccionEnvioSerializer, UsuarioSerializer
)
import mercadopago
from django.conf import settings
from decimal import Decimal

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.filter(activo=True).select_related('categoria', 'marca')
    serializer_class = ProductoSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['categoria', 'marca', 'destacado', 'nuevo']
    search_fields = ['nombre', 'descripcion', 'SKU', 'modelo_compatible', 'año_compatible']
    ordering_fields = ['precio', 'nombre', 'created_at', 'destacado']
    ordering = ['-destacado', '-created_at']
    
    @action(detail=False, methods=['get'])
    def destacados(self, request):
        productos = self.get_queryset().filter(destacado=True)[:12]
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def nuevos(self, request):
        productos = self.get_queryset().filter(nuevo=True)[:12]
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def buscar(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response([])
        
        productos = self.get_queryset().filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(SKU__icontains=query) |
            Q(modelo_compatible__icontains=query)
        )[:20]
        
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def relacionados(self, request):
        producto_id = request.query_params.get('producto_id')
        if not producto_id:
            return Response([])
        
        try:
            producto = Producto.objects.get(id=producto_id)
            relacionados = self.get_queryset().filter(
                Q(categoria=producto.categoria) |
                Q(marca=producto.marca)
            ).exclude(id=producto.id).distinct()[:8]
            
            serializer = self.get_serializer(relacionados, many=True)
            return Response(serializer.data)
        except Producto.DoesNotExist:
            return Response([])

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.filter(activo=True)
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
    @action(detail=True, methods=['get'])
    def productos(self, request, slug=None):
        categoria = self.get_object()
        productos = categoria.productos.filter(activo=True)
        
        # Aplicar filtros si existen
        marca = request.query_params.get('marca')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        
        if marca:
            productos = productos.filter(marca__nombre__iexact=marca)
        if min_price:
            productos = productos.filter(precio__gte=min_price)
        if max_price:
            productos = productos.filter(precio__lte=max_price)
        
        page = self.paginate_queryset(productos)
        if page is not None:
            serializer = ProductoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class CarritoViewSet(viewsets.ModelViewSet):
    serializer_class = CarritoSerializer
    
    # Allow anonymous users access (could use session key if needed, or enforce login for now as per prompt model which relies on User ForeignKey)
    # The models define ForeignKey to AUTH_USER_MODEL which implies authenticated user, 
    # OR we need to modify models to allow null user. The prompt models show `usuario = models.ForeignKey(..., on_delete=models.CASCADE)` which IS required.
    # So we require authentication.
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Carrito.objects.filter(usuario=self.request.user, activo=True)
    
    @action(detail=False, methods=['get'])
    def mi_carrito(self, request):
        carrito, created = Carrito.objects.get_or_create(
            usuario=request.user,
            activo=True,
            defaults={'session_key': request.session.session_key}
        )
        serializer = self.get_serializer(carrito)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def agregar_producto(self, request):
        carrito, created = Carrito.objects.get_or_create(
            usuario=request.user,
            activo=True
        )
        
        producto_id = request.data.get('producto_id')
        cantidad = int(request.data.get('cantidad', 1))
        
        try:
            producto = Producto.objects.get(id=producto_id, activo=True)
            
            if producto.stock < cantidad:
                return Response(
                    {'error': f'Stock insuficiente. Disponible: {producto.stock}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            item, item_created = ItemCarrito.objects.get_or_create(
                carrito=carrito,
                producto=producto,
                defaults={'cantidad': cantidad, 'precio_unitario': producto.precio_final}
            )
            
            if not item_created:
                item.cantidad += cantidad
                item.save()
            
            serializer = self.get_serializer(carrito)
            return Response(serializer.data)
            
        except Producto.DoesNotExist:
            return Response(
                {'error': 'Producto no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['post'])
    def actualizar_cantidad(self, request):
        item_id = request.data.get('item_id')
        cantidad = int(request.data.get('cantidad', 1))
        
        try:
            item = ItemCarrito.objects.get(
                id=item_id,
                carrito__usuario=request.user,
                carrito__activo=True
            )
            
            if cantidad < 1:
                item.delete()
            else:
                if item.producto.stock < cantidad:
                    return Response(
                        {'error': f'Stock insuficiente. Disponible: {item.producto.stock}'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                item.cantidad = cantidad
                item.save()
            
            carrito = item.carrito
            serializer = self.get_serializer(carrito)
            return Response(serializer.data)
            
        except ItemCarrito.DoesNotExist:
            return Response(
                {'error': 'Ítem no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['post'])
    def eliminar_producto(self, request):
        item_id = request.data.get('item_id')
        
        try:
            item = ItemCarrito.objects.get(
                id=item_id,
                carrito__usuario=request.user,
                carrito__activo=True
            )
            item.delete()
            
            carrito = item.carrito
            serializer = self.get_serializer(carrito)
            return Response(serializer.data)
            
        except ItemCarrito.DoesNotExist:
            return Response(
                {'error': 'Ítem no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['post'])
    def vaciar(self, request):
        carrito = Carrito.objects.filter(usuario=request.user, activo=True).first()
        if carrito:
            carrito.items.all().delete()
        
        serializer = self.get_serializer(carrito)
        return Response(serializer.data)

class OrdenViewSet(viewsets.ModelViewSet):
    serializer_class = OrdenSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['estado', 'metodo_pago', 'metodo_envio']
    ordering_fields = ['fecha_creacion', 'total']
    ordering = ['-fecha_creacion']
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Orden.objects.filter(usuario=self.request.user)
        # For guests, arguably we shouldn't return a list, or only return by order ID if secured (e.g. via token). 
        # For now, return empty for anonymous to prevent leaking others' orders.
        return Orden.objects.none()
    
    def create(self, request):
        datos = request.data
        items_data = datos.get('items', [])
        
        if not items_data:
             # Try fallback to user's cart if no items provided directly and user is logged in
            if request.user.is_authenticated:
                carrito = Carrito.objects.filter(usuario=request.user, activo=True).first()
                if carrito and carrito.items.count() > 0:
                     # Adapt cart items to the logic below
                     pass # (omitted for brevity, sticking to direct payload preference)
            
            if not items_data:
                return Response(
                    {'error': 'No se proporcionaron productos para la orden'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Validate stock and filter available items
        valid_items_data = []
        for item in items_data:
            try:
                prod_id = item.get('id')
                cantidad = int(item.get('cantidad', 1))
                producto = Producto.objects.get(id=prod_id)
                if producto.stock < cantidad:
                    return Response(
                        {'error': f'Stock insuficiente para {producto.nombre} (Disponible: {producto.stock})'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                valid_items_data.append(item)
            except Producto.DoesNotExist:
                # Skip items that don't exist
                continue

        if not valid_items_data:
             return Response(
                {'error': 'No hay productos válidos para procesar la orden'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create Order
        try:
            # Calculate totals for valid items
            subtotal = sum( 
                Decimal(str(item.get('precio'))) * int(item.get('cantidad', 1)) 
                for item in valid_items_data 
            )
            costo_envio = Decimal(str(datos.get('costo_envio', 0)))
            descuento = Decimal(str(datos.get('descuento', 0)))
            total = subtotal + costo_envio - descuento # Model handles IVA calculation if needed, or we explicitly set it.
            
            orden = Orden.objects.create(
                usuario=request.user if request.user.is_authenticated else None,
                cliente_nombre=datos.get('cliente_nombre', ''),
                cliente_apellido=datos.get('cliente_apellido', ''),
                cliente_email=datos.get('cliente_email', ''),
                cliente_telefono=datos.get('cliente_telefono', ''),
                cliente_rut=datos.get('cliente_rut', ''),
                
                direccion_calle=datos.get('direccion_calle', ''),
                direccion_numero=datos.get('direccion_numero', ''),
                direccion_dpto=datos.get('direccion_dpto', ''),
                direccion_comuna=datos.get('direccion_comuna', ''),
                direccion_region=datos.get('direccion_region', ''),
                direccion_codigo_postal=datos.get('direccion_codigo_postal', ''),
                direccion_indicaciones=datos.get('direccion_indicaciones', ''),
                
                metodo_pago=datos.get('metodo_pago', 'mercadopago'),
                metodo_envio=datos.get('metodo_envio', 'domicilio'),
                
                subtotal=subtotal,
                costo_envio=costo_envio,
                descuento=descuento,
                total=total,
                
                notas=datos.get('notas', '')
            )
            
            # Create Order Details
            for item in valid_items_data:
                prod = Producto.objects.get(id=item.get('id'))
                DetalleOrden.objects.create(
                    orden=orden,
                    producto=prod,
                    cantidad=int(item.get('cantidad', 1)),
                    precio_unitario=Decimal(str(item.get('precio'))),
                    # Subtotal calculated by model's save method or explicitly:
                    subtotal=Decimal(str(item.get('precio'))) * int(item.get('cantidad', 1))
                )

            # If came from a registered user's active cart, disable it? 
            # (Requires logic to link database cart with this payload, maybe for later)

            serializer = self.get_serializer(orden)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['post'])
    def pagar_mercadopago(self, request, pk=None):
        orden = get_object_or_404(Orden, pk=pk)
        
        # ... (Mercado Pago logic using properties from 'orden' object)
        # Same logic as before, but mapped to the persisted object
        
        sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)
        
        # Force localhost for local development to satisfy MP validation
        # base_url = "http://127.0.0.1:8000"
        # base_url = "https://www.google.com/search?q=autopartespro"
        base_url = settings.SITE_URL
        
        # Validate Payer Email to prevent Self-Payment Error (PA_UNAUTHORIZED_RESULT_FROM_POLICIES)
        payer_email = orden.cliente_email
        # Optional: You can hardcode your seller email here to check, or just rely on the user using a different one.
        # But to be safe, if we are in DEBUG, maybe force a test email if it looks suspicious?
        # For now, let's just make sure the data is clean.
        
        preference_data = {
            "items": [
                {
                    "id": str(orden.id),
                    "title": f"Orden #{orden.numero_orden}",
                    "description": f"Compra en AutoPartes Pro",
                    "quantity": 1,
                    "currency_id": "CLP",
                    "unit_price": float(orden.total)
                }
            ],
            "payer": {
                "name": orden.cliente_nombre,
                "surname": orden.cliente_apellido,
                "email": payer_email,
                "phone": {
                    "area_code": "",
                    "number": orden.cliente_telefono
                },
                "address": {
                    "street_name": orden.direccion_calle,
                    "street_number": int(orden.direccion_numero) if orden.direccion_numero.isdigit() else 123,
                    "zip_code": orden.direccion_codigo_postal
                }
            },
            "back_urls": {
                "success": f"{base_url}/pago/exitoso/?orden={orden.id}",
                "failure": f"{base_url}/pago/fallido/",
                "pending": f"{base_url}/pago/pendiente/"
            },
            "auto_return": "approved",
            "binary_mode": True, # Try False if this persists, but usually True is fine for instant payments
            "payment_methods": {
                "excluded_payment_methods": [],
                "excluded_payment_types": [
                    {"id": "ticket"}, # Exclude offline payments like Pagofacil if you want instant approval
                    {"id": "atm"}
                ],
                "installments": 12
            },
            "external_reference": str(orden.id),
            "statement_descriptor": "AUTOPARTESPRO"
        }
        
        try:
            print(f"Creating Preference with data: {preference_data}")
            preference_response = sdk.preference().create(preference_data)
            print(f"MP Response: {preference_response}")
            
            if preference_response.get("status") not in [200, 201]:
                 error_detail = preference_response.get("response", {})
                 # Log full error to console for PythonAnywhere logs
                 print(f"ERROR MERCADO PAGO: {error_detail}") 
                 return Response(
                    {'error': 'Error Mercado Pago', 'details': error_detail},
                    status=status.HTTP_400_BAD_REQUEST
                )

            preference = preference_response["response"]
            if "id" not in preference:
                 return Response(
                    {'error': 'No Preference ID', 'details': preference},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            orden.referencia_pago = preference["id"]
            orden.save()
            
            return Response({
                "preference_id": preference["id"],
                "init_point": preference["init_point"], 
                "sandbox_init_point": preference["sandbox_init_point"],
                "orden_id": orden.id
            })
            
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class MercadoPagoWebhookView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        try:
            data = request.data
            
            if data.get('type') == 'payment':
                payment_id = data.get('data', {}).get('id')
                
                sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)
                payment_info = sdk.payment().get(payment_id)
                
                if payment_info['status'] == 200:
                    payment = payment_info['response']
                    orden_id = payment.get('external_reference')
                    
                    try:
                        orden = Orden.objects.get(id=orden_id)
                        
                        if payment['status'] == 'approved':
                            orden.estado = 'pagada'
                            orden.fecha_pago = payment['date_approved']
                            orden.referencia_pago = payment_id
                            
                            # Reducir stock de productos
                            for detalle in orden.detalles.all():
                                detalle.producto.reducir_stock(detalle.cantidad)
                            
                            # Enviar notificaciones
                            self.enviar_notificaciones(orden)
                            
                        elif payment['status'] == 'rejected':
                            orden.estado = 'rechazada'
                        
                        orden.save()
                        
                        return Response({'status': 'ok'})
                        
                    except Orden.DoesNotExist:
                        return Response({'error': 'Orden no encontrada'}, status=404)
            
            return Response({'status': 'ignored'})
            
        except Exception as e:
            print(f"Error en webhook MercadoPago: {e}")
            return Response({'error': str(e)}, status=500)
    
    def enviar_notificaciones(self, orden):
        # Aquí puedes implementar envío de emails, WhatsApp, etc.
        pass

class CreatePreferenceView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        try:
            sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)
            data = request.data
            
            preference_data = {
                "items": data.get('items', []),
                "payer": data.get('payer', {}),
                "back_urls": data.get('back_urls', {}),
                "auto_return": "approved",
                "binary_mode": True,
            }
            
            preference_response = sdk.preference().create(preference_data)
            preference = preference_response["response"]
            
            return Response({'id': preference['id']})
            
        except Exception as e:
            return Response({'error': str(e)}, status=500)
