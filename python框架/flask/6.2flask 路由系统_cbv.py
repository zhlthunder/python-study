#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

"""
fbv和cbv对比：
https://www.cnblogs.com/joeyfang/archive/2017/01/16/6269342.html
Function Based View（FBV）和Class Based View （CBV）对比

fbv:
step1：根据访问请求，在urls寻找匹配的url映射，得到views.index

setp2：根据views.index ，调用views下index函数（传入参数request即用户请求信息）

step3：根据客户请求信息对数据进行处理，得到用户所需的数据output和context，通过HttpResponse返回将客户端

cbv:
其实CBV过程可以看成是FBV过程的抽象化、对象化。他需要最基本的三个类View，ContextMixin，TemplateResponseMixin

对应FBV的三个步骤：

step1. View类提供类方法as_view(),用于调用dipatch()，根据request类型分发给get，post...等对应方法处理。

step2. ContextMixin类，get_context_data(self, **kwargs)获取上下文数据，如果对数据库进行操作均可以继承该类，然后将增删改查的结果放入上下文数据中（即重写get_context_data）

step3. TemplateResponseMixin类，将内容渲染到指定模板上，通过render_to_response()方法实现对应功能

而其他模板视图基本就是在这三个类上进行继承重写后得到。




"""


from flask import Flask,views
app = Flask(__name__)


def auth(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner

##基于CBV的方式添加路由
class IndexView(views.MethodView):
    methods = ['GET']
    decorators = [auth, ]
    def get(self):
        return 'Index.GET'

    def post(self):
        return 'Index.POST'


app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))  # name=endpoint

"""
IndexView类的as_view方法中有如下的一段代码，会根据decorators列表中定义的装饰器函数对view函数进行多次装饰
        if cls.decorators:
            view.__name__ = name
            view.__module__ = cls.__module__
            for decorator in cls.decorators:
                view = decorator(view)
"""



if __name__ == '__main__':
    app.run()


#view_func.__name__  : 返回的就是函数的名称
#通过分析源码可知，如果endpoint参数不写，默认就是函数名