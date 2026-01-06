from django.core.management.base import BaseCommand
from productos.models import Producto, Categoria, Marca
import shutil
import os
from django.conf import settings
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populates the database with initial product data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database...')
        
        # Ensure media directory exists
        media_prod_dir = os.path.join(settings.MEDIA_ROOT, 'productos')
        os.makedirs(media_prod_dir, exist_ok=True)
        
        # Source of images
        static_img_dir = os.path.join(settings.BASE_DIR, 'web', 'static', 'imagenes')

        products_data = [
            { "id": 1, "name": "Filtro Caja Cambio Honda", "brand": "Honda", "price": 35000, "category": "Filtros", "image": "filtro-caja-cambio-honda.jpg", "code": "HON-FIL-001" },
            { "id": 2, "name": "Tuercas de seguridad MG ONE,MG ZS,MG ZX", "brand": "MG", "price": 70000, "category": "Tuercas", "image": "tuercas-de-seguridad-mg.jpg", "code": "MG-TUE-002" },
            { "id": 3, "name": "Venta de repuestos Originales MG", "brand": "MG", "price": 900, "category": "Originales", "image": "venta-de-respuestos-originales-mg.jpg", "code": "MG-REP-003" },
            { "id": 4, "name": "Espejo Honda City 2014 al 2021", "brand": "Honda", "price": 230000, "category": "Espejos", "image": "espejo-honda-city-2014-al-2021.jpg", "code": "HON-ESP-004" },
            { "id": 5, "name": "Mascara Honda Pilot y Ridgeline", "brand": "Honda", "price": 230000, "category": "Mascara", "image": "mascara-honda-pilot-y-ridgeline.jpg", "code": "HON-MAS-005" },
            { "id": 6, "name": "Bomba de agua Honda Pilot o Ridgeline", "brand": "Honda", "price": 230000, "category": "Bomba de Agua", "image": "bomba-de-agua-honda-pilot-o-ridgeline.jpg", "code": "HON-BOM-006" },
            { "id": 7, "name": "Aceite motor Mitsubishi", "brand": "Mitsubishi", "price": 69000, "category": "Aceite", "image": "aceite-motor-mitsubishi.jpg", "code": "MIT-ACE-007" },
            { "id": 8, "name": "Aceite caja Honda cada uno", "brand": "Honda", "price": 13000, "category": "Aceite", "image": "aceite-caja-honda.jpg", "code": "HON-ACE-008" },
            { "id": 9, "name": "Mensula parachoque delantero Honda CRV 2002 al 2006", "brand": "Honda", "price": 40000, "category": "Mensula", "image": "mensula-parach-delantero-honda.jpg", "code": "HON-MEN-009" },
            { "id": 10, "name": "Tapa deposito agua radiador Ford y Mazda. Original Ford", "brand": "Ford y Mazda", "price": 25000, "category": "Tapa deposito agua radiador", "image": "tapa-deposito-agua-radiador-for-mazda.jpg", "code": "FOR-TAP-010" },
            { "id": 11, "name": "Aceite motor 5W30 Honda", "brand": "Honda", "price": 17000, "category": "Aceite", "image": "aceite-motor-honda.jpg", "code": "HON-ACE-011" },
            { "id": 12, "name": "Aceite caja CVT modelos hasta 2014", "brand": "Honda", "price": 17000, "category": "Aceite", "image": "aceite-caja-honda2.jpg", "code": "HON-ACE-012" },
            { "id": 13, "name": "Coolant Original Honda", "brand": "Honda", "price": 35000, "category": "Refrigerante", "image": "colan-original-honda.jpg", "code": "HON-COO-013" },
            { "id": 14, "name": "Aceite Diferencial Honda VTM-4 / 3.8 lts.", "brand": "Honda", "price": 60000, "category": "Aceite", "image": "aceite-diferencial-honda.jpg", "code": "HON-ACE-014" },
            { "id": 15, "name": "Aceite caja ATF-TYPE 3.1", "brand": "Honda", "price": 69000, "category": "Aceite", "image": "aceite-caja-typer-r.jpg", "code": "HON-ACE-015" },
            { "id": 16, "name": "Kit Mantención MG ZX/ZC", "brand": "MG", "price": 105000, "category": "Kit Mantención", "image": "kit-mantencion.jpg", "code": "MG-KIT-016" },
            { "id": 17, "name": "Filtro Combustible MG", "brand": "MG", "price": 15000, "category": "Filtros", "image": "filtro-mg.jpg", "code": "MG-FIL-017" },
            { "id": 18, "name": "Venta de repuestos Originales Ford", "brand": "Ford", "price": 45000, "category": "Originales ford", "image": "for.jpg", "code": "FOR-REP-018" },
            { "id": 19, "name": "Batería de auto 12V", "brand": "Varta", "price": 120000, "category": "Baterías", "image": "disponible-variedad.jpg", "code": "VAR-BAT-019" },
            { "id": 20, "name": "Pastillas de freno Honda Civic", "brand": "Honda", "price": 80000, "category": "Frenos", "image": "410201-PD391H-802.jpg", "code": "HON-FRE-020" },
            { "id": 21, "name": "Amortiguadores delanteros Toyota Corolla", "brand": "Toyota", "price": 150000, "category": "Suspensión", "image": "disponible-variedad.jpg", "code": "TOY-AMO-021" },
            { "id": 22, "name": "Correa de distribución Kia Rio", "brand": "Kia", "price": 50000, "category": "Correas", "image": "disponible-variedad.jpg", "code": "KIA-COR-022" },
            { "id": 23, "name": "Radiador Chevrolet Spark", "brand": "Chevrolet", "price": 90000, "category": "Radiadores", "image": "disponible-variedad.jpg", "code": "CHE-RAD-023" },
            { "id": 24, "name": "Bujías NGK para motor 1.6L", "brand": "NGK", "price": 25000, "category": "Bujías", "image": "disponible-variedad.jpg", "code": "NGK-BUJ-024" }
        ]

        count = 0
        for item in products_data:
            # Create/Get Category
            categoria, _ = Categoria.objects.get_or_create(
                nombre=item['category'],
                defaults={'slug': item['category'].lower().replace(' ', '-')}
            )
            
            # Create/Get Brand
            marca, _ = Marca.objects.get_or_create(
                nombre=item['brand']
            )

            # Copy Image if exists
            img_path = None
            if item['image']:
                src = os.path.join(static_img_dir, item['image'])
                dst = os.path.join(media_prod_dir, item['image'])
                if os.path.exists(src):
                    shutil.copy2(src, dst)
                    img_path = f'productos/{item["image"]}'
            
            # Create Product
            prod, created = Producto.objects.update_or_create(
                SKU=item['code'],
                defaults={
                    'nombre': item['name'],
                    'descripcion': f"Repuesto original {item['brand']} - {item['name']}",
                    'categoria': categoria,
                    'marca': marca,
                    'precio': item['price'],
                    'stock': 10,
                    'activo': True,
                    'nuevo': True,
                    'imagen_principal': img_path
                }
            )
            
            if created:
                count += 1
                self.stdout.write(self.style.SUCCESS(f'Created product: {prod.nombre}'))
            else:
                 self.stdout.write(f'Updated product: {prod.nombre}')

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} new products.'))
