from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.db.models import Sum, F
from .models import Factura, DetalleFactura
from .forms import FacturaForm, DetalleFacturaForm
from mesas.models import Mesa

def opciones(request):
    return render(request, 'facturacion/opciones.html')

def abrir_factura(request):
    try:
        if request.method == 'POST':
            form = FacturaForm(request.POST)
            if form.is_valid():
                factura = form.save()
                messages.success(request, f'Factura #{factura.id} abierta exitosamente.')
                return redirect('agregar_productos', factura_id=factura.id)
        else:
            form = FacturaForm()
        return render(request, 'facturacion/abrir_factura.html', {'form': form})
    except Exception as e:
        messages.error(request, f'Error al abrir factura: {str(e)}')
        return render(request, 'facturacion/abrir_factura.html', {'form': FacturaForm()})


def agregar_productos(request, factura_id):
    try:
        factura = get_object_or_404(Factura, id=factura_id, estado='abierta')

        if request.method == 'POST':
            form = DetalleFacturaForm(request.POST)
            if form.is_valid():
                detalle = form.save(commit=False)
                detalle.factura = factura
                detalle.save()
                messages.success(request, 'Producto agregado exitosamente.')
                return redirect('agregar_productos', factura_id=factura.id)
            else:
                # Debug: ver errores del formulario
                print("Errores del formulario:", form.errors)
        else:
            form = DetalleFacturaForm()

        detalles = factura.detalles.all()
        total = factura.total()

        return render(request, 'facturacion/agregar_productos.html', {
            'factura': factura,
            'form': form,
            'detalles': detalles,
            'total': total
        })
    except Exception as e:
        print(f"Error completo: {str(e)}")  # Para debug
        messages.error(request, f'Error al agregar productos: {str(e)}')
        return redirect('opciones')


def cerrar_factura(request, factura_id):
    try:
        factura = get_object_or_404(Factura, id=factura_id, estado='abierta')
        
        if request.method == 'POST':
            factura.estado = 'cerrada'
            factura.fecha_cierre = timezone.now()
            factura.save()
            messages.success(request, f'Factura #{factura.id} cerrada exitosamente.')
            return redirect('historial')
        
        total = factura.total()
        return render(request, 'facturacion/cerrar_factura.html', {
            'factura': factura, 
            'total': total
        })
        
    except Exception as e:
        messages.error(request, f'Error al cerrar la factura: {str(e)}')
        return redirect('opciones')

def historial(request):
    hoy = timezone.now().date()
    facturas = Factura.objects.filter(fecha__date=hoy, estado='cerrada').order_by('-fecha')
    total_dia = sum(f.total() for f in facturas)

    return render(request, 'facturacion/historial.html', {
        'facturas': facturas,
        'total_dia': total_dia,
        'fecha': hoy
    })

def facturas_abiertas(request):
    facturas = Factura.objects.filter(estado='abierta').order_by('-fecha')
    return render(request, 'facturacion/facturas_abiertas.html', {
        'facturas': facturas
    })