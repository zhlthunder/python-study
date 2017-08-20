# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse

from blog.models import *

##related with form
from django import forms


# Create your views here.

def index(req):
    emps=Employee.objects.all()
    return render_to_response('index.html',{'emps':emps})


def show_author(req):
    authors=Author.objects.all()
    return render_to_response('show_author.html',{'authors':authors})

def show_book(req):
    books=Book.objects.all()
    return render_to_response('show_book.html',{'books':books})

#create form class
class UserForm(forms.Form):
    name=forms.CharField()

def register(req):
    if req.method=='POST':
        form=UserForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("ok")
    else:
        form=UserForm()
        return render_to_response('register.html',{'form':form})


class PersonForm(forms.Form):
    username=forms.CharField()
    headImg=forms.FileField()

def regis(req):
    if req.method=='POST':
        uf=PersonForm(req.POST,req.FILES)
        if uf.is_valid():
            print(uf.cleaned_data['username'])
            print(uf.cleaned_data['headImg'].name)
            print(uf.cleaned_data['headImg'].size)
            fp=file(uf.cleaned_data['headImg'].name,'wb')
            data=uf.cleaned_data['headImg'].read()
            fp.write(data)
            fp.close()

            return HttpResponse("ok")
    else:
        uf=PersonForm()
    return render_to_response('regis.html',{'uf':uf})