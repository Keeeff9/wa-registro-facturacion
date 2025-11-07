from django.db import models
from django.utils import timezone
from inventario.models import Producto
from mesas.models import Mesa
from personal.models import Mesero

# Create your models here.

class Factura(models.Model):
    mesa= models.OneToOneField(Mesa, on_delete=models.PROTECT)
    mesero= models.ForeignKey(Mesero, on_delete=models.PROTECT, related_name="facturas")
    fecha_apertura = models.DateTimeField(default=timezone.now)
    fecha_cierre = models.DateTimeField(blank=True,null=True)
    cerrada = models.BooleanField(default=False)

    def total(self):
        return sum(detalle.subtotal() for detalle in self.delete.all())
    
    def __str__(self):
        return f"Factura {self.id} - Mesa {self.mesa.numero} ({'Cerrada' if self.cerrada else 'Abierta'})"
    
class Detalle(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='detalles')
    Producto = models.ForeignKey(Producto,on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.Producto.precio * self.cantidad
    
    def __str__(self):
        return f"{self.cantidad} x {self.Producto.nombre}"
