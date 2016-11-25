
# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

class Autenticacao(View):
    """
    View para autenticar usuarios.
    """
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('/index')
        else:
            next_url = request.GET.get('next')
            return render(request, 'autenticacao/login.html', {'next': next_url})

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
            return redirect(request.POST.get('next', '/index'))
        else:
            resposta['mensagem'] = 'Login ou Senha incorreto(s)'

        return render(request, 'autenticacao/login.html', resposta)

    def novousuario(self,request):
        primeiroNome = request.NOVOUSUARIO.get("first-name")
        senha = request.POST.get("senha")

        print self.primeiroNome
        # user = authenticate(username=usuario, password=senha)
        # if user:
        #     login(request, user)
        #     return redirect(request.POST.get('next', '/index'))
        # else:
        #     resposta['mensagem'] = 'Login ou Senha incorreto(s)'

        return redirect(request.NOVOUSUARIO.get('next', '/index'))




class Index(LoginRequiredMixin, View):
    login_url = '/'

    def get(self, request):

        resposta = {
            'nome' : 'Teste'
        }
        return render(request, 'index.html', resposta)

    def post(self, request):
        return render(request, 'index.html', {})



class Contato(LoginRequiredMixin, View):
    login_url = '/'

    def get(self, request):
        resposta = {
            'nome' : 'Teste'
        }
        return render(request, 'contato.html', resposta)

    def post(self, request):
        return render(request, 'contato.html', {})

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('autenticacao')

