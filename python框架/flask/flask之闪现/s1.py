#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask,flash,get_flashed_messages
app = Flask(__name__)
app.secret_key="asdfad"


@app.route('/get')
def get():
    #从某个地方获取设置过的所有值，并清除
    #闪现：就是读取一次后就被清除了，所以叫这个名字
    data=get_flashed_messages()
    print(data)
    return 'Hello World!--get'

@app.route('/set')
def set():
    #向某个地方设置一个值
    flash("asdfasdfafsd")
    return 'Hello World!--set'

if __name__ == '__main__':
    app.run()