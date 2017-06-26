from django.db import models
from django.utils import timezone
from apps.medicamento.models import Medicamento
from apps.trabajador.models import Trabajador
from apps.proveedor.models import Proveedor

# Create your models here.
class Compras(models.Model):
	fecha = models.DateTimeField(default=timezone.now)
	codigo = models.CharField(max_length=6)
	medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
	total = models.CharField(max_length=23)

	

	def __unicode__(self):
		return str(self.codigo)

class Detalle_compra(models.Model):
	cantidad = models.CharField(max_length=4)
	estado = models.BooleanField(default=True)
	fecha_produccion = models.DateField(default=timezone.now, blank=True)
	fecha_expiracion = models.DateField(default=timezone.now, blank=True)
	notificacion_stock = models.CharField(max_length=32)
	notificacion_fecha_expiracion = models.CharField(max_length=32)
	igv = models.DecimalField(max_digits=8, decimal_places=2)
	compras = models.ForeignKey(Compras, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.cantidad)
