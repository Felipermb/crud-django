# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from pedido.models import *
from pedido.forms import *
from pedido.const import *
# Create your views here.


class NovoPedido(LoginRequiredMixin, CreateView):
    model = Pedido
    form_class = FormularioPedido
    template_name = 'pedido/novoPedido.html'
    success_url = reverse_lazy('listar-pedidos')

    def get_initial(self):
        print self.request.user, ' --> ', self.request.user.id
        self.initial.update({'user': self.request.user.id })
        return self.initial

    # def get_context_data(self, **kwargs):
    #     context = super(NovoPedido, self).get_context_data(**kwargs)
    #     context['n_form'] = FormularioTipoRoupa()
    #     return context

        

class ListarPedido(ListView):
    """
    View para listar veiculos cadastrados.
    """
    model = Pedido
    template_name = 'pedido/historico.html'
