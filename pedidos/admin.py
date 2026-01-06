from django.contrib import admin
from .models import Orden, DetalleOrden, HistorialOrden

class DetalleOrdenInline(admin.TabularInline):
    model = DetalleOrden
    extra = 0
    readonly_fields = ['producto', 'cantidad', 'precio_unitario', 'subtotal']

class HistorialOrdenInline(admin.TabularInline):
    model = HistorialOrden
    extra = 0
    readonly_fields = ['estado_anterior', 'estado_nuevo', 'observaciones', 'usuario', 'fecha']
    can_delete = False
    
    def has_add_permission(self, request, obj):
        return False

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ['numero_orden', 'cliente_nombre', 'total', 'estado', 'metodo_pago', 'fecha_creacion']
    list_filter = ['estado', 'metodo_pago', 'metodo_envio', 'fecha_creacion']
    search_fields = ['numero_orden', 'cliente_nombre', 'cliente_apellido', 'cliente_email']
    readonly_fields = ['numero_orden', 'fecha_creacion', 'subtotal', 'iva', 'total']
    inlines = [DetalleOrdenInline, HistorialOrdenInline]
    fieldsets = (
        ('Información de la Orden', {
            'fields': ('numero_orden', 'usuario', 'estado', 'fecha_creacion')
        }),
        ('Datos del Cliente', {
            'fields': (
                'cliente_nombre', 'cliente_apellido', 'cliente_email',
                'cliente_telefono', 'cliente_rut'
            )
        }),
        ('Dirección de Envío', {
            'fields': (
                'direccion_calle', 'direccion_numero', 'direccion_dpto',
                'direccion_comuna', 'direccion_region', 'direccion_codigo_postal',
                'direccion_indicaciones'
            )
        }),
        ('Métodos', {
            'fields': ('metodo_pago', 'metodo_envio')
        }),
        ('Costos', {
            'fields': ('subtotal', 'costo_envio', 'descuento', 'iva', 'total')
        }),
        ('Información de Pago', {
            'fields': ('referencia_pago', 'comprobante_pago')
        }),
        ('Seguimiento', {
            'fields': ('codigo_seguimiento', 'url_seguimiento')
        }),
        ('Notas', {
            'fields': ('notas',)
        }),
        ('Fechas', {
            'fields': ('fecha_confirmacion', 'fecha_pago', 'fecha_envio', 'fecha_entrega'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['marcar_como_pagada', 'marcar_como_enviada', 'marcar_como_entregada']
    
    def save_model(self, request, obj, form, change):
        if change:
            # Guardar historial de cambios de estado
            original = Orden.objects.get(pk=obj.pk)
            if original.estado != obj.estado:
                HistorialOrden.objects.create(
                    orden=obj,
                    estado_anterior=original.estado,
                    estado_nuevo=obj.estado,
                    usuario=request.user,
                    observaciones=form.cleaned_data.get('notas', '')
                )
        super().save_model(request, obj, form, change)
    
    def marcar_como_pagada(self, request, queryset):
        queryset.update(estado='pagada')
    marcar_como_pagada.short_description = "Marcar como pagada"
    
    def marcar_como_enviada(self, request, queryset):
        queryset.update(estado='enviada')
    marcar_como_enviada.short_description = "Marcar como enviada"
    
    def marcar_como_entregada(self, request, queryset):
        queryset.update(estado='entregada')
    marcar_como_entregada.short_description = "Marcar como entregada"
