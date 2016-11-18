# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from pedido.models import *
from pedido.forms import *
# Create your views here.


class NovoPedido(LoginRequiredMixin, CreateView):
    model = Pedido
    form_class = FormularioPedido
    template_name = 'pedido/novoPedido.html'
    success_url = reverse_lazy('index')

    def get_initial(self):

        print self.request.user, ' --> ', self.request.user.id
        self.initial.update({'user': self.request.user.id })

        return self.initial
