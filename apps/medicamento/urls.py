from django.conf.urls import url
from .  import views
from .views import Listar_medicamento, Crear_medicamento
urlpatterns = [
		url(r'^listar_medicamento/$', Listar_medicamento.as_view(), name="listar_medicamento"),
		url(r'^crear_medicamento/$', Crear_medicamento.as_view(), name="crear_medicamento"),
]
