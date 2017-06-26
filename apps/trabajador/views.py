from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import TrabajadorCreateForm
from .models import Trabajador
from braces.views import LoginRequiredMixin
# from django.

# Create your views here.

class Listar_trabajador(LoginRequiredMixin, ListView):
	model = Trabajador
	template_name = 'trabajador/listar_trabajador.html'


class Crear_trabajador(LoginRequiredMixin, CreateView):
	form_class = TrabajadorCreateForm
	model = Trabajador
	template_name = 'trabajador/crear_trabajador.html'
	success_url = '/listar_trabajador'
