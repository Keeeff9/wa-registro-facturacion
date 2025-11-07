from django.db import models

# Create your models here.
class Mesero(models.Model):
    nombre = models.CharField(max_length=100)
    telefono= models.CharField(max_length=100,blank=True,null=True)
    email= models.EmailField(blank=True,null=True)

    def __str__(self):
            return f"{self.id} - {self.nombre}"