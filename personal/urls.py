from django.urls import path
from . import views

urlpatterns =[
    path('', views.lista_meseros, name='lista_meseros'),
    path('nuevo/', views.nuevo_mesero, name='nuevo_mesero'),
]