import os
import django
from django.conf import settings
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autopartespro.settings')
django.setup()
settings.ALLOWED_HOSTS += ['testserver']

from pedidos.models import Orden, DetalleOrden
from productos.models import Producto
from rest_framework.test import APIRequestFactory
from api.views import OrdenViewSet

# Ensure we have a product
product = Producto.objects.first()
if not product:
    print("No products found to test order creation.")
    exit(1)

factory = APIRequestFactory()
data = {
    'items': [
        {'id': product.id, 'cantidad': 1, 'precio': float(product.precio)}
    ],
    'cliente_nombre': 'Test Guest',
    'cliente_apellido': 'User',
    'cliente_email': 'guest@test.com',
    'cliente_telefono': '+56912345678',
    'direccion_calle': 'Test St',
    'direccion_numero': '123',
    'direccion_comuna': 'Santiago',
    'direccion_region': 'RM',
    'metodo_pago': 'transferencia',
    'metodo_envio': 'domicilio',
    'costo_envio': 0,
    'descuento': 0
}

view = OrdenViewSet.as_view({'post': 'create'})
request = factory.post('/api/ordenes/', data, format='json')
response = view(request)

print(f"Status Code: {response.status_code}")
if response.status_code == 201:
    print(f"Order created: ID {response.data['id']}, Number: {response.data['numero_orden']}")
    
    # Verify in DB
    orden = Orden.objects.get(id=response.data['id'])
    print(f"DB Verification: Orden {orden.numero_orden} exists. Usuario: {orden.usuario}")
    if orden.usuario is None:
         print("SUCCESS: Order created for guest (usuario is None).")
    else:
         print("WARNING: Usuario is not None.")
else:
    print("Error:", response.data)
