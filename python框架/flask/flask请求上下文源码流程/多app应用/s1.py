#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from werkzeug.wsgi import  DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask,current_app

app1=Flask('app01')
app2=Flask('app02')



@app1.route('/index')
def index():
    print(current_app)
    return 'app01'

@app2.route('/index2')
def index2():
    print(current_app)
    return 'app02'

#www.baidu.com/index  app1
#www.baidu.com/sec/index  app2
dm=DispatcherMiddleware(app1,{
    '/sec':app2
})

if __name__ == '__main__':
    run_simple('localhost',5000,dm,)