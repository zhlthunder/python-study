#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

class Md(object):
    def __init__(self,old_wsgi_ap):
        self.old_wsgi_ap=old_wsgi_ap

    def __call__(self, environ, start_response):
        print("开始执行")  ##实现中间件的功能代码
        ret=self.old_wsgi_ap(environ, start_response)
        print("开始之后") ##实现中间件的功能代码
        return ret

if __name__ == '__main__':
    app.wsgi_app=Md(app.wsgi_app)  ##相当于对响应率进行装饰
    app.run()