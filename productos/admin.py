from django.contrib import admin
from .models import Categoria, Marca, Producto, ProductoImagen
from django.utils.html import format_html

class ProductoImagenInline(admin.TabularInline):
    model = ProductoImagen
    extra = 1
    fields = ['imagen', 'preview', 'orden', 'descripcion']
    readonly_fields = ['preview']
    
    def preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-height: 80px; max-width: 80px;" />', obj.imagen.url)
        return "Sin imagen"
    preview.short_description = "Vista previa"

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Added 'destacado' to list_display to match list_editable
    list_display = ['imagen_preview', 'nombre', 'SKU', 'precio_final_display', 'stock_status', 'categoria', 'marca', 'destacado', 'activo']
    list_display_links = ['nombre', 'imagen_preview']
    list_filter = ['categoria', 'marca', 'activo', 'destacado', 'nuevo']
    search_fields = ['nombre', 'SKU', 'descripcion', 'modelo_compatible']
    list_editable = ['activo', 'destacado']
    
    fieldsets = (
        ('Información General', {
            'fields': (
                ('nombre', 'SKU'),
                ('slug', 'activo'),
                'descripcion',
                'descripcion_corta'
            )
        }),
        ('Clasificación', {
            'fields': (('categoria', 'marca'), ('destacado', 'nuevo'))
        }),
        ('Precios y Stock', {
            'fields': (
                ('precio', 'precio_antes'),
                ('costo', 'stock'),
                'stock_minimo'
            ),
            'description': 'Gestione aquí los precios de venta y el inventario disponible.'
        }),
        ('Multimedia Principal', {
            'fields': ('imagen_principal', 'imagen_principal_preview')
        }),
        ('Especificaciones Técnicas', {
            'fields': (
                ('modelo_compatible', 'año_compatible'),
                ('peso', 'dimensiones'),
                'garantia'
            ),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [ProductoImagenInline]
    readonly_fields = ['slug', 'created_at', 'updated_at', 'imagen_principal_preview']
    
    def imagen_principal_preview(self, obj):
        if obj.imagen_principal:
            return format_html('<img src="{}" style="max-height: 200px; max-width: 200px; border-radius: 5px;" />', obj.imagen_principal.url)
        return "Sin imagen"
    imagen_principal_preview.short_description = "Vista Previa Actual"

    def imagen_preview(self, obj):
        if obj.imagen_principal:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px; border-radius: 3px;" />', obj.imagen_principal.url)
        return ""
    imagen_preview.short_description = "Img"

    def precio_final_display(self, obj):
        color = "green" if obj.precio_antes else "black"
        return format_html('<span style="color: {}; font-weight: bold;">${}</span>', color, obj.precio_final)
    precio_final_display.short_description = "Precio Final"

    def stock_status(self, obj):
        if obj.stock == 0:
            return format_html('<span style="color: red;">AGOTADO</span>')
        elif obj.stock <= obj.stock_minimo:
            return format_html('<span style="color: orange;">BAJO ({})</span>', obj.stock)
        return format_html('<span style="color: green;">OK ({})</span>', obj.stock)
    stock_status.short_description = "Stock"

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'icon_preview', 'producto_count', 'activo']
    search_fields = ['nombre']
    
    def icon_preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-height: 30px;" />', obj.imagen.url)
        return ""
    icon_preview.short_description = "Icono"
    
    def producto_count(self, obj):
        return obj.productos.count()
    producto_count.short_description = "Productos Asociados"

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'logo_preview', 'activa']
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 30px;" />', obj.logo.url)
        return ""
    logo_preview.short_description = "Logo"
