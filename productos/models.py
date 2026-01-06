from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    descripcion = models.TextField(blank=True)
    imagen = models.FileField(upload_to='categorias/', blank=True, null=True)
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['orden', 'nombre']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('categoria-detail', kwargs={'slug': self.slug})

class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    logo = models.FileField(upload_to='marcas/', blank=True, null=True)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    # Información básica
    SKU = models.CharField(max_length=50, unique=True, verbose_name='Código SKU')
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    descripcion = models.TextField()
    descripcion_corta = models.CharField(max_length=300, blank=True)
    
    # Relaciones
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos')
    
    # Precios y stock
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_antes = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Precio anterior')
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=5, verbose_name='Stock mínimo')
    
    # Especificaciones técnicas
    modelo_compatible = models.CharField(max_length=200, blank=True, verbose_name='Modelos compatibles')
    año_compatible = models.CharField(max_length=100, blank=True, verbose_name='Años compatibles')
    garantia = models.CharField(max_length=100, blank=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text='Peso en kg')
    dimensiones = models.CharField(max_length=100, blank=True, help_text='Alto x Ancho x Profundidad (cm)')
    
    # Imágenes
    imagen_principal = models.FileField(upload_to='productos/')
    imagen_2 = models.FileField(upload_to='productos/', blank=True, null=True)
    imagen_3 = models.FileField(upload_to='productos/', blank=True, null=True)
    imagen_4 = models.FileField(upload_to='productos/', blank=True, null=True)
    
    # Estado y metadata
    destacado = models.BooleanField(default=False)
    nuevo = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['SKU']),
            models.Index(fields=['nombre']),
            models.Index(fields=['categoria']),
            models.Index(fields=['precio']),
            models.Index(fields=['destacado']),
        ]
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.nombre}-{self.SKU}")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nombre} ({self.SKU})"
    
    def get_absolute_url(self):
        return reverse('producto-detail', kwargs={'slug': self.slug})
    
    @property
    def precio_final(self):
        """Devuelve el precio con descuento si aplica"""
        if self.precio_antes:
            return self.precio
        return self.precio
    
    @property
    def descuento_porcentaje(self):
        """Calcula el porcentaje de descuento"""
        if self.precio_antes and self.precio_antes > self.precio:
            return int(((self.precio_antes - self.precio) / self.precio_antes) * 100)
        return 0
    
    @property
    def en_stock(self):
        """Verifica si hay stock disponible"""
        return self.stock > 0
    
    @property
    def stock_bajo(self):
        """Alerta cuando el stock es bajo"""
        return self.stock <= self.stock_minimo
    
    def reducir_stock(self, cantidad):
        """Reduce el stock al realizar una venta"""
        if cantidad <= self.stock:
            self.stock -= cantidad
            self.save()
            return True
        return False
    
    def aumentar_stock(self, cantidad):
        """Aumenta el stock (reposición)"""
        self.stock += cantidad
        self.save()

class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.FileField(upload_to='productos/galeria/')
    orden = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=200, blank=True)
    
    class Meta:
        ordering = ['orden']
        verbose_name = 'Imagen de producto'
        verbose_name_plural = 'Imágenes de productos'
    
    def __str__(self):
        return f"Imagen de {self.producto.nombre}"
