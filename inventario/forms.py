from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'descripcion', 'precio']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Producto.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Ya existe un producto con ese nombre")
        return nombre