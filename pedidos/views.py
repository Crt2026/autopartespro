from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import mercadopago
from .models import Orden, DetalleOrden
from productos.models import Producto
from django.conf import settings

@method_decorator(csrf_exempt, name='dispatch')
class ProcesarPagoAPIView(APIView):
    def post(self, request):
        try:
            data = request.data # DRF parses JSON automatically
            
            # 1. Crear orden
            orden = Orden.objects.create(
                usuario=request.user if request.user.is_authenticated else None,
                total=data.get('total', 0),
                estado='pendiente',
                datos_cliente=data.get('cliente', {}),
                direccion_envio=data.get('direccion', {}),
                metodo_pago='mercadopago'
            )
            
            # 2. Crear items
            items = data.get('items', [])
            mp_items = []
            
            for item in items:
                try:
                    producto = Producto.objects.get(id=item['id'])
                    DetalleOrden.objects.create(
                        orden=orden,
                        producto=producto,
                        cantidad=item['cantidad'],
                        precio=item['precio']
                    )
                    mp_items.append({
                        "title": item['nombre'],
                        "quantity": int(item['cantidad']),
                        "currency_id": "CLP",
                        "unit_price": float(item['precio'])
                    })
                except Producto.DoesNotExist:
                    pass
            
            # 3. Create MP Preference
            sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)
            
            preference_data = {
                "items": mp_items,
                "payer": {
                    "name": data.get('cliente', {}).get('firstName', 'Test'),
                    "surname": data.get('cliente', {}).get('lastName', 'User'),
                    "email": data.get('cliente', {}).get('email', 'test@user.com'),
                },
                "back_urls": {
                    "success": f"{settings.SITE_URL}/pago/exitoso/?orden={orden.id}",
                    "failure": f"{settings.SITE_URL}/pago/fallido/",
                    "pending": f"{settings.SITE_URL}/pago/pendiente/"
                },
                "auto_return": "approved",
                "external_reference": str(orden.id)
            }
            
            preference_response = sdk.preference().create(preference_data)
            
            return Response({
                "preference_id": preference_response["response"]["id"],
                "orden_id": orden.id,
                "init_point": preference_response["response"]["init_point"] # Useful link
            })
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
