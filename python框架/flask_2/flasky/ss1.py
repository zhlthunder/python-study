#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask,request,make_response
app=Flask(__name__)
app.secret_key='123445'

@app.route('/')
def index():
    return "<h1>hello world</h1>"

@app.route('/test')
def test():
    user_agent=request.headers.get('User-Agent')
    return "<h1>your browser is %s</h1>" % user_agent

@app.route('/user/<name>')
def user(name):
    return "<h1>hello %s</h1>"%name

@app.route('/order')
def order():
    response=make_response('order')
    response.set_cookie('zhl','123')  ##此处如果写成 123就会报错
    return response

if __name__ == '__main__':
    app.run(debug=True)
