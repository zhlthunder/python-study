#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl




from flask import Flask,render_template,request,redirect,session,url_for
app = Flask(__name__)
app.debug=True


@app.before_request
def process_request1(*args,**kwargs):
    print("process_request1进来了")

@app.before_request
def process_request2(*args,**kwargs):
    print("process_request2进来了")


@app.after_request
def process_response1(response):
    print("process_response1走了")
    return response

@app.after_request
def process_response2(response):
    print("process_response2走了")
    return response


@app.route('/index',methods=['GET'])
def index():
    print("index 函数")
    return "index"


if __name__ == '__main__':
    app.run()

#输出信息： （注意秩序顺序， request是顺序， reponse是倒序# ）
# process_request1进来了
# process_request2进来了
# index 函数
# process_response2走了
# process_response1走了