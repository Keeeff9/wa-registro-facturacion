from django.urls import path
from . import views

urlpatterns = [
    path('', views.opciones, name='opciones'),
    path('abrir/', views.abrir_factura, name='abrir_factura'),
    path('agregar/<int:factura_id>/', views.agregar_productos, name='agregar_productos'),
    path('cerrar/<int:factura_id>/', views.cerrar_factura, name='cerrar_factura'),  
    path('historial/', views.historial, name='historial'),
    path('abiertas/', views.facturas_abiertas, name='facturas_abiertas'),
]