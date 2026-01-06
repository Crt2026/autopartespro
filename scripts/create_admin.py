import os
import sys
import django

# Add project root to path so autopartespro module is found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autopartespro.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_admin():
    User = get_user_model()
    username = 'admin'
    email = 'admin@autopartespro.cl'
    password = 'admin'
    
    if not User.objects.filter(username=username).exists():
        print(f"Creando superusuario '{username}'...")
        User.objects.create_superuser(username, email, password)
        print(f"Superusuario creado exitosamente.\nUsuario: {username}\nContraseña: {password}")
    else:
        print(f"El usuario '{username}' ya existe.")

if __name__ == '__main__':
    create_admin()
