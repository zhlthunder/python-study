#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    return "hello world"

if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app=ProxyFix(app.wsgi_app)
    app.run()