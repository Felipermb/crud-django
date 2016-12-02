# -*- coding: utf-8 -*-

from django import forms
from pedido.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from const import *

# from django.forms.extras.widgets import SelectDateWidget

class FormularioPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ['data_entrega', 'data_pedido']
        # date_field = forms.DateField(widget=SelectDateWidget)

    def __init__(self, *args, **kwargs):
        super(FormularioPedido, self).__init__(*args, **kwargs)
        self.fields['pagamento'].queryset = Cartao.objects.filter(cliente__user__id = kwargs['initial']['user'])
        self.fields['endereco_busca'].queryset = Endereco.objects.filter(cliente__user__id = kwargs['initial']['user'])
        self.fields['endereco_entrega'].queryset = Endereco.objects.filter(cliente__user__id = kwargs['initial']['user'])

        self.fields['usuario'].queryset = Cliente.objects.filter(user__id = kwargs['initial']['user'])


        self.fields['pagamento'].widget.attrs['class'] = 'form-control'

        self.fields['valor_pedido'].widget.attrs['class'] = 'form-control'

        self.fields['nome_responsavel'].widget.attrs['class'] = 'form-control has-feedback-left'
        self.fields['nome_responsavel'].widget.attrs['value'] = User.objects.get(id = kwargs['initial']['user']).get_full_name()
        self.fields['nome_responsavel'].widget.attrs['placeholder'] = 'Responsavel pelo pedido'


        self.fields['data_busca'].widget.attrs['class'] = 'form-control has-feedback-left '
        self.fields['data_busca'].widget.attrs['type'] = 'date'


        self.fields['endereco_busca'].widget.attrs['class'] = 'form-control has-feedback-left '
        self.fields['endereco_entrega'].widget.attrs['class'] = 'form-control has-feedback-left '
        self.fields['pagamento'].widget.attrs['class'] = 'form-control has-feedback-left '

        self.fields['quantidadeCamisa'].widget.attrs['min'] = 0
        self.fields['quantidadeCamisa'].widget.attrs['class'] = 'form-control'
        self.fields['camisa'].widget.attrs['class'] = 'icheckbox_flat-green checked'

        self.fields['quantidadeCamiseta'].widget.attrs['min'] = 0
        self.fields['quantidadeCamiseta'].widget.attrs['class'] = 'form-control'
        self.fields['camiseta'].widget.attrs['class'] = 'icheckbox_flat-green checked'

        self.fields['quantidadeEdredom'].widget.attrs['min'] = 0
        self.fields['quantidadeEdredom'].widget.attrs['class'] = 'form-control'
        self.fields['edredom'].widget.attrs['class'] = 'icheckbox_flat-green checked'

        self.fields['quantidadeLencol'].widget.attrs['min'] = 0
        self.fields['quantidadeLencol'].widget.attrs['class'] = 'form-control'
        self.fields['lencol'].widget.attrs['class'] = 'icheckbox_flat-green checked'

        self.fields['quantidadeRLuxo'].widget.attrs['min'] = 0
        self.fields['quantidadeRLuxo'].widget.attrs['class'] = 'form-control'
        self.fields['rLuxo'].widget.attrs['class'] = 'icheckbox_flat-green checked'

        self.fields['quantidadeRIntima'].widget.attrs['min'] = 0
        self.fields['quantidadeRIntima'].widget.attrs['class'] = 'form-control'
        self.fields['rIntima'].widget.attrs['class'] = 'icheckbox_flat-green checked'

        self.fields['quantidadeRJeans'].widget.attrs['min'] = 0
        self.fields['quantidadeRJeans'].widget.attrs['class'] = 'form-control'
        self.fields['rJeans'].widget.attrs['class'] = 'icheckbox_flat-green checked'

        self.fields['quantidadeTBanho'].widget.attrs['min'] = 0
        self.fields['quantidadeTBanho'].widget.attrs['class'] = 'form-control'
        self.fields['tBanho'].widget.attrs['class'] = 'icheckbox_flat-green checked'

        self.fields['quantidadeTMesa'].widget.attrs['min'] = 0
        self.fields['quantidadeTMesa'].widget.attrs['class'] = 'form-control'
        self.fields['tMesa'].widget.attrs['class'] = 'icheckbox_flat-green checked'

        self.fields['quantidadeTRosto'].widget.attrs['min'] = 0
        self.fields['quantidadeTRosto'].widget.attrs['class'] = 'form-control'
        self.fields['tRosto'].widget.attrs['class'] = 'icheckbox_flat-green checked'



        self.fields['pecas_branca'].widget.attrs['class'] = 'icheckbox_flat-green checked'
# class FormularioTipoRoupa(forms.ModelForm):

#     class Meta:
#         model = TipoRoupa
#         exclude = ['pedido']


#     def __init__(self, *args, **kwargs):
#         super(FormularioTipoRoupa, self).__init__(*args, **kwargs)
#         self.fields['tipo'].queryset = Pedido.objects.filter()


#         self.fields['quantidade'].widget.attrs['min'] = 0
#         self.fields['quantidade'].widget.attrs['value'] = 0
#         self.fields['quantidade'].widget.attrs['class'] = 'form-control'


#         # self.fields['pecas_branca'].widget.attrs['class'] = 'form-control'

#         self.fields['tipo'].widget.attrs['class'] = 'form-control'
#         # self.fields['tipo'].
#         # self.fields['']
