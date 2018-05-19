#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


##错误定制

from flask import Flask,render_template,request
app = Flask(__name__)
app.debug=True



@app.route('/index',methods=['GET'])
def index():
    print("index 函数")
    return "index"


if __name__ == '__main__':
    app.run()

"""
##函数定制：

在后台中定义如下的函数，然后再模板文件中调用
@app.template_global()
def sb(a1, a2):
    return a1 + a2


@app.template_filter()
def db(a1, a2, a3):
    return a1 + a2 + a3


html调用方式：{{sb(1,2)}}  {{ 1|db(2,3)}} 备注：这个写法，1是第一个参数

"""

