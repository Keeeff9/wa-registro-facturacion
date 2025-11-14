from django.contrib import admin
from .models import Factura, DetalleFactura

# Register your models here.

admin.site.register(Factura)
admin.site.register(DetalleFactura)
