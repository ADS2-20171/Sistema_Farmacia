from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
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

class ActualizarMedicamento(UpdateView):
    form_class = MedicamentoCreateForm
    template_name = 'medicamento/crear_medicamento.html'
    model = Medicamento
    success_url = '/listar_medicamento'

class EliminarMedicamento(DeleteView):
    model = Medicamento
    success_url = '/lista_medicamento'
    template_name = 'medicamento/eliminar_medicamento.html'
    group_required = ['administrador']