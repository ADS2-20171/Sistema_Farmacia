from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import ComprasForm, DetalleCompraForm
from .models import Compras, Detalle_compra
from braces.views import LoginRequiredMixin
# from django.

# Create your views here.

class Listar_compras(LoginRequiredMixin, ListView):
	model = Compras
	template_name = 'compras/listar_compras.html'


class Crear_compras(LoginRequiredMixin, CreateView):
	form_class = ComprasForm
	model = Compras
	template_name = 'compras/crear_compras.html'
	success_url = '/listar_compras'

class ActualizarCompras(UpdateView):
    form_class = ComprasForm
    template_name = 'compras/crear_compras.html'
    model = Compras
    success_url = '/listar_compras'


class DetalleCompraList(LoginRequiredMixin, ListView):
	model = Detalle_compra
	form_class = DetalleCompraForm
	template_name = 'compras/detalle_compras.html'


	
# class CreateCliente(LoginRequiredMixin, CreateView):
# 	form_class = ClienteForm
# 	template_name = 'clientes/create_update_clientes.html'
# 	model = Cliente
# 	success_url = '/lista_clientes'


# class ActualizarCompra(UpdateView):
# 	form_class = ComprasForm
# 	template_name = 'clientes/create_update_clientes.html'
# 	model = Cliente
# 	success_url='/lista_clientes'

# class ListaCliente(LoginRequiredMixin,GroupRequiredMixin, ListView):
# 	context_object_name = 'clientes'
# 	model = Cliente
# 	template_name = 'clientes/lista_cliente.html'
# 	group_required = ['trabajadores']


# Create your views here.
# class DetalleView(LoginRequiredMixin, DetailView):
# 	model = Cliente
# 	template_name = 'clientes/detalle_clientes.html'





# class EliminarView(GroupRequiredMixin, DeleteView):
# 	model = Cliente
# 	success_url='/lista_clientes'
# 	template_name = 'clientes/eliminar_cliente.html'
# 	group_required = ['administrador']

