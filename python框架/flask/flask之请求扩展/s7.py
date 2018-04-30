#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##第一次请求前执行
##比如数据库的连接池创建或其他的初始的操作等等


from flask import Flask,render_template,request
app = Flask(__name__)
app.debug=True


@app.before_first_request
def first(*args,**kwargs): ##只在第一个请求到来前执行
    pass

@app.route('/index',methods=['GET'])
def index():
    print("index 函数")
    return "index"


if __name__ == '__main__':
    app.run()


