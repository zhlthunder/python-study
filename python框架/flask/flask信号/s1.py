#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##此代码未执行

from flask import Flask,signals,render_template
app = Flask(__name__)

def func(*args,**kwargs):
    print("触发信号")

signals.request_started.connect(func)  #将自定义函数注册到信号中

##触发信号调用的是send方法： signals.request_started.send()

@app.before_first_request  ##这是之前的讲的flask请求扩展的部分
def before_first(*args,**kwargs):
    pass

@app.before_request
def before_request(*args,**kwargs):
    pass

@app.route('/')
def index():
    print("视图")
    return render_template('index.html')

if __name__ == '__main__':
    app.wsgi_app
    app.run()