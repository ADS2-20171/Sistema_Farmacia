from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin
from .forms import ClientesForm
from .models import Cliente


class ListaCliente(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/lista_cliente.html'


class CreateCliente(LoginRequiredMixin, CreateView):
    form_class = ClientesForm
    template_name = 'clientes/crear_clientes.html'
    model = Cliente
    success_url = '/lista_clientes'


class ActualizarCliente(UpdateView):
    form_class = ClientesForm
    template_name = 'clientes/crear_clientes.html'
    model = Cliente
    success_url = '/lista_clientes'


class EliminarCliente(DeleteView):
    model = Cliente
    success_url = '/lista_clientes'
    template_name = 'clientes/eliminar_cliente.html'
    group_required = ['administrador']
