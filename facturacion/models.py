from django.db import models
from personal.models import Mesero
from mesas.models import Mesa
from inventario.models import Producto
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

class Factura(models.Model):
    ESTADO_CHOISES = [
        ('abierta', 'Abierta'),
        ('cerrada', 'Cerrada'),
    ]

    mesa = models.ForeignKey(Mesa, on_delete=models.PROTECT)
    mesero = models.ForeignKey(Mesero, on_delete=models.PROTECT)
    fecha = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOISES, default='abierta')

    def total(self):
        return sum(item.subtotal() for item in self.detalles.all())
    
    def __str__(self):
        return f"Factura #{self.id} - Mesa {self.mesa.numero} ({self.estado})"
    
    def clean(self):
        if self.estado == 'abierta':            
            factura_abierta = Factura.objects.filter(
                mesa=self.mesa, 
                estado='abierta'
            ).exclude(pk=self.pk).exists()
            
            if factura_abierta:
                raise ValidationError("Ya existe una factura abierta en esta mesa")
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

        facturas_abiertas_en_mesa = Factura.objects.filter(
            mesa=self.mesa, 
            estado='abierta'
        ).exists()
                
        if facturas_abiertas_en_mesa and self.mesa.disponible:
            self.mesa.disponible = False
            self.mesa.save()

        elif not facturas_abiertas_en_mesa and not self.mesa.disponible:
            self.mesa.disponible = True
            self.mesa.save()

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad
        
    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"  
    
    def clean(self):        
        if self.factura_id and self.factura.estado == 'cerrada':
            raise ValidationError("No se pueden modificar detalles de una factura cerrada")
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)