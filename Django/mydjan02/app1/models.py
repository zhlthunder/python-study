# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class IP(models.Model):
    hostname=models.CharField(max_length=50,unique=True)
    ip=models. GenericIPAddressField(unique=True)
    port=models.IntegerField(default='22')
    os=models.CharField(max_length=20,default='linux',verbose_name='Operating System')

    # 一个类代表一个数据表，类名称就是表的名称；
    # 类的成员变量代表的就是列的名称
class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=60)
    state_province=models.CharField(max_length=30)
    country=models.CharField(max_length=50)
    website=models.URLField()

    def __unicode__(self): # used to display name infor at admin web
        return self.name

class Author(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()

    def __unicode__(self): # used to display name infor at admin web
        return self.first_name

class Book(models.Model):
    title=models.CharField(max_length=100)
    authors=models.ManyToManyField(Author)
    publisher=models.ForeignKey(Publisher)
    publication_date=models.DateField()

    def __unicode__(self): # used to display name infor at admin web
        return self.title

# 备注：
# ManyToManyField 表示多对多的关系；
# ForeignKey   表示多对一的关系；叫外键，表示链接到另外一个表
# 因为数据表默认由很多的元素，所有肯定是多对**，所以没有一对多的说法，只有
# 多对多： 一个书可以有多个作者，一个作者也可以有多本书；
# 多对一： 多本书都是在一个出版社出的；

# 注意，生成的表中， 多对多的关系，会自动生成一个 book_author的表
