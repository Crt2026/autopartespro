from django.contrib.auth.backends import ModelBackend
from django.utils import timezone
from django.core.exceptions import ValidationError

class SecurityValuesBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        
        if user:
            # Si el usuario se autenticó correctamente, verificar si está bloqueado
            if user.bloqueado_hasta and user.bloqueado_hasta > timezone.now():
                # Opcional: Podríamos lanzar una excepción o simplemente retornar None
                # Si retornamos None, Django lo tratará como falla de autenticación
                return None
            return user
        return None
