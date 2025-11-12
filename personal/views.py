from django.shortcuts import render, redirect
from .models import Mesero
from .forms import MeseroForm
# Create your views here.

def opciones(request):
    return render(request,'personal/opciones.html')

def lista_meseros(request):
    meseros = Mesero.objects.all()
    return render(request, 'personal/lista_meseros.html', {'meseros':meseros})

def nuevo_mesero(request):
    if request.method == 'POST':
        form = MeseroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_meseros')
    else:
        form = MeseroForm()
    return render(request, 'personal/nuevo_mesero.html', {'form':form})

