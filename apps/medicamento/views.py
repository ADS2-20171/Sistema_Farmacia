from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import MedicamentoCreateForm
from .models import Medicamento
from braces.views import LoginRequiredMixin
# from django.

# Create your views here.

class Listar_medicamento(LoginRequiredMixin, ListView):
	model = Medicamento
	template_name = 'medicamento/listar_medicamento.html'


class Crear_medicamento(LoginRequiredMixin, CreateView):
	form_class = MedicamentoCreateForm
	model = Medicamento
	template_name = 'medicamento/crear_medicamento.html'
	success_url = '/listar_medicamento'
