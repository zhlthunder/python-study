# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.admin import UserAdmin  #used for user defined admin function extension
from django.contrib import admin
from models import *


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title',) ##define search box for Book table
    list_filter = ('title','publication_date',) ##define filter box for Book table
    date_hierarchy = 'publication_date'  ##collection with **
    # ordering = ('publication_date',)  ##sorted by **  small to big
    ordering = ('-publication_date',)  ##sorted by **  big to small
    list_display = ('title','publication_date') ## choose the column to been display at admin table

#if you want to know more application ,just double click on modeladmin,you will find all related method 


#after register, user table can be seen at admin web site;
admin.site.register(IP)
admin.site.register(Book,BookAdmin)  #register book and bookadmin
admin.site.register(Publisher)
admin.site.register(Author)



# Register your models here.
