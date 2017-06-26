# enconding : utf-8
from django import forms

from .models import Proveedor


class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['codigo', 'nombre', 'razon_social','domicilio','localidad','telefono','e_mail']