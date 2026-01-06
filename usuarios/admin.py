from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, DireccionEnvio

class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'first_name', 'last_name', 'rut', 'es_cliente', 'es_vendedor', 'is_staff']
    list_filter = ['es_cliente', 'es_vendedor', 'is_staff', 'is_active', 'bloqueado_hasta']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('rut', 'telefono', 'direccion', 'comuna', 'region', 'codigo_cliente')}),
        ('Roles', {'fields': ('es_cliente', 'es_vendedor', 'es_admin')}),
        ('Marketing', {'fields': ('newsletter', 'terminos_aceptados')}),
        ('Seguridad', {'fields': ('intentos_fallidos', 'bloqueado_hasta')}),
    )
    
    readonly_fields = ['fecha_registro', 'ultimo_acceso']

admin.site.register(Usuario, CustomUserAdmin)

@admin.register(DireccionEnvio)
class DireccionEnvioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'alias', 'comuna', 'region', 'por_defecto']
    list_filter = ['comuna', 'region', 'por_defecto']
    search_fields = ['usuario__username', 'usuario__email', 'calle', 'comuna']
