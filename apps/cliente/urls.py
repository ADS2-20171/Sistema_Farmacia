from django.conf.urls import patterns, url
from .views import ListaCliente,CreateCliente,ActualizarCliente,EliminarCliente

urlpatterns = patterns('',	
	#clientes
	url(r'^lista_clientes/$', ListaCliente.as_view(), name = 'listar_clientes'),
	url(r'^actualizar_clientes/(?P<pk>\d+)/$', ActualizarCliente.as_view(), name ="actualizar_clientes"), 
	url(r'^eliminar_cliente/(?P<pk>\d+)/$', EliminarCliente.as_view(), name="eliminar_clientes"), 
	url(r'^create_clientes/$', CreateCliente.as_view(), name='crear_clientes'),
  )