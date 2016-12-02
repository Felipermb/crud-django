# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from autenticacao.models import *

class FormularioCartao(forms.ModelForm):
    class Meta:
        model = Cartao
        exclude = []

    def __init__(self, *args, **kwargs):

        super(FormularioCartao, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset =  Cliente.objects.filter(user__id = kwargs['initial']['user'])


        self.fields['nome'].widget.attrs['class'] = 'form-control has-feedback-left'
        self.fields['num'].widget.attrs['class'] = 'form-control has-feedback-left'
        self.fields['cod_seg'].widget.attrs['class'] = 'form-control has-feedback-left'
        self.fields['data_vencimento'].widget.attrs['class'] = 'form-control has-feedback-left'


class FormularioEndereco(forms.ModelForm):
    class Meta:
        model = Endereco
        exclude = []

    def __init__(self, *args, **kwargs):

        super(FormularioEndereco, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset =  Cliente.objects.filter(user__id = kwargs['initial']['user'])

        self.fields['numero'].widget.attrs['class'] = 'form-control has-feedback-left'
        self.fields['complemento'].widget.attrs['class'] = 'form-control has-feedback-left'
        self.fields['cep'].widget.attrs['class'] = 'form-control has-feedback-left'
