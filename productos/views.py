from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from productos.models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer
import mercadopago

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['categoria', 'marca', 'destacado']
    search_fields = ['nombre', 'descripcion', 'SKU', 'modelo_compatible']
    ordering_fields = ['precio', 'nombre', 'created_at']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def destacados(self, request):
        productos = self.get_queryset().filter(destacado=True)
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MercadoPagoViewSet(viewsets.ViewSet):
    def create(self, request):
        sdk = mercadopago.SDK("APP_USR-e72d1962-1a6f-4a72-aa69-479b0c87a62f")
        
        preference_data = request.data
        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        
        return Response({"id": preference["id"]})