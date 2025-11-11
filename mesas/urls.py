from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mesas, name='lista_mesas'),
    path('nueva/', views.nueva_mesa, name='nueva_mesa'),
]