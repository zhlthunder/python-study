#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__,template_folder='templates',static_folder='statics',static_url_path='/static')
app.debug=True

from .views.account import account
from .views.blog import blog
from .views.user import user

app.register_blueprint(account)  #将蓝图注册到app
app.register_blueprint(blog)   #将蓝图注册到app
app.register_blueprint(user)   #将蓝图注册到app


##在这里可以实现之前讲的flask扩展相关的功能，即在所有请求执行之前执行下面的函数；
# @app.before_request
# def process_request(*args,**kwargs):
#     print("来了")

##请求到来的时候，由app将请求分发到各个蓝图中
##蓝图提供了一种方法来组织程序的目录结构