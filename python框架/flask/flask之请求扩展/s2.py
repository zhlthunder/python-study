#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl




from flask import Flask,render_template,request,redirect,session,url_for
app = Flask(__name__)
app.debug=True


@app.before_request
def process_request(*args,**kwargs):
    print("进来了")

# @app.after_request
# def process_response(*args,**kwargs): ##这个函数必须有返回值，否则会报错：“TypeError: 'NoneType' object is not callable”
#     # print(args,kwargs)  #从打印信息中看，其中包含response ,输出： (<Response 5 bytes [200 OK]>,) {}
#     pass


@app.after_request
def process_response(response):
    print("走了")
    return response


@app.route('/index',methods=['GET'])
def index():
    print("index 函数")
    return "index"


if __name__ == '__main__':
    app.run()

#输出信息：
# 进来了
# index 函数
# 走了