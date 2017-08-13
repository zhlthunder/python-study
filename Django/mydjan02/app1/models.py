# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class IP(models.Model):
    hostname=models.CharField(max_length=50,unique=True)
    ip=models. GenericIPAddressField(unique=True)
    port=models.IntegerField(default='22')
    os=models.CharField(max_length=20,default='linux',verbose_name='Operating System')

class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    time=models.CharField(max_length=20)

class Publisher(models.Model):
    title=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
