# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from autenticacao.models import Cliente, Endereco, Cartao
from const import *
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.db import models

class Pedido(models.Model):

    nome_responsavel = models.CharField(max_length=200)
    data_pedido = models.DateField(auto_now=True)
    data_busca = models.DateField(default = datetime.now)
    data_entrega = models.DateField(null = True)
    valor_pedido = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    endereco_busca = models.ForeignKey(Endereco,related_name="pedidos_busca")
    endereco_entrega = models.ForeignKey(Endereco,related_name="pedidos_entrega")
    pagamento = models.ForeignKey(Cartao ,related_name="pedidos_pagamento")
    pecas_branca = models.BooleanField(default=False)

    def __str__(self):
    	 return u'{0} - R$ {1}'.format(self.endereco_entrega, self.valor_pedido)
    	# return ''.format()

    def calcula_valor(self):
        valor = 0
        quantidade_roupas = 0
        # print "testeeeee " + str(self.tipos_roupas.count())
        for tipo in self.tipos_roupas.all():
            # print '----> ', tipo.tipo, tipo.get_tipo_display()
            if tipo.tipo == 1:
                valor += tipo.quantidade * 7
                quantidade_roupas += 1
                pass
            elif tipo.tipo == 2:
                valor += tipo.quantidade * 4
                quantidade_roupas += 1
                pass
            elif tipo.tipo == 3:
                valor += tipo.quantidade * 22
                quantidade_roupas += 1
                pass
            elif tipo.tipo == 4:
                valor += tipo.quantidade * 9
                quantidade_roupas += 1
                pass
            elif tipo.tipo == 5:
                valor += tipo.quantidade * 25
                quantidade_roupas += 1
                pass
            elif tipo.tipo == 6:
                valor += tipo.quantidade * 3
                quantidade_roupas += 1
                pass
            elif tipo.tipo == 7:
                valor += tipo.quantidade * 9
                quantidade_roupas += 1
                pass
            elif tipo.tipo == 8:
                valor += tipo.quantidade * 4
                quantidade_roupas += 1
                pass
            elif tipo.tipo == 9:
                valor += tipo.quantidade * 10
                quantidade_roupas += 1
                pass
            elif tipo.tipo == 10:
                valor += tipo.quantidade * 2
                quantidade_roupas += 1
                pass
            # else:
            #     # mais mais codigo
            #     pass

        if quantidade_roupas > 1 and self.pecas_branca == True:
            valor +=7

        valor += 5 #Valor do Frete (Chama o Leo) OBS: nao passar o CEP, pois ele tem que descobrir
        self.valor_pedido = valor
        self.save()


class TipoRoupa(models.Model):
    tipo = models.IntegerField(choices=TIPOS_ROUPAS, default=DEFAULT_TIPO_ROUPAS)
    quantidade = models.IntegerField()
    pedido = models.ForeignKey(Pedido, related_name="tipos_roupas")

    def __str__(self):
        # return '{0} - {1} {2}'.format(self.tipo, self.get_tipo_display(), self.pedido)
        return '{0} - {1}'.format(self.tipo, self.get_tipo_display())





# method for updating
@receiver(post_save, sender=TipoRoupa)
def atualiza_valor_pedido(sender, instance, **kwargs):
    instance.pedido.calcula_valor()
