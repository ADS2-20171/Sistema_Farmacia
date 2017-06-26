from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin
from .forms import ProveedorForm
from .models import Proveedor


class ListaProveedor(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'proveedor/listar_proveedor.html'


class CreateProveedor(LoginRequiredMixin, CreateView):
    form_class = ProveedorForm
    template_name = 'proveedor/crear_proveedor.html'
    model = Proveedor
    success_url = '/listar_proveedor'


class ActualizarProveedor(UpdateView):
    form_class = ProveedorForm
    template_name = 'proveedor/actualizar_proveedor.html'
    model = Proveedor
    success_url = '/listar_proveedor'


class EliminarProveedor(DeleteView):
    model = Proveedor
    success_url = '/listar_proveedor'
    template_name = 'proveedor/eliminar_proveedor.html'
    group_required = ['administrador']
