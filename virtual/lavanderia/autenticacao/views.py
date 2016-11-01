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
        	print request.POST.get("login")
        	login = request.POST.get("login")
        	print request.POST.get("senha")
        	senha = request.POST.get("senha")
		return render(request, 'autenticacao/login.html', {})

class Index(View):
    def get(self, request):
        return render(request, 'index.html', {})

    def post(self, request):
        return render(request, 'index.html', {})