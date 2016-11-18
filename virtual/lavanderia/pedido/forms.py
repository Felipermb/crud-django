# -*- coding: utf-8 -*-

from django import forms
from pedido.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class FormularioPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ['valor_pedido', 'data_entrega']

    def __init__(self, *args, **kwargs):
        super(FormularioPedido, self).__init__(*args, **kwargs)
        self.fields['pagamento'].queryset = Cartao.objects.filter(cliente__user__id = kwargs['initial']['user'])
        self.fields['endereco_busca'].queryset = Endereco.objects.filter(cliente__user__id = kwargs['initial']['user'])
        self.fields['endereco_entrega'].queryset = Endereco.objects.filter(cliente__user__id = kwargs['initial']['user'])

        self.fields['pagamento'].widget.attrs['class'] = 'form-control'
        self.fields['nome_responsavel'].widget.attrs['class'] = 'form-control has-feedback-left'
        self.fields['nome_responsavel'].widget.attrs['value'] = User.objects.get(id = kwargs['initial']['user']).get_full_name()
        self.fields['nome_responsavel'].widget.attrs['placeholder'] = 'Responsavel pelo pedido'
