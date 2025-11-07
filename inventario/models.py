from django.db import models

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
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre})"
    
    
