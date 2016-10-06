from __future__ import unicode_literals
from django.db import models

class Usuarios(models.Model):
	
	login = models.CharField(max_length=100)
	senha = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	def __str__(self):
 		return '{0} {1} {2}'.format(self.login, self.senha, self.email)