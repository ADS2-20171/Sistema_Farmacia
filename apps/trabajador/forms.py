# enconding : utf-8
from django import forms
from .models import Trabajador
from input_mask.widgets import InputMask

class TrabajadorCreateForm(forms.ModelForm):

    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellido_paterno', 'apellido_materno','dni','direccion','celular','tipo','password']