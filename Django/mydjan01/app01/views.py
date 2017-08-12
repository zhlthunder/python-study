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
    tt=req.POST.get('inp1');
    aa=req.POST.get('inp2');
    ttime=req.POST.get('inp3');
    # print tt,aa,ttime;
    dic={'title':tt,'author':aa,'time':ttime};
    Book.objects.create(**dic);
    return HttpResponse("ok");