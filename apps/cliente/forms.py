# enconding : utf-8
from django import forms

from .models import Cliente


class ClientesForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'direccion','dni']