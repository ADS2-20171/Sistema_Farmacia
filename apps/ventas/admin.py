from django.contrib import admin
from .models import Factura, Factura_Detalle

# Register your models here.
admin.site.register(Factura)
admin.site.register(Factura_Detalle)