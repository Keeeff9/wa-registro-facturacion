from django.urls import path
from . import views

urlpatterns =[
    path('', views.lista_meseros, name='lista_meseros'),
]