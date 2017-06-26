# enconding : utf-8
from django import forms

from .models import Compras, Detalle_compra
from input_mask.widgets import InputMask
from bootstrap3_datetime.widgets import DateTimePicker

class ComprasForm(forms.ModelForm):

    class Meta:
        model = Compras
        fields = ['fecha', 'codigo','medicamento','proveedor','trabajador', 'total']
        widgets = {
        	'fecha': forms.TextInput(attrs={
				'type' : 'date',
				 'placeholder' : 'ingrese fecha de compra'
				}),
        	'codigo' : forms.TextInput(attrs={
        		 'type': 'text',
        		 'placeholder' : 'ingrese el codigo de compra'
        		}),
        	'total' :forms.TextInput(attrs={
        		'type' : 'number',
        		'placeholder' : 'ingrese el total de la compra'
           		})
        }

class DetalleCompraForm(forms.ModelForm):

    class Meta:
        model = Detalle_compra
        fields = ['cantidad', 'estado', 'fecha_produccion', 'fecha_expiracion', 'notificacion_stock', 'notificacion_fecha_expiracion', 'igv','compras']
