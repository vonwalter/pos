# punto_de_venta/urls.py

from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('empresas/', views.lista_empresas, name='lista_empresas'),
    path('empresas/<int:pk>/', views.detalle_empresa, name='detalle_empresa'),
    path('empresas/nueva/', views.crear_empresa, name='crear_empresa'),
    path('puntos_venta/', views.lista_puntos_venta, name='lista_puntos_venta'),
    path('puntos_venta/<int:pk>/', views.detalle_punto_venta, name='detalle_punto_venta'),
    path('puntos_venta/nuevo/', views.crear_punto_venta, name='crear_punto_venta'),
    path('clientes/', views.seleccionar_empresa, name='seleccionar_empresa'),
    path('clientes/<int:empresa_pk>/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:empresa_pk>/<int:cliente_pk>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/<int:empresa_pk>/nuevo/', views.crear_cliente, name='crear_cliente'),
]
