# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.admin import UserAdmin  #used for user defined admin function extension
from django.contrib import admin
from models import *


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title',) ##define search box for Book table
    list_filter = ('title','publication_date',) ##define filter box for Book table
    date_hierarchy = 'publication_date'  ##sorted by time


#after register, user table can be seen at admin web site;
admin.site.register(IP)
admin.site.register(Book,BookAdmin)  #register book and bookadmin
admin.site.register(Publisher)
admin.site.register(Author)



# Register your models here.
