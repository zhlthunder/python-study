# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from models import *

# from django.shortcuts import render
#
# # Create your views here.


# def index(req):
# 	return HttpResponse("Test---ok");

def index(req):
    return render_to_response('index.html')

def asset(req):
    books=Book.objects.all();
    return render_to_response('asset.html',{'books':books});

def upload(req):
    print req.POST;
    aauthor=req.POST.get('author');
    ttime=req.POST.get('time',);
    ttile=req.POST.get('title',);
    print aauthor,ttime,ttile
    Book.objects.create(author=aauthor,time=ttime,title=ttile)  ##write to database

    return HttpResponse("ok");  ##"ok "  will be return to ajax "arg"