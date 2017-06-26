from django.conf.urls import url, patterns
from .  import views
from .views import Listar_compras, Crear_compras, ActualizarCompras, DetalleCompraList

urlpatterns = patterns('',
		url(r'^listar_compras/$', Listar_compras.as_view(), name="listar_compras"),
		url(r'^crear_compras/$', Crear_compras.as_view(), name="crear_compras"),
		url(r'^actualizar_compras/(?P<pk>\d+)/$', ActualizarCompras.as_view(), name ="actualizar_compras"), 
		url(r'^detalle_compras/(?P<pk>\d+)/$',DetalleCompraList.as_view(), name="detalle_compras")
)
