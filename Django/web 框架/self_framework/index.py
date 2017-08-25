#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from wsgiref.simple_server import make_server
import time
from jinja2 import Template

# 下面的框架，方法所有的url都是返回相同的内容
# 第一步要实现，根据不同的url地址，返回不同的字符串
# 实现：1.获取url, 2.根据url的不同，做出不同的响应

 #方法 1.最基本的实现URL不同地址寻址的方法：
# def RunServer(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])  #此句不可以省，否则会报错
#     # print environ  #打印所有的请求的信息
#     request_url=environ['PATH_INFO']
#     # print request_url
#     if request_url=='/home/index':
#         return "home/index"
#     elif request_url=='/test/':
#         return "/testing/"
#     else:
#         return "404"

#方法2:通过列表的方式来存储url路径
def index():
    # return 'index'
    data=open('html/index.html').read()
    # return data
#此时我们返回的只是静态的页面，无法传入动态的数据，即此时就要在html中嵌套我们的值
# 比如现在我们自己定义一个替换的规则，比如我们在index.html中定义一个特殊的标签：@{alex}
    current_time=str(time.time())
    # new_str=data.replace('@{alex}',current_time)  #即通过使用简单的替换可以完成我们的需求
    # return new_str
# 但使用这种替换的方式有点太低端了，此时就引入了 jinjia2(它是一种模板语言)，它有定义的模板规则。

  # 总结：模板语句，就是用于把用户的数据渲染到模板字符串中的指定的位置，为得到一个新的字符串，
  #   所以jinja2的作用就是，把用户的数据和html中指定的位置进行结合渲染的功能，所有的模板语言都是通过这种方式来实现的。
    template = Template(data)
    result = template.render(name='Johnnnnn',age='12',current_time=current_time,
                             user_list=['jack','tony','alen'],
                             num=1,)
    return result.encode('utf-8')






def test():
    # return 'test'
    data=open('html/test.html').read()
    return data

url_list=[
    ('/index/',index),
    ('/test/',test),
]


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])  #此句不可以省，否则会报错
    # print environ  #打印所有的请求的信息
    request_url=environ['PATH_INFO']
    # print request_url
    for url in url_list:
        if request_url==url[0]:
            return url[1]()
    else:
        return "404"








if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()