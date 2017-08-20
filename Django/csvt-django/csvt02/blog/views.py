# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.shortcuts import render

from blog.models import *


# Create your views here.

def index(req):
    emps=Employee.objects.all()
    return render_to_response('index.html',{'emps':emps})
