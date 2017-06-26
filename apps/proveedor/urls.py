from django.conf.urls import patterns, url
from .views import ListaProveedor,CreateProveedor,ActualizarProveedor,EliminarProveedor

urlpatterns = patterns('',	
	#clientes
	url(r'^listar_proveedor/$', ListaProveedor.as_view(), name="listar_proveedor"),
	url(r'^actualizar_proveedor/(?P<pk>\d+)/$', ActualizarProveedor.as_view(), name ="actualizar_proveedor"), 
	url(r'^eliminar_proveedor/(?P<pk>\d+)/$', EliminarProveedor.as_view(), name="eliminar_proveedor"), 
	url(r'^crear_proveedor/$', CreateProveedor.as_view(), name='crear_proveedor'),
  )	