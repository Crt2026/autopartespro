from django.urls import path
from .views import ReactAppView

urlpatterns = [
    # Catch-all or specific paths that React handles
    path('', ReactAppView.as_view(), name='home'),
    path('productos/', ReactAppView.as_view(), name='products'),
    path('producto/<slug:slug>/', ReactAppView.as_view(), name='producto-detail'),
    path('carrito/', ReactAppView.as_view(), name='cart'),
    path('login/', ReactAppView.as_view(), name='login'),
    path('registro/', ReactAppView.as_view(), name='register'),
    path('nosotros/', ReactAppView.as_view(), name='about'),
    path('contacto/', ReactAppView.as_view(), name='contact'),
    # Add other React routes here so Django serves index.html for them
]
