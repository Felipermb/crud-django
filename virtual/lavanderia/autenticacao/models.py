from __future__ import unicode_literals

from django.db import models

class Autenticacao(models.Model):
	login = models.CharField(max_length=200)
	senha = models.CharField(max_length=200)
	email = models.CharField(max_length=200)

	def __str__(self):
		return '{0} {1} {2}'.format(self.login, self.senha, self.email)