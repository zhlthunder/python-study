#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
# 组件安装： pip3 install Flask-Session
#安装redis : pip3 install redis


from flask import Flask,session
from flask_session import RedisSessionInterface


app=Flask(__name__)
app.secret_key='asdfad'


##第一种配置方式：
from redis import Redis  #这只是redis的模块，需要安装了redis server后才可以正常使用，所以此脚本无法执行
conn=Redis("连接redis server需要的配置参数")
# conn=Redis()
app.session_interface=RedisSessionInterface(conn,key_prefix='__',use_signer=False)
# #只要使用这就，就可以实现替换


#第二种配置方式（只是写法不同，调用方法完全相同）
# from redis import Redis
# from flask.ext.session import Session
# app.config['SESSION_TYPE'] = 'redis'
# app.config['SESSION_REDIS'] = Redis(host='192.168.0.94',port='6379')
# Session(app)




@app.route('/')
def index():
    session['xxx']=123

    return "index"

if __name__ == '__main__':
    app.run()

#说明，无论是自定义的session还是第三方的组件，都是通过为app.session_interface 重新定义一个对象；
#请求进来时：self.session_interface.open_session(self, request) 执行，获得session ，就是一个特殊的字典
#请求结束时， self.session_interface.save_session(self, app, session, response) 保存session