from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mesas, name='lista_mesas'),
]