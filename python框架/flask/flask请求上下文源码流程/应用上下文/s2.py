#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##需求：是要把before函数中的某个参数传递到视图函数中，
# 可以借助session或request来实现传递
#这种方式可以实现传递，但因为request中本身有很多的属性，这种方式就有可能导致某些属性被重写，导致request收到影响
##这种情况下，推荐大家使用 g

from flask import Flask,request
app = Flask(__name__)

@app.before_request
def before():
    a=123
    request.a=123
    pass

@app.route('/')
def index():
    print(request.a)
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

##改进：下面通过g来实现函数之间的参数传递
##可以把g想象成一个空字典，这个列表中元素的生命周期就是  一次请求的周期。

from flask import Flask,request,g
app = Flask(__name__)

@app.before_request
def before():
    a=123
    g.a=123
    pass

@app.route('/')
def index():
    print(g.a)
    return 'Hello World!'

if __name__ == '__main__':
    app.run()