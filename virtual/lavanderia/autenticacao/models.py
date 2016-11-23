
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
		return 'CEP: {0} - NUM: {1}'.format(self.cep, self.numero)

class Cartao(models.Model):
	num = models.CharField(max_length=16)
	cod_seg = models.CharField(max_length=3)
	data_vencimento = models.CharField(max_length=7)
	nome = models.CharField(max_length=100)
	cliente = models.ForeignKey(Cliente, related_name="cartoes")

	def __str__(self):
		return 'NOME: {0} - CARTAO: {1}{2}{3}{4} .... {5}{6}{7}{8}'.format(self.nome, self.num[0], self.num[1], self.num[2], self.num[3], self.num[12], self.num[13], self.num[14], self.num[15] )
