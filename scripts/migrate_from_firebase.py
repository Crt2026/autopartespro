import firebase_admin
from firebase_admin import credentials, firestore
from django.core.management.base import BaseCommand
from productos.models import Producto, Categoria

class Command(BaseCommand):
    help = 'Migra datos de Firebase a Django'
    
    def handle(self, *args, **options):
        # NOTE: You need to set the path to your serviceAccountKey.json
        cred_path = 'c:/Users/Cristobal/Desktop/autopartespro/serviceAccountKey.json' 
        
        try:
            if not firebase_admin._apps:
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
            db = firestore.client()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error initializing Firebase: {e}. Please ensure serviceAccountKey.json exists.'))
            return

        # Migrar categorías
        self.stdout.write('Migrando categorías...')
        categorias_ref = db.collection('categorias')
        categorias = categorias_ref.get()
        
        for doc in categorias:
            data = doc.to_dict()
            categoria, created = Categoria.objects.get_or_create(
                nombre=data['nombre'],
                defaults={'descripcion': data.get('descripcion', '')}
            )
            if created:
                self.stdout.write(f'Categoría creada: {categoria.nombre}')
        
        # Migrar productos
        self.stdout.write('Migrando productos...')
        productos_ref = db.collection('productos')
        productos = productos_ref.get()
        
        count = 0
        for doc in productos:
            data = doc.to_dict()
            
            # Buscar categoría
            categoria_nombre = data.get('categoria', 'General')
            categoria = Categoria.objects.filter(nombre=categoria_nombre).first()
            if not categoria:
                categoria = Categoria.objects.create(nombre=categoria_nombre)
            
            # Crear producto
            Producto.objects.create(
                SKU=data.get('SKU', ''),
                nombre=data['nombre'],
                descripcion=data.get('descripcion', ''),
                marca=data.get('marca', ''),
                precio=data.get('precio', 0) if data.get('precio') else 0,
                stock=data.get('stock', 0),
                categoria=categoria,
                imagen=data.get('imagen', 'productos/default.jpg')
            )
            count += 1
            
        self.stdout.write(self.style.SUCCESS(f'Migración completada. {count} productos migrados.'))
