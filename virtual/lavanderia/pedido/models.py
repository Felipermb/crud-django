from __future__ import unicode_literals
from autenticacao.models import Cliente, Endereco, Cartao
from const import *
from datetime import datetime

from django.db import models

class Pedido(models.Model):

    data_pedido = models.DateField(auto_now=True)
    data_busca = models.DateField(default = datetime.now)
    data_entrega = models.DateField(null = True)
    valor_pedido = models.DecimalField(max_digits=8, decimal_places=2)
    endereco_busca = models.ForeignKey(Endereco,related_name="pedidos_busca")
    endereco_entrega = models.ForeignKey(Endereco,related_name="pedidos_entrega")
    pagamento = models.ForeignKey(Cartao, related_name="pedidos_pagamento")
    pecas_branca = models.BooleanField(default=False)


    def save(self, *args, **kwargs):

        self.valor_pedido = 123.45
        
        # if getattr(self, '_image_changed', True):
        #     small=rescale_image(self.image,width=100,height=100)
        #     self.image_small=SimpleUploadedFile(name,small_pic)
        super(Pedido, self).save(*args, **kwargs)


    def __str__(self):
    	return '{0} - R$ {1}'.format(self.endereco_entrega, self.valor_pedido)

class TipoRoupa(models.Model):
    tipo = models.IntegerField(choices=TIPOS_ROUPAS, default=DEFAULT_TIPO_ROUPAS)
    quantidade = models.IntegerField()
    pedido = models.ForeignKey(Pedido, related_name="tipos_roupas")

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.tipo, self.quantidade, self.pedido)
