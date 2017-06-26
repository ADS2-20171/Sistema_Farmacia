from django import forms
from .models import Medicamento
from input_mask.widgets import InputMask

class MedicamentoCreateForm(forms.ModelForm):

    class Meta:
        model = Medicamento
        fields = ['nombre', 'codigo', 'componente','concentracion','descripcion','sanitario','tipo','precio_venta','nombre_laboratorio','stock_minimo']