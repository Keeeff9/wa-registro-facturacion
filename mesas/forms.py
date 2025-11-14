from django import forms
from .models import Mesa

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero', 'disponible']

    def clean_numero(self):
        numero = self.cleaned_data['numero']
        if Mesa.objects.filter(numero=numero).exists():
            raise forms.ValidationError("Esa mesa ya existe")
        return numero