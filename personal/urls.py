from django.urls import path
from . import views

urlpatterns =[
    path('', views.opciones, name='opciones'),
    path('nuevo/', views.nuevo_mesero, name='nuevo_mesero'),
    path('lista/', views.lista_meseros, name='lista_meseros'),
]