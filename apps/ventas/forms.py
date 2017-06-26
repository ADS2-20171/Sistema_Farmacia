# enconding : utf-8
from django import forms

from .models import Factura, Factura_Detalle


class CreateVentasForm(forms.ModelForm):

    class Meta:
        model = Factura
        fields = ['fecha', 'numero', 'serie','direccion','total','vendedor','ruc','igv']

