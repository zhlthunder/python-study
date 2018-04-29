#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:


##按目前的思维，应该会采用下面的方法来实现这个需求 （即基于函数实现）
# from flask import Flask,request
# from utils import msg
#
# app = Flask(__name__)
# app.debug=True
#
#
# @app.route('/index')
# def index():
#     # data=request.query_string.get('val')
#     data='xyy'
#     if data=='xyy':
#         ##发送报警: 短信/邮件
#         msg.email("zhl")
#         msg.message("zhl")
#
#     return 'Hello World!'
#
# if __name__ == '__main__':
#     app.run()


##进阶的实现方法： 这样做的好处，代码之间没有耦合
from flask import Flask,request
from utils.message import send_msgs

app = Flask(__name__)
app.debug=True


@app.route('/index')
def index():
    # data=request.query_string.get('val')
    data='xyy'
    if data=='xyy':
        ##发送报警: 短信/邮件
        send_msgs("zhl")

    return 'Hello World!'

if __name__ == '__main__':
    app.run()