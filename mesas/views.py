from django.shortcuts import render, redirect
from .models import Mesa
from .forms import MesaForm
# Create your views here.

def opciones_mesas(request):
    return render(request,'mesas/opciones_mesas.html')
 
def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesas/lista_mesas.html', {'mesas': mesas})

def nueva_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mesas')
    else:
        form = MesaForm()

    return render(request, 'mesas/nueva_mesa.html', {'form':form})