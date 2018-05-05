#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask,request,session,g,current_app
app=Flask(__name__) #说明：这是在为app取一个名字，可以是任意的字符串，比如Flask("tests"),只不过这里用的__name__就是用的是文件的名字来命名app

@app.route('/index')
def index():
    print(request)  ##request 是LocalProxy 的对象，会执行LocalProxy 的__str__方法  --》调用 localproxy的_get_current_object方法--》执行偏函数
      #--》偏函数执行完成后，返回 ctx.request
    print(request.method)
         # 会执行LocalProxy 的__getattr__方法 ，其中执行 return getattr(self._get_current_object(), name)--》所以会先执行偏函数，返回 ctx.request后
         #再执行getattr,最终返回： ctx.request.method
    print(session)
                   ##session 是LocalProxy 的对象，会执行LocalProxy 的__str__方法  --》调用 localproxy的_get_current_object方法--》执行偏函数
      #--》偏函数执行完成后，返回 ctx.session

    print(g)  ##执行g对象的__str__方法，就是调用LocalProxy(partial(_lookup_app_object, 'g'))， 执行方法和上面的request相关
    print(current_app)  #使用方法和g相关

    return "aaaaa"

if __name__ == '__main__':
    #1.app.__call__
    #2.app.wsgi_app
    app.wsgi_app
    app.request_class
    app.run()