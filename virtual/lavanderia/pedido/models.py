# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from autenticacao.models import Cliente, Endereco, Cartao
from const import *
from datetime import datetime ,timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver



from django.db import models

class Pedido(models.Model):

    nome_responsavel = models.CharField(max_length=200)
    data_pedido = models.DateField(auto_now=True)
    data_busca = models.DateField(default = datetime.now)
    data_entrega = models.DateField(default = datetime.now()+ timedelta(days=2) )
    valor_pedido = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    endereco_busca = models.ForeignKey(Endereco,related_name="pedidos_busca")
    endereco_entrega = models.ForeignKey(Endereco,related_name="pedidos_entrega")
    pagamento = models.ForeignKey(Cartao ,related_name="pedidos_pagamento")
    usuario = models.ForeignKey(Cliente, related_name="usuario_pedido", default='User.id')

    camisa = models.BooleanField(default=True)
    quantidadeCamisa = models.IntegerField(default=0)

    camiseta = models.BooleanField()
    quantidadeCamiseta = models.IntegerField(default=0)

    edredom = models.BooleanField()
    quantidadeEdredom = models.IntegerField(default=0)

    lencol = models.BooleanField()
    quantidadeLencol = models.IntegerField(default=0)

    rLuxo = models.BooleanField()
    quantidadeRLuxo = models.IntegerField(default=0)

    rIntima = models.BooleanField()
    quantidadeRIntima = models.IntegerField(default=0)

    rJeans = models.BooleanField()
    quantidadeRJeans = models.IntegerField(default=0)

    tBanho = models.BooleanField()
    quantidadeTBanho = models.IntegerField(default=0)

    tMesa = models.BooleanField()
    quantidadeTMesa = models.IntegerField(default=0)

    tRosto = models.BooleanField()
    quantidadeTRosto = models.IntegerField(default=0)

    pecas_branca = models.BooleanField(default=False)

    def __str__(self):
    	 return '{0} - R$ {1}'.format(self.endereco_entrega, self.valor_pedido)
