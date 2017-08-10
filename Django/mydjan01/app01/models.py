# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 50)
    author = models.CharField(max_length= 20)
    time = models.IntegerField(default = 0)

class Publisher(models.Model):
    name = models.CharField(max_length= 20)
    address = models.CharField(max_length= 20)
