#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##参考： http://www.pythondoc.com/flask-restful/second.html

from flask import Flask
app=Flask(__name__)

@app.route('/index')
def index():
    return "你好，我是web主页面"

if __name__ == '__main__':
    app.run(debug=True)