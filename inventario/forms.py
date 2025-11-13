from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'descripcion', 'precio']
        widgets ={
            'precio': forms.NumberInput(attrs={
                'placeholder': 'Ej: 15000',
                'min': '50'
            })
        }
    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 50:
            raise forms.ValidationError("El precio debe ser mayor a 50 pesos")
        return precio
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if self.instance.pk:
            if Producto.objects.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Ya existe un producto con ese nombre")
        else:
            # Si estamos creando un nuevo producto
            if Producto.objects.filter(nombre__iexact=nombre).exists():
                raise forms.ValidationError("Ya existe un producto con ese nombre")
        return nombre
    