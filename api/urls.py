from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductoViewSet, CategoriaViewSet, CarritoViewSet,
    OrdenViewSet, MercadoPagoWebhookView, CreatePreferenceView
)

router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'carrito', CarritoViewSet, basename='carrito')
router.register(r'ordenes', OrdenViewSet, basename='orden')

urlpatterns = [
    path('', include(router.urls)),
    path('webhook/mercadopago/', MercadoPagoWebhookView.as_view(), name='mercadopago-webhook'),
    path('create-preference', CreatePreferenceView.as_view(), name='create-preference'),
]
