from django.urls import path
from . import views

urlpatterns = [
    path('', views.opciones_mesas, name='opciones_mesas'),
    path('nueva/', views.nueva_mesa, name='nueva_mesa'),
    path('lista/', views.lista_mesas, name='lista_mesas'),
]