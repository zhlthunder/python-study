#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from wsgiref.simple_server import make_server
import time
from jinja2 import Template
from url import url_list




def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/Views')])  #此句不可以省，否则会报错
    # print environ  #打印所有的请求的信息
    request_url=environ['PATH_INFO']
    # print request_url
    for url in url_list:
        if request_url==url[0]:
            return url[1]()
    else:
        return "404"


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()