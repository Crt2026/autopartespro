from django.db import models
from django.conf import settings
from productos.models import Producto
import uuid

class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carritos')
    session_key = models.CharField(max_length=40, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'
        ordering = ['-creado']
    
    def __str__(self):
        return f"Carrito #{self.id} - {self.usuario}"
    
    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())
    
    @property
    def cantidad_total(self):
        return sum(item.cantidad for item in self.items.all())

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    agregado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Ítem del carrito'
        verbose_name_plural = 'Ítems del carrito'
        unique_together = ['carrito', 'producto']
    
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    
    @property
    def subtotal(self):
        return self.precio_unitario * self.cantidad
    
    def save(self, *args, **kwargs):
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio_final
        super().save(*args, **kwargs)

class Orden(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('pagada', 'Pagada'),
        ('en_proceso', 'En proceso'),
        ('enviada', 'Enviada'),
        ('entregada', 'Entregada'),
        ('cancelada', 'Cancelada'),
        ('rechazada', 'Rechazada'),
    )
    
    METODOS_PAGO = (
        ('mercadopago', 'Mercado Pago'),
        ('transferencia', 'Transferencia Bancaria'),
        ('efectivo', 'Efectivo'),
        ('dataphone', 'Datáfono'),
    )
    
    METODOS_ENVIO = (
        ('domicilio', 'Despacho a domicilio'),
        ('retiro', 'Retiro en tienda'),
        ('chilexpress', 'Chilexpress'),
        ('starken', 'Starken'),
        ('bluexpress', 'Bluexpress'),
    )
    
    # Identificación
    numero_orden = models.CharField(max_length=20, unique=True, editable=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ordenes', null=True, blank=True)
    
    # Estado y fechas
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_confirmacion = models.DateTimeField(null=True, blank=True)
    fecha_pago = models.DateTimeField(null=True, blank=True)
    fecha_envio = models.DateTimeField(null=True, blank=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    
    # Información del cliente
    cliente_nombre = models.CharField(max_length=100)
    cliente_apellido = models.CharField(max_length=100)
    cliente_email = models.EmailField()
    cliente_telefono = models.CharField(max_length=20)
    cliente_rut = models.CharField(max_length=12, blank=True)
    
    # Dirección de envío
    direccion_calle = models.CharField(max_length=200, blank=True)
    direccion_numero = models.CharField(max_length=20, blank=True)
    direccion_dpto = models.CharField(max_length=20, blank=True)
    direccion_comuna = models.CharField(max_length=100, blank=True)
    direccion_region = models.CharField(max_length=100, blank=True)
    direccion_codigo_postal = models.CharField(max_length=10, blank=True)
    direccion_indicaciones = models.TextField(blank=True)
    
    # Métodos
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    metodo_envio = models.CharField(max_length=20, choices=METODOS_ENVIO)
    
    # Costos
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    iva = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Información de pago
    referencia_pago = models.CharField(max_length=100, blank=True)
    comprobante_pago = models.FileField(upload_to='comprobantes/', blank=True, null=True)
    notas = models.TextField(blank=True)
    
    # Seguimiento
    codigo_seguimiento = models.CharField(max_length=100, blank=True)
    url_seguimiento = models.URLField(blank=True)
    
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Órdenes'
        ordering = ['-fecha_creacion']
        indexes = [
            models.Index(fields=['numero_orden']),
            models.Index(fields=['usuario']),
            models.Index(fields=['estado']),
            models.Index(fields=['fecha_creacion']),
        ]
    
    def __str__(self):
        return f"Orden #{self.numero_orden} - {self.cliente_nombre}"
    
    def save(self, *args, **kwargs):
        if not self.numero_orden:
            # Generar número de orden único
            self.numero_orden = f"ORD-{uuid.uuid4().hex[:8].upper()}"
        
        # Calcular IVA (19% en Chile)
        if not self.iva:
            self.iva = (self.subtotal * 19) / 100
        
        # Calcular total si no está definido
        if not self.total:
            self.total = self.subtotal + self.costo_envio + self.iva - self.descuento
        
        super().save(*args, **kwargs)
    
    @property
    def nombre_completo_cliente(self):
        return f"{self.cliente_nombre} {self.cliente_apellido}"
    
    @property
    def direccion_completa(self):
        if self.metodo_envio == 'retiro':
            return "Retiro en tienda"
        
        parts = []
        if self.direccion_calle:
            parts.append(f"{self.direccion_calle} {self.direccion_numero}")
        if self.direccion_dpto:
            parts.append(f"Depto {self.direccion_dpto}")
        if self.direccion_comuna:
            parts.append(self.direccion_comuna)
        if self.direccion_region:
            parts.append(self.direccion_region)
        
        return ", ".join(parts)

class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Detalle de orden'
        verbose_name_plural = 'Detalles de orden'
    
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    
    def save(self, *args, **kwargs):
        # Calcular subtotal automáticamente
        self.subtotal = self.precio_unitario * self.cantidad
        super().save(*args, **kwargs)

class HistorialOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='historial')
    estado_anterior = models.CharField(max_length=20, blank=True)
    estado_nuevo = models.CharField(max_length=20)
    observaciones = models.TextField(blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Historial de orden'
        verbose_name_plural = 'Historiales de orden'
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.orden.numero_orden} - {self.estado_nuevo}"
