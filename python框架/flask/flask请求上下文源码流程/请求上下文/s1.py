#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def hello():
    return "hello world!!"

if __name__ == '__main__':
    #查看flask源码涉及到以下几个部分
    import flask.globals  ## 查看全局变量相关的信息，重点看local对象和request对象的实例化；
    app.__call__  ##这里可以查看到： 请求到来之后，request信息的压栈，请求处理，请求结束后弹栈的过程
    app.request_class ##最终封装请求信息的请求类的部分
    app.open_session

    app.run()