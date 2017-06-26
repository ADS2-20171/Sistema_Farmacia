from django.conf.urls import url, patterns
from .  import views
from .views import Listar_medicamento, Crear_medicamento, ActualizarMedicamento, EliminarMedicamento
urlpatterns = patterns('',
		url(r'^listar_medicamento/$', Listar_medicamento.as_view(), name="listar_medicamento"),
		url(r'^crear_medicamento/$', Crear_medicamento.as_view(), name="crear_medicamento"),
		url(r'^actualizar_medicamento/(?P<pk>\d+)/$', ActualizarMedicamento.as_view(), name ="actualizar_medicamento"),
		url(r'^eliminar_medicamento/(?P<pk>\d+)/$', EliminarMedicamento.as_view(), name="eliminar_medicamento"), 
)