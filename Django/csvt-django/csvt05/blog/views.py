# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms

# Create your views here.

class UserForm(forms.Form):
    username=forms.CharField()

def login(req):
    if req.method=='POST':
        uf=UserForm(req.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            req.session['username']=username
            return HttpResponseRedirect('/index/')
    else:
        uf=UserForm()
    return render_to_response('login.html',{'uf':uf})

def index(req):
    username=req.session.get('username','anybody')
    return  render_to_response('index.html',{'username':username})

def logout(req):
    del req.session['username']
    return HttpResponse("logout successfully")