from django.db import models
from datetime import datetime
from django.utils import timezone
from apps.trabajador.models import Trabajador
from apps.medicamento.models import Medicamento
# Create your models here.

class Factura(models.Model):
	fecha = models.DateField(default=timezone.now, blank=True)
	numero = models.CharField(max_length=3)
	serie = models.CharField(max_length=5)
	direccion = models.CharField(max_length=100)
	medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
	total = models.CharField(max_length=3)
	vendedor = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
	ruc = models.CharField(max_length=12)
	igv = models.DecimalField(max_digits=8, decimal_places=2)

	def __unicode__(self):
		return str(self.serie)

class Factura_Detalle(models.Model):
	cantidad = models.CharField(max_length=3)
	descripcion = models.CharField(max_length=100)
	precio = models.CharField(max_length=23)
	subtotal = models.CharField(max_length=42)
	factura = models.ForeignKey(Factura)

	def __unicode__(self):
		return str(self.cantidad)