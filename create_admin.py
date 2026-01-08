import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autopartespro.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = "admin"
PASSWORD = "admin123"
EMAIL = "admin@admin.com"

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(
        username=USERNAME,
        password=PASSWORD,
        email=EMAIL
    )
    print("✅ Superusuario creado")
else:
    print("⚠️ El superusuario ya existe")
