# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=20,default=None)

    def __unicode__(self):
        return self.name

#retated define many to one
class Entry(models.Model):
    name=models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    name=models.CharField(max_length=30)
    entry=models.ForeignKey(Entry)

    def __unicode__(self):
        return self.name



#related define many to many
class Author(models.Model):
    name=models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    name=models.CharField(max_length=30)
    authors=models.ManyToManyField(Author)

    def __unicode__(self):
        return self.name


##related with file upload
class User(models.Model):
    username=models.CharField(max_length=40)
    headImg=models.FileField(upload_to='./upload/')

    def __unicode__(self):
        return self.username
