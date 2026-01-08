from django.contrib.auth import get_user_model
User = get_user_model()

if User.objects.filter(username="admin").exists():
    admin = User.objects.get(username="admin")
    admin.set_password("admin123")
    admin.is_staff = True
    admin.is_superuser = True
    admin.save()
    print("🔁 Admin actualizado")
else:
    User.objects.create_superuser("admin", "admin@email.com", "admin123")
    print("✅ Admin creado")
