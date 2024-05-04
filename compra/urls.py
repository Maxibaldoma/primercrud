from django.urls import path
from . import views

app_name = 'compra'


urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),  # URL para listar productos
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),  # URL para agregar producto
    path('agregar-proveedores/', views.agregar_proveedor, name='agregar_proveedor'),  # URL para agregar proveedor
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),  # URL para listar proveedores
    ]
