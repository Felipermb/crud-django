# -*- coding: utf-8 -*-

from django import forms
from pedido.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from django.forms.extras.widgets import SelectDateWidget

class FormularioPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ['valor_pedido', 'data_entrega']
        # date_field = forms.DateField(widget=SelectDateWidget)

    def __init__(self, *args, **kwargs):
        super(FormularioPedido, self).__init__(*args, **kwargs)
        self.fields['pagamento'].queryset = Cartao.objects.filter(cliente__user__id = kwargs['initial']['user'])
        self.fields['endereco_busca'].queryset = Endereco.objects.filter(cliente__user__id = kwargs['initial']['user'])
        self.fields['endereco_entrega'].queryset = Endereco.objects.filter(cliente__user__id = kwargs['initial']['user'])

        self.fields['pagamento'].widget.attrs['class'] = 'form-control'

        self.fields['nome_responsavel'].widget.attrs['class'] = 'form-control has-feedback-left'
        self.fields['nome_responsavel'].widget.attrs['value'] = User.objects.get(id = kwargs['initial']['user']).get_full_name()
        self.fields['nome_responsavel'].widget.attrs['placeholder'] = 'Responsavel pelo pedido'


        self.fields['data_busca'].widget.attrs['class'] = 'form-control has-feedback-left '
        self.fields['data_busca'].widget.attrs['type'] = "date"

        self.fields['endereco_busca'].widget.attrs['class'] = 'form-control has-feedback-left '
        self.fields['endereco_entrega'].widget.attrs['class'] = 'form-control has-feedback-left '
        self.fields['pagamento'].widget.attrs['class'] = 'form-control has-feedback-left '


class FormularioTipoRoupa(forms.ModelForm):

    class Meta:
        model = TipoRoupa
        exclude = ['pedido']

    def __init__(self, *args, **kwargs):
        super(FormularioTipoRoupa, self).__init__(*args, **kwargs)
        self.fields['quantidade'].widget.attrs['min'] = 0
        self.fields['quantidade'].widget.attrs['value'] = 0
        self.fields['quantidade'].widget.attrs['class'] = 'form-control'

        self.fields['tipo'].widget.attrs['class'] = 'form-control'
        # self.fields['']
