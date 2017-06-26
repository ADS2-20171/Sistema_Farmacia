from django.db import models

# Create your models here.
class Proveedor(models.Model):
	codigo = models.IntegerField(default=6)
	nombre = models.CharField(max_length=40)
	razon_social = models.CharField(max_length=100)
	domicilio = models.CharField(max_length=100)
	localidad = models.CharField(max_length=100)
	telefono = models.CharField(max_length=8)
	e_mail = models.EmailField(max_length=100)

	def __unicode__(self):
		return self.nombre