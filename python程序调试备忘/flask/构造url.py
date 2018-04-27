#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 构造URL
# 在Web程序中常常需要获取某个页面的URL，在Flask中需要使用url_for('方法名')来构造对应方法的URL。下面是Flask官方的例子。

from flask import Flask,url_for

app=Flask(__name__)

@app.route('/')
def index():pass

@app.route('/login')
def login():pass

@app.route('/user/<username>')
def profile(username):pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile',username='zhl'))

# 输出：
# /
# /login
# /login?next=%2F
# /user/zhl