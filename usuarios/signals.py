from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta

@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    from .models import Usuario
    username = credentials.get('username')
    try:
        user = Usuario.objects.get(username=username)
        user.intentos_fallidos += 1
        
        if user.intentos_fallidos >= 3:
            user.bloqueado_hasta = timezone.now() + timedelta(minutes=15)
        
        user.save()
    except Usuario.DoesNotExist:
        # No revelar si el usuario existe o no
        pass

@receiver(user_logged_in)
def reset_failed_login(sender, request, user, **kwargs):
    user.intentos_fallidos = 0
    user.bloqueado_hasta = None
    user.save()
