#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask,request,render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app=Flask(__name__)
# manager=Manager(app)
bootsrap=Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/test')
def test():
    user_agent=request.headers.get('User-Agent')
    return "<h1>your browser is %s</h1>" % user_agent

@app.route('/user/<name>')
def user(name):
    return "<h1>hello %s</h1>"%name

if __name__ == '__main__':
    app.run()


