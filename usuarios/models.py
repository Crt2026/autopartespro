from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    rut = models.CharField(max_length=12, blank=True, unique=True, null=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    comuna = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    
    # Roles
    es_cliente = models.BooleanField(default=True)
    es_vendedor = models.BooleanField(default=False)
    es_admin = models.BooleanField(default=False)
    
    # Marketing
    newsletter = models.BooleanField(default=False)
    terminos_aceptados = models.BooleanField(default=False)
    
    # Metadata
    codigo_cliente = models.CharField(max_length=50, blank=True, unique=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultimo_acceso = models.DateTimeField(auto_now=True)
    
    # Seguridad
    intentos_fallidos = models.IntegerField(default=0)
    bloqueado_hasta = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_staff or self.is_superuser:
            self.es_admin = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class DireccionEnvio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='direcciones')
    alias = models.CharField(max_length=50, help_text="Ej: Casa, Oficina")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    dpto = models.CharField(max_length=20, blank=True)
    comuna = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20, blank=True)
    indicaciones = models.TextField(blank=True)
    por_defecto = models.BooleanField(default=False)
    
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Dirección de Envío"
        verbose_name_plural = "Direcciones de Envío"
        
    def save(self, *args, **kwargs):
        if self.por_defecto:
            # Desmarcar otras direcciones por defecto del usuario
            DireccionEnvio.objects.filter(usuario=self.usuario, por_defecto=True).update(por_defecto=False)
        super().save(*args, **kwargs)
        
    def direccion_completa(self):
        return f"{self.calle} {self.numero}, {self.comuna}, {self.region}"
    
    def __str__(self):
        return f"{self.alias} - {self.usuario.username}"
