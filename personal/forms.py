from django import forms
from .models import Mesero

class MeseroForm(forms.ModelForm):
    class Meta:
        model = Mesero
        fields = ['nombre', 'telefono', 'email']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Mesero.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Ya existe un mesero con ese nombre")
        return nombre