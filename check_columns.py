from django.db import connection
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autopartespro.settings')
django.setup()

with connection.cursor() as cursor:
    cursor.execute("DESCRIBE usuarios_usuario;")
    columns = [col[0] for col in cursor.fetchall()]
    print("Columns in usuarios_usuario:", columns)
    
    if 'intentos_fallidos' in columns:
        print("intentos_fallidos EXISTS")
    else:
        print("intentos_fallidos MISSING")
