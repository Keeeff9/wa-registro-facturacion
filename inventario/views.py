from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def gestion_productos(request):
    return render(request,'inventario/gestion_productos.html')

def lista_productos(request):
    productos= Producto.objects.all().order_by('categoria')
    return render(request,'inventario/lista_productos.html', {'productos': productos})

def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')    
    else:
        form = ProductoForm()

    return render(request, 'inventario/nuevo_producto.html', {'form': form})