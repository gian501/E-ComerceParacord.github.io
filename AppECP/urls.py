from django.urls import path
from .views import *
from AppECP import views

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('register/', register, name='register'),
    path('datos_usuarios/', datos_usuarios, name='datos_usuarios'),
    path('aboutus/', aboutus, name='aboutus'),
    path('busquedaProducto', busquedaProducto, name= "busquedaProducto"),
    path('editarPerfil', editarPerfil, name="EditarPerfil"),

    path('producto/list', views.ProductoListView.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ProductoDetailView.as_view(), name='Detail'),
    path(r'^nuevo$', views.ProductoCreateView.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ProductoUpdateView.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProductoDeleteView.as_view(), name='Delete'),

        # CARRITO
    path('carrito', views.carrito_index, name="carrito_index"),
    path('carrito/agregar', views.carrito_save, name="carrito_save"),
    path('carrito/clean', views.carrito_clean, name="carrito_clean"),
    path('item_carrito/<int:item_carrito_id>/eliminar', views.item_carrito_delete, name="item_carrito_delete"),
]