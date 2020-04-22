# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Topic(models.Model):
	"""docstring for Topic"""

	top_name = models.CharField(max_length=250)

	def __str__(self):
		return self.top_name

class Webpage(models.Model):
	"""docstring for Webpage"""

	topic = models.ForeignKey(Topic)
	name = models.CharField(max_length=250, unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	"""docstring for AccessRecord"""

	name = models.ForeignKey(Webpage)
	date = models.DateField()

	def __str__(self):
		return str(self.date)
		
		
		