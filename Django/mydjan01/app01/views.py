# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *

# from django.shortcuts import render
#
# # Create your views here.


# def index(req):
# 	return HttpResponse("Test---ok");

def index(req):
    return render_to_response('index.html')

def monitor(req):
    books=Book.objects.all();
    return render_to_response('asset.html',{'books':books});