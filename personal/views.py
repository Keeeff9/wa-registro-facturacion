from django.shortcuts import render
from .models import Mesero
# Create your views here.

def lista_meseros(request):
    meseros = Mesero.objects.all()
    return render(request, 'personal/lista_meseros.html', {'meseros':meseros})
