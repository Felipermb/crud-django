# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class Autenticacao(View):
    """
    View para autenticar usuarios.
    """
    def get(self, request):
        return render(request, 'autenticacao/login.html', {})

    def post(self, request):
        resposta = {
            'sucesso': False,
            'mensagem': ''
        }
        usuario = request.POST.get("login")
        senha = request.POST.get("senha")
        user = authenticate(username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('/index')
        else:
            resposta['mensagem'] = 'Login ou Senha incorreto(s)'

        return render(request, 'autenticacao/login.html', resposta)



class Index(LoginRequiredMixin, View):
    login_url = '/'
    
    def get(self, request):
        
        resposta = {
            'nome' : 'Teste'
        }
        return render(request, 'index.html', resposta)

    def post(self, request):
        return render(request, 'index.html', {})



class NovoPedido(LoginRequiredMixin, View):
    login_url = '/'
    
    def get(self, request):
        
        resposta = {
            'nome' : 'Teste'
        }
        return render(request, 'novoPedido.html', resposta)

    def post(self, request):
        return render(request, 'novoPedido.html', {})

class Contato(LoginRequiredMixin, View):
    login_url = '/'

    def get(self, request):
        resposta = {
            'nome' : 'Teste'
        }
        return render(request, 'contato.html', resposta)

    def post(self, request):
        return render(request, 'contato.html', {})