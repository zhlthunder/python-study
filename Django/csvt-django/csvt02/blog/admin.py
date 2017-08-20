# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import *

admin.site.register(Employee)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(User)

# Register your models here.
