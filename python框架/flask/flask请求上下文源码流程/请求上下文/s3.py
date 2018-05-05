#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##通过下面的方法来确认向stack中存入对象和获取对象的方法
##下面是通过手动的方法获取存入local中的对象的方法
from flask.globals import _request_ctx_stack


class Foo(object):
    def __init__(self):
        self.xxx=123

_request_ctx_stack.push(Foo())
print(_request_ctx_stack.top)
obj=_request_ctx_stack.top
print(obj.xxx)

# _request_ctx_stack.pop()
# print(_request_ctx_stack.top)
print("-------------------------------")

##下面利用flask源码中的偏函数的方法来获取对象

from flask.globals import _request_ctx_stack
from functools import partial

def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError("不存在")
    return getattr(top, name)

class Foo(object):
    def __init__(self):
        self.xxx=123

req=partial(_lookup_req_object,'xxx')

##1.这句可以类比为：请求刚进来时执行的操作
_request_ctx_stack.push(Foo())


##2.这些是使用的过程
v=req()
print(v)  ##通过这个方法也可以获取意义的值

#3.这句时请求结束之后移除的操作
_request_ctx_stack.pop()

