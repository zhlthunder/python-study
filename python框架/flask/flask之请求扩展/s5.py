#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


##错误定制：根据状态码定制错误页面

from flask import Flask,render_template,request
app = Flask(__name__)
app.debug=True

@app.errorhandler(404)
def err_404(arg):
    return "404错误了"


@app.route('/index',methods=['GET'])
def index():
    print("index 函数")
    return "index"


if __name__ == '__main__':
    app.run()

