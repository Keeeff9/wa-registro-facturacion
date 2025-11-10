from django.shortcuts import render
from .models import Mesa
# Create your views here.

def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesas/lista_mesas.html', {'mesas': mesas})