#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 路由
# 在上面的例子里可以看到路由的使用。如果了解Spring Web MVC的话，应该对路由很熟悉。路由通过使用Flask的app.route装饰器来设置，这类似Java的注解。

from flask import Flask

app = Flask(__name__)
app.config.update(DEBUG=True)  # 参数形式配置

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)

##测试方法，通过浏览器访问：localhost:8088
##支持两个url: http://localhost:8088/hello ,  http://localhost:8088