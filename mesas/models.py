from django.db import models

# Create your models here.
class Mesa(models.Model):
    numero=models.PositiveIntegerField(unique=True)
    disponible=models.BooleanField(default=True)

    def __str__(self):
        estado= "Disponible" if self.disponible else "Ocupada"
        return f"Mesa {self.numero} - {estado}"