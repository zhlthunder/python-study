#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


from flask import Flask,views
app = Flask(__name__)

"""
参数介绍：
defaults=None,              默认值,当URL中无参数，函数需要参数时，使用defaults={'k':'v'}为函数提供参数
endpoint=None,              名称，用于反向生成URL，即： url_for('名称')
methods=None,               允许的请求方式，如：["GET","POST"]


strict_slashes=None,        对URL最后的 / 符号是否严格要求，
                           如：
                           @app.route('/index',strict_slashes=False)，
                           访问 http://www.xx.com/index/ 或 http://www.xx.com/index均可
                           @app.route('/index',strict_slashes=True)
                           仅访问 http://www.xx.com/index

redirect_to=None,           重定向到指定地址
                            如：
                            @app.route('/index/<int:nid>', redirect_to='/home/<nid>')
                             或
                             def func(adapter, nid):
                             return "/home/888"
                               @app.route('/index/<int:nid>', redirect_to=func)





"""


#defaults= 参数举例
# @app.route('/index',methods=['GET','POST'],endpoint='n1',defaults={'nid':88})
# def index(nid):
#     print(nid)
#     return 'Hello World!'


##redirect_to= 参数举例
@app.route('/index',methods=['GET','POST'],endpoint='n1',redirect_to='/index2')
def index():
    return '公司老页面'

@app.route('/index2',methods=['GET','POST'],endpoint='n2')
def index2():
    return '公司新页面'


if __name__ == '__main__':
    app.run()


#view_func.__name__  : 返回的就是函数的名称
#通过分析源码可知，如果endpoint参数不写，默认就是函数名