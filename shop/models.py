from __future__ import unicode_literals
from django.db import models

class Product(models.Model):
	nombre = models.CharField(max_length=140)
	description = models.CharField(max_length=140, null=True,blank=True)
	price = models.FloatField()
	def __str__(self):
		return self.nombre
	
