from django.db import models


# Create your models here.
class Medicamento(models.Model):
	nombre = models.CharField(max_length=30)
	codigo = models.CharField(max_length=6)
	componente = models.CharField(max_length=50)
	concentracion = models.CharField(max_length=60)
	descripcion = models.CharField(max_length=100)
	sanitario = models.CharField(max_length=60)
	tipo = models.CharField(max_length=30)
	precio_venta = models.DecimalField(max_digits=10,decimal_places=10)
	nombre_laboratorio = models.CharField(max_length=50)
	stock_minimo =  models.IntegerField(default=3)
	
	def __unicode__(self):
		return self.nombre