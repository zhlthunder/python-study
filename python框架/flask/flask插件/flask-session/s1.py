#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask,session

app=Flask(__name__)
app.secret_key='asdfad'

@app.route('/')
def index():
    ##执行session对象的__setitem__方法
    session['xxx']=123
    #这句完成的操作： 在local的ctx中找到session（初始状态为一个空字典），并在空字典中写值

    return "index"

if __name__ == '__main__':
    # app.__call__
    app.wsgi_app
    app.open_session
    app.run()