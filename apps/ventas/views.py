from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin
from .forms import CreateVentasForm
from .models import Factura


class ListaVentas(LoginRequiredMixin, ListView):
    model = Factura
    template_name = 'ventas/listar_ventas.html'


class CreateVentas(LoginRequiredMixin, CreateView):
    form_class = CreateVentasForm
    template_name = 'ventas/crear_ventas.html'
    model = Factura
    success_url = '/listar_ventas'


class ActualizarVentas(UpdateView):
    form_class = CreateVentasForm
    template_name = 'ventas/crear_ventas.html'
    model = Factura
    success_url = '/listar_ventas'


class EliminarVentas(DeleteView):
    model = Factura
    success_url = '/listar_ventas'
    template_name = 'ventas/eliminar_ventas.html'
    group_required = ['administrador']
