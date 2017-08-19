# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.shortcuts import render

# Create your views here.

class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def say(self):
        return "I'm "+self.name

def index(req):
    user={
        'name':'jack',
        'age':123,
        'sex':'male',
    }

    pp=Person('tom',23,'female')

    book_list=['python','java','php','web']

    # return HttpResponse("<h1>welcome to Django web</h>")
    # return render_to_response('index.html',{'title':'csvt','user':'jack'})
    return render_to_response('index.html',{'title':'csvt','user':user,'person':pp,'book_list':book_list})

def test(req,id):
    return render_to_response('index.html',{'id':id})

def ttt(req,parm):
    return render_to_response('index.html',{'id':parm})