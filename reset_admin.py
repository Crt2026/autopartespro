import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autopartespro.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin'
password = 'admin123'

try:
    user = User.objects.get(username=username)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.es_admin = True  # Custom field
    user.save()
    print(f"User '{username}' updated successfully. Password: '{password}', is_staff=True")
except User.DoesNotExist:
    User.objects.create_superuser(username, 'admin@example.com', password)
    print(f"User '{username}' created successfully. Password: '{password}'")
