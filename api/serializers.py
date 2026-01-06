from rest_framework import serializers
from productos.models import Producto, Categoria, Marca
from pedidos.models import Carrito, ItemCarrito, Orden, DetalleOrden
from usuarios.models import Usuario, DireccionEnvio

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'slug', 'descripcion', 'imagen']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre', 'logo', 'descripcion']

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), 
        source='categoria',
        write_only=True
    )
    marca = MarcaSerializer(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(
        queryset=Marca.objects.all(),
        source='marca',
        write_only=True,
        required=False,
        allow_null=True
    )
    
    precio_final = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    descuento_porcentaje = serializers.IntegerField(read_only=True)
    en_stock = serializers.BooleanField(read_only=True)
    stock_bajo = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Producto
        fields = [
            'id', 'SKU', 'nombre', 'slug', 'descripcion', 'descripcion_corta',
            'categoria', 'categoria_id', 'marca', 'marca_id',
            'precio', 'precio_antes', 'precio_final', 'descuento_porcentaje',
            'stock', 'stock_bajo', 'en_stock', 'modelo_compatible', 'año_compatible',
            'garantia', 'peso', 'dimensiones', 'imagen_principal',
            'destacado', 'nuevo', 'activo', 'created_at'
        ]

class ItemCarritoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.filter(activo=True),
        source='producto',
        write_only=True
    )
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = ItemCarrito
        fields = ['id', 'producto', 'producto_id', 'cantidad', 'precio_unitario', 'subtotal']

class CarritoSerializer(serializers.ModelSerializer):
    items = ItemCarritoSerializer(many=True, read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    cantidad_total = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Carrito
        fields = ['id', 'usuario', 'items', 'total', 'cantidad_total', 'creado', 'actualizado']

class DetalleOrdenSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    
    class Meta:
        model = DetalleOrden
        fields = ['id', 'producto', 'cantidad', 'precio_unitario', 'subtotal']

class OrdenSerializer(serializers.ModelSerializer):
    detalles = DetalleOrdenSerializer(many=True, read_only=True)
    nombre_completo_cliente = serializers.CharField(read_only=True)
    direccion_completa = serializers.CharField(read_only=True)
    
    class Meta:
        model = Orden
        fields = [
            'id', 'numero_orden', 'usuario', 'estado',
            'cliente_nombre', 'cliente_apellido', 'nombre_completo_cliente',
            'cliente_email', 'cliente_telefono', 'cliente_rut',
            'direccion_calle', 'direccion_numero', 'direccion_dpto',
            'direccion_comuna', 'direccion_region', 'direccion_codigo_postal',
            'direccion_indicaciones', 'direccion_completa',
            'metodo_pago', 'metodo_envio',
            'subtotal', 'costo_envio', 'descuento', 'iva', 'total',
            'referencia_pago', 'comprobante_pago', 'notas',
            'codigo_seguimiento', 'url_seguimiento',
            'detalles', 'fecha_creacion', 'fecha_pago', 'fecha_envio', 'fecha_entrega'
        ]
        read_only_fields = ['numero_orden', 'fecha_creacion']

class DireccionEnvioSerializer(serializers.ModelSerializer):
    direccion_completa = serializers.SerializerMethodField()
    
    class Meta:
        model = DireccionEnvio
        fields = [
            'id', 'usuario', 'alias', 'nombre', 'apellido', 'telefono',
            'calle', 'numero', 'dpto', 'comuna', 'region', 'codigo_postal',
            'indicaciones', 'por_defecto', 'direccion_completa',
            'creado', 'actualizado'
        ]
        read_only_fields = ['usuario', 'creado', 'actualizado']
    
    def get_direccion_completa(self, obj):
        return obj.direccion_completa()

class UsuarioSerializer(serializers.ModelSerializer):
    direcciones = DireccionEnvioSerializer(many=True, read_only=True)
    ordenes_count = serializers.IntegerField(read_only=True)
    total_gastado = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'rut', 'telefono', 'direccion', 'comuna', 'region',
            'es_cliente', 'es_vendedor', 'es_admin',
            'newsletter', 'terminos_aceptados',
            'codigo_cliente', 'fecha_registro', 'ultimo_acceso',
            'direcciones', 'ordenes_count', 'total_gastado',
            'is_active', 'date_joined', 'last_login'
        ]
        read_only_fields = ['codigo_cliente', 'fecha_registro', 'date_joined', 'last_login']
