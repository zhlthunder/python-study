#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##flask快速入门：
##参考博客：http://www.cnblogs.com/wupeiqi/articles/7552008.html
#http://www.pythonav.com/all/1.html
#安装
# pip3 install flask

#类似wsgi的模块: flask中使用的wsgi为 werkzeug
#说明：web框架中的WSGI，本质上就是完成socket的创建用的。

# 使用 werkzeug实现的一个简单server(也就是socket服务器端);

# from werkzeug.wrappers import Request, Response
#
# @Request.application
# def hello(request):
#     return Response('Hello World!')
#
# if __name__ == '__main__':
#     from werkzeug.serving import run_simple
#     run_simple('localhost', 4000, hello)


##使用wsgiref实现的一个简单server(也就是socket服务器端);

# from wsgiref.simple_server import make_server
#
#
# def RunServer(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]
#
#
# if __name__ == '__main__':
#     httpd = make_server('', 8000, RunServer)
#     print("Serving HTTP on port 8000...")
#     httpd.serve_forever()

##最最本地的，就是通过socket来实现的，上面的都是基于socket的封装，完全基于socket实现如下：
# 众所周知，对于所有的Web应用，本质上其实就是一个socket服务端，用户的浏览器其实就是一个socket客户端

##需要在python2下运行
# import socket
#
# def handle_request(client):
#     buf = client.recv(1024)
#     client.send("HTTP/1.1 200 OK\r\n\r\n")
#     client.send("Hello, Seven")
#
# def main():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind(('localhost',8000))
#     sock.listen(5)
#
#     while True:
#         connection, address = sock.accept()
#         handle_request(connection)
#         connection.close()
#
# if __name__ == '__main__':
#     main()

##说明：
# 目前学习的flask和django都是在wsgi的基础上来实现的。
# 大概流程就是：客户端请求来了之后，从request中提取url匹配对应的视图函数，视图函数执行完之后获取返回值，将返回值和模板一起返回给用户

##flask基本使用：
from flask import Flask
##实例化flask对象
app = Flask(__name__)

#将url(/)和hellow_world的对应关系添加到路由中
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    #监听用户请求
    #如果有用户请求到来，则执行app的__cal__方法
    ##__cal__方法其实是整个请求的入口，在这个方法中把请求的数据进行封装，把请求中URL拿来进行路由映射，并执行视图函数，获取视图函数的返回值后给客户
        # app.__call__()
    app.run()


##对象后面加（），执行对象的__cal__方法
#源码解析：
#点击run进入app.py中，可以看到def run(self, host=None, port=None, debug=None, **options)，这个函数中
#主要就是调用我们上面的 run_simple(host, port, self, **options) 函数，参考我们上面的例子，请求到来的时候
#执行的是self(),即是对象后面加（），执行对象的__cal__方法
#紧接着，我们引用app.__call__()，点击.__call__，打开查看这个方法的源码；
 # def __call__(self, environ, start_response):
 #        """Shortcut for :attr:`wsgi_app`."""
 #        return self.wsgi_app(environ, start_response)
 # 再打开wsgi_app的源码，即下面就是web请求的入口

        # ctx = self.request_context(environ)
        # ctx.push()
        # error = None
        # try:
        #     try:
        #         response = self.full_dispatch_request()
        #     except Exception as e:
        #         error = e
        #         response = self.handle_exception(e)
        #     except:
        #         error = sys.exc_info()[1]
        #         raise
        #     return response(environ, start_response)
        # finally:
        #     if self.should_ignore_error(error):
        #         error = None
        #     ctx.auto_pop(error)