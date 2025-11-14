from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100,unique=True)

    class Meta:
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria= models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name='products')
    nombre= models.CharField(max_length=100,unique=True)
    descripcion= models.TextField(blank=True,null=True)
    precio=models.IntegerField(
        verbose_name="Precio (COP)",
        validators=[MinValueValidator(50)],
        help_text="precio en pesos colombianos"
    )

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre})"
    
    def precio_formateado(self):
        return f"{self.precio:,.0f}".replace(",",".")
    
    
