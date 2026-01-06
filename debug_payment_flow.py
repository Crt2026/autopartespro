import os
import django
from decimal import Decimal
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autopartespro.settings')
django.setup()
from django.conf import settings
settings.ALLOWED_HOSTS += ['testserver']

from pedidos.models import Orden
from productos.models import Producto
from rest_framework.test import APIRequestFactory
from api.views import OrdenViewSet

print("--- Starting Payment Flow Debug ---")

# 1. Create Order
product = Producto.objects.first()
if not product:
    print("No products found.")
    exit(1)

factory = APIRequestFactory()
data = {
    'items': [{'id': product.id, 'cantidad': 1, 'precio': float(product.precio)}],
    'cliente_nombre': 'Debug User',
    'cliente_apellido': 'Debug Lastname',
    'cliente_email': 'debug@test.com',
    'cliente_telefono': '+56912345678',
    'direccion_calle': 'Debug St',
    'direccion_numero': '123',
    'direccion_comuna': 'Santiago',
    'direccion_region': 'RM',
    'metodo_pago': 'mercadopago',
    'metodo_envio': 'domicilio'
}

print("Attempting to create order...")
view_create = OrdenViewSet.as_view({'post': 'create'})
request_create = factory.post('/api/ordenes/', data, format='json')
response_create = view_create(request_create)

if response_create.status_code != 201:
    print(f"FAILED to create order. Status: {response_create.status_code}")
    print(response_create.data)
    exit(1)

orden_id = response_create.data['id']
print(f"Order created successfully. ID: {orden_id}")

# 2. Initiate Payment (pagar_mercadopago)
print(f"Attempting to initiate payment for Order {orden_id}...")
view_pay = OrdenViewSet.as_view({'post': 'pagar_mercadopago'})
request_pay = factory.post(f'/api/ordenes/{orden_id}/pagar_mercadopago/')
# We need to force logic to see this as a detail route for the specific object
# In a real request, DRF router handles grabbing the object based on PK in URL.
# Here, we must manually ensure 'pk' is passed to the view method or viewset.

# Correct way to test ViewSet detail action with APIRequestFactory:
view_pay = OrdenViewSet.as_view({'post': 'pagar_mercadopago'})
response_pay = view_pay(request_pay, pk=orden_id)

print(f"Payment Endpoint Status: {response_pay.status_code}")
if response_pay.status_code == 200:
    print("SUCCESS: Payment preference created.")
    print("Preference ID:", response_pay.data.get('preference_id'))
    print("Init Point:", response_pay.data.get('init_point'))
else:
    print("FAILED to initiate payment.")
    print("Error Data:", response_pay.data)
