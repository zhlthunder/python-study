#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# flask配置参数导入方法：
# 1.app.config['DEBUG'] = True
#2.app.debug=True
#3.app.config.from_pyfile("settings.py")   settings.py 中内容样式为“ DEBUG=True”
#以上三种方法都不常用
#4.在settings.py中定义类



from flask import Flask
app = Flask(__name__)
# app.config.from_pyfile("settings.py")
app.config.from_object("settings.DevelopmentConfig")

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
