
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from productos.models import Producto

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        # These names must match the names in your urls.py or be handled by your React router
        # Since we use React Router, we need to return the 'paths' that React handles
        # But Django's sitemap expects URL names to reverse.
        # However, our React app handles /*. 
        # So we can't standardly reverse 'about' if it doesn't exist in urls.py.
        #
        # SOLUTION: We will return hardcoded paths or ensure these paths exist conceptually.
        # Since we want /about, /contact, etc.
        return ['home', 'products', 'about', 'contact', 'login', 'register']

    def location(self, item):
        if item == 'home':
            return '/'
        return f'/{item}'

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Producto.objects.filter(activo=True)

    def lastmod(self, obj):
        return obj.updated_at
