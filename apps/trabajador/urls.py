from django.conf.urls import url
from .  import views
from .views import Listar_trabajador, Crear_trabajador

urlpatterns = [
		url(r'^listar_trabajador/$', Listar_trabajador.as_view(), name="listar_trabajador"),
		url(r'^crear_trabajador/$', Crear_trabajador.as_view(), name="crear_trabajador"),
]
