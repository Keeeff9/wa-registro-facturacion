from django import forms
from .models import Mesero

class MeseroForm(forms.ModelForm):
    class Meta:
        model = Mesero
        fields = ['codigo','nombre']

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if Mesero.objects.filter(codigo__iexact=codigo).exists():
            raise forms.ValidationError("Codigo no disponible")
        return codigo