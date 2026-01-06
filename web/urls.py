from django.urls import path
from .views import ReactAppView

urlpatterns = [
    # Catch-all or specific paths that React handles
    path('', ReactAppView.as_view(), name='home'),
    path('productos/', ReactAppView.as_view(), name='products'),
    path('carrito/', ReactAppView.as_view(), name='cart'),
    path('login/', ReactAppView.as_view(), name='login'),
    # Add other React routes here so Django serves index.html for them
]
