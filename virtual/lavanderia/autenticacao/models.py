
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class Cliente(models.Model):
	nome = models.CharField(max_length=200)
	telefone = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	user = models.ForeignKey(User)

	def __str__(self):
		return '{0} - {1} - {2}'.format(self.nome, self.telefone, self.email)

class Endereco(models.Model):
	cep = models.CharField(max_length=8)
	complemento = models.CharField(max_length=100)
	numero = models.CharField(max_length=5)
	cliente = models.ForeignKey(Cliente, related_name="enderecos")

	def __str__(self):
		return '{0}'.format(self.cep)

class Cartao(models.Model):
	num = models.CharField(max_length=16)
	cod_seg = models.CharField(max_length=3)
	data_vencimento = models.CharField(max_length=7)
	nome = models.CharField(max_length=100)
	cliente = models.ForeignKey(Cliente, related_name="cartoes")

	def __str__(self):
		return '{0} - {1}'.format(self.nome, self.num)
