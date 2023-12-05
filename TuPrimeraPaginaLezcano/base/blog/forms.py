from django import forms
from .models import Categoria, Entrada

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'contenido']

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)