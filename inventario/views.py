from django.shortcuts import render
from .models import Producto
# Create your views here.

def lista_productos(request):
    productos= Producto.objects.select_related('categoria').all()
    return render(request,'inventario/lista_productos.html', {'productos': productos})

    