#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask,request
from flask.ext.script import Manager

app=Flask(__name__)
manager=Manager(app)

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

if __name__ == '__main__':
    manager.run()


'''
C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python框架\flask_2\flasky>python3 ss2.py
ss2.py:6: ExtDeprecationWarning: Importing flask.ext.script is deprecated, use flask_script instead.
  from flask.ext.script import Manager
usage: ss2.py [-?] {shell,runserver} ...

positional arguments:
  {shell,runserver}
    shell            Runs a Python shell inside Flask application context.  在flask应用上下中运行python shell
    runserver        Runs the Flask development server i.e. app.run()  运行python开发服务器，app.run()

optional arguments:
  -?, --help         show this help message and exit
'''