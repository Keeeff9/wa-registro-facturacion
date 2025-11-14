from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestion_productos, name='gestion_productos'),
    path('lista/', views.lista_productos, name='lista_productos'),
    path('nuevo/', views.nuevo_producto, name='nuevo_producto'),
]