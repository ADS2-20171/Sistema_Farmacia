from django.db import models

# Create your models here.

class Cliente(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	direccion =  models.CharField(max_length=80)
	dni = models.CharField(max_length=8)

	def __unicode__(self):
		return self.nombre