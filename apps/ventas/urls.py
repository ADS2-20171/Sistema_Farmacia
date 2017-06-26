from django.conf.urls import patterns, url
from .views import ListaVentas,CreateVentas,ActualizarVentas,EliminarVentas

urlpatterns = patterns('',	
	#clientes
	url(r'^listar_ventas/$', ListaVentas.as_view(), name = 'listar_ventas'),
	url(r'^actualizar_ventas/(?P<pk>\d+)/$', ActualizarVentas.as_view(), name ="actualizar_ventas"), 
	url(r'^eliminar_ventas/(?P<pk>\d+)/$', EliminarVentas.as_view(), name="eliminar_ventas"), 
	url(r'^create_ventas/$', CreateVentas.as_view(), name='crear_ventas'),
  )