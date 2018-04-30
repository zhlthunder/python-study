#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##需求： 当访问某个网站出错时，重定向到错误的页面显示错误的信息；

#方法1：在请求头中注明错误的信息，
##但这个过程中，是服务器端先将错误信息发送到客户端，然后客户端重新提交请求， 即这个包含错误信息的URL可以被客户端修改，那就有可能被恶意利用
# from flask import Flask,flash,get_flashed_messages,request,redirect
# app = Flask(__name__)
#
#
# @app.route('/index')
# def index():
#     #request.query_string 获取请求头中的信息
#     val=request.args.get('v')
#     print(val)
#     if val=='oldboy':
#         return 'Hello World!'
#     return redirect('/error?msg=aaasdfasdfsa')
#
# @app.route('/error')
# def error():
#     #显示错误信息
#     msg=request.args.get('msg')
#     return '错误信息：%s'%(msg,)
#
# if __name__ == '__main__':
#     app.run()
#

##方法2：采用闪现来实现，这样所有的数据都只存储在服务器端，安全可靠
from flask import Flask,flash,get_flashed_messages,request,redirect
app = Flask(__name__)
app.secret_key="asdfasfdaf"  #闪现如果不设置这个，运行时会出错，从这方面来判断，闪现也是使用session来实现的（重要）


@app.route('/index')
def index():
    #request.query_string 获取请求头中的信息
    val=request.args.get('v')
    print(val)
    if val=='oldboy':
        return 'Hello World!'
    flash("超时错误")
    return redirect('/error')

@app.route('/error')
def error():
    #显示错误信息
    data=get_flashed_messages()
    if data:
        msg=data[0]
    else:
        msg="..."
    return '错误信息：%s'%(msg,)

if __name__ == '__main__':
    app.run()

##总结：闪现的功能就是把一些临时的数据存放在服务器端，防止安全问题
"""
flash中存储的数据可以进行分类：
flash("超时错误"，cagtegory="xxx")
get_flashed_messages(cagtegory_filter=['xxx'])  这样取的时候只拿这一类的数据，其它的数据可以不动

闪现：就是用session实现的，即先把数据存放到session中，获取的时候采用pop的方法，这样数据清除了
另外，既然是基于session实现的，那就不用担心数据错乱的问题，
什么是数据错乱呢？ 即不用的客户端用户访问产生的错误信息，可以准确的按照用户别区分开来，为什么呢？
session本质上维护的就是一个用户列表，所以已经实现了对用户的隔离

闪现应用于：对临时数据操作，如：显示错误信息

"""
