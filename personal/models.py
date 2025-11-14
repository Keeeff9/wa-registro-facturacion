from django.db import models

# Create your models here.
class Mesero(models.Model):
    codigo = models.CharField(max_length=10,unique=True)
    nombre= models.CharField(max_length=100,)

    class Meta: 
        verbose_name_plural = "Meseros"    

    def __str__(self):
            return f"{self.codigo} - {self.nombre}"