#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import  flask.globals
from flask import Flask

app=Flask(__name__)
app.__call__

"""
打开globals，
先看下面这个：
_request_ctx_stack = LocalStack()

点开 LocalStack
可以看到下面的部分，调用了一个Local ，这个local和我们自己实现的local类相同。
    def __init__(self):
        self._local = Local()

即这部分完成的就是threading  local局部变量的功能；

可以想象一下，我们在前面使用时，直接导入request后，就可以从request中获取用户请求的所有信息。
为什么可以获取到客户端的请求信息呢？ 那可能是因为 请求过来之后就被存放到local中了

它是怎么存储的呢？ 说明如下：
请求来了之后，入口是： app.__call__
点击__call__后，
    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)
再进入wsgi_app，重点看下面这部分：
        ctx = self.request_context(environ) ##environ 包含请求相关的所有信息   #将请求相关的数据environ封装到了request_context对象中
        ctx.push()
          #push中的这句：  _request_ctx_stack.push(self)   ， 将封装了请求相关数据的对象添加到了某地

再点击_request_ctx_stack ，转到如下处：
_request_ctx_stack = LocalStack()
==》即此处完成了将request相关的数据存放到了local中

"""