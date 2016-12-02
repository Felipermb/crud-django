
# -*- coding: utf-8 -*-
from django.views.generic import View ,CreateView, DeleteView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from autenticacao.models import *
from autenticacao.forms import *
from django.db import IntegrityError


class ListarCartao(LoginRequiredMixin, ListView):
    login_url='/'
    model = Cartao
    template_name = 'autenticacao/listarCartao.html'

    def get_queryset(self):
        self.request_user = self.request.user
        return Cartao.objects.filter(cliente__user=self.request_user)

class ListarEndereco(LoginRequiredMixin, ListView):
    login_url='/'
    model = Endereco
    template_name = 'autenticacao/listarEndereco.html'

    def get_queryset(self):
        self.request_user = self.request.user
        return Endereco.objects.filter(cliente__user=self.request_user)

    

class DeletarCartao(LoginRequiredMixin, DeleteView):
    login_url='/'
    model = Cartao
    template_name = 'autenticacao/deletar_cartao.html'
    success_url = reverse_lazy('listar_cartao')

class DeletarEndereco(LoginRequiredMixin, DeleteView):
    login_url='/'
    model = Endereco
    template_name = 'autenticacao/deletar_endereco.html'
    success_url = reverse_lazy('listar_endereco')


class NovoCartao(LoginRequiredMixin, CreateView):
    model = Cartao
    form_class = FormularioCartao
    template_name = 'autenticacao/cartao.html'
    success_url = reverse_lazy('index')

    def get_initial(self):
        print self.request.user, ' --> ', self.request.user.id
        self.initial.update({'user': self.request.user.id })
        return self.initial


class NovoEndereco(LoginRequiredMixin, CreateView):
    model = Endereco
    form_class = FormularioEndereco
    template_name = 'autenticacao/endereco.html'
    success_url = reverse_lazy('index')

    def get_initial(self):
        print self.request.user, ' --> ', self.request.user.id
        self.initial.update({'user': self.request.user.id })
        return self.initial




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
        acao = request.POST.get('acao', 'login')



        print acao

        acao_list = {
            'login': self.login,
            'cadastrar': self.cadastrar
        }
        return acao_list[acao]()

    def login (self):
        resposta = {
            'sucesso': False,
            'mensagem': ''
        }
        usuario = self.request.POST.get("login")
        senha = self.request.POST.get("senha")
        user = authenticate(username=usuario, password=senha)
        if user:
            login(self.request, user)
            return redirect(self.request.POST.get('next', '/index'))
        else:
            resposta['mensagem'] = 'Login ou Senha incorreto(s)'

        return render(self.request, 'autenticacao/login.html', resposta)

    def cadastrar(self):
        resposta = {
            'sucesso': False,
            'mensagem': ''
        }

        first_name = self.request.POST.get("first-name")
        last_name = self.request.POST.get("last-name")
        email = self.request.POST.get("email")
        login = self.request.POST.get("login")
        senha = self.request.POST.get("senha")

        try:
            user = User.objects.create_user(login, email, senha)
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            login(self.request, user)
            return redirect(self.request.POST.get('next', '/index'))
        except IntegrityError:
            resposta['mensagem'] = 'Usuário já cadastrado'
        except Exception as erro:


            print '+'*10, erro, '+'*10

            resposta['mensagem'] = 'Cadastro não realizado'

        return render(self.request, 'autenticacao/login.html', resposta)


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
