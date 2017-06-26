from django.db import models

# Create your models here.
class Trabajador(models.Model):
	nombre = models.CharField(max_length=50)
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno = models.CharField(max_length=50)
	dni = models.CharField(max_length=7)
	direccion = models.CharField(max_length=90)
	celular =  models.CharField(max_length=9)
	tipo = models.CharField(max_length=20)
	password = models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre