from django import forms
from .models import Factura, DetalleFactura
from mesas.models import Mesa
from personal.models import Mesero
from inventario.models import Categoria, Producto

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields= ['mesa', 'mesero']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mesa'].queryset = Mesa.objects.filter(disponible=True)
        self.fields['mesero'].queryset = Mesero.objects.all()

class DetalleFacturaForm(forms.ModelForm):

    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=True,
        label="Categoría"
    )

    class Meta:
        model = DetalleFactura
        fields = ['categoria', 'producto', 'cantidad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['producto'].queryset = Producto.objects.none()

        if 'categoria' in self.data:
            try:
                categoria_id = int(self.data.get('categoria'))
                self.fields['producto'].queryset = Producto.objects.filter(categoria_id=categoria_id)
            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            categoria = self.instance.producto.categoria
            self.fields['categoria'].initial = categoria
            self.fields['producto'].queryset = Producto.objects.filter(categoria=categoria)
