#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from wsgiref.simple_server import make_server


def RunServer(environ, start_response):  #2.处理请求的部分
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'


if __name__ == '__main__':  #1.基于WSGI实现的socket的部分
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()

    # WGSI完成的工作：
    # 1.接收情况；
    # 2.预处理请求
    # Runserver(预处理的结果)