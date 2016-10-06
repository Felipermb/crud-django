# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render

class Autenticacao(View):
    """
    View para autenticar usuarios.
    """
    def get(self, request):
        return render(request, 'autenticacao/login.html', {})

    def post(self, request):

        # print request.POST.get('senha')  #"pegar somente a senha"

		return render(request, 'autenticacao/login.html', {})