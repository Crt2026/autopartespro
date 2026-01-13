from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from web.views import ReactAppView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="AutoPartes Pro API",
      default_version='v1',
      description="API para tienda de autopartes",
      terms_of_service="https://www.autopartespro.cl/terms/",
      contact=openapi.Contact(email="contacto@autopartespro.cl"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

from django.contrib.sitemaps.views import sitemap
from web.sitemaps import StaticViewSitemap, ProductSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}

urlpatterns = [
    # Admin Redirect (Fix for no trailing slash)
    path('admin', RedirectView.as_view(url='/admin/', permanent=True)),
    # Admin
    path('admin/', admin.site.urls),
    
    # API
    path('api/', include('api.urls')),
    
    # API Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    # Web App Routes (Home, Products, etc.)
    path('', include('web.urls')),
]

# Servir archivos estáticos y media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Servir media en cualquier entorno (para Railway)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# React App (debe ir al final de todo)
urlpatterns += [
    re_path(r'^.*$', ReactAppView.as_view(), name='react-app'),
]