import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autopartespro.settings")
django.setup()

print("--- DATABASE SETTINGS ---")
db = settings.DATABASES['default']
print(f"ENGINE: {db['ENGINE']}")
print(f"NAME: {db['NAME']}")
print(f"HOST: {db['HOST']}")
print(f"PORT: {db['PORT']}")
print(f"USER: {db['USER']}")

print("\n--- DATA CHECK ---")
try:
    from productos.models import Producto
    count = Producto.objects.count()
    print(f"Productos found: {count}")
    if count > 0:
        print(f"Example: {Producto.objects.first()}")
except Exception as e:
    print(f"Error querying products: {e}")

try:
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE()")
        print(f"\nConnected to DB: {cursor.fetchone()}")
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(f"Total tables: {len(tables)}")
except Exception as e:
    print(f"Error connecting to DB: {e}")
