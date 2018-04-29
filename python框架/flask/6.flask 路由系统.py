#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask
app = Flask(__name__)

"""
step 1:先执行：app.route('/',methods=['GET','POST'],endpoint='n1')
 def route(self, rule, **options):
        #执行之后： rule='/'  options="methods=['GET','POST'],endpoint='n1')",即已经进行了闭包的操作，将这些值封装到下面的函数中了
        def decorator(f):
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator

step 2: 执行@decorator===decorator(index)

总结：添加路由关系的本质就是执行self.add_url_rule(rule, endpoint, f, **options) 这个方法；
"""

#添加路由关系方法1
@app.route('/index',methods=['GET','POST'],endpoint='n1')
def index():
    return 'Hello World!'


#添加路由关系方法2
#既然添加路由关系的本质就是执行self.add_url_rule(rule, endpoint, f, **options) 这个方法，我可以直接执行这个方法试试看
def login():
    return "login----test"
app.add_url_rule("/login",'n2',login,methods=['GET','POST'])
##经过测试，直接调用上面的方法时也可以完成路由关系的添加，即这种方式和django定义路由关系的方法类似了，即上面是添加路由关系的本质


if __name__ == '__main__':
    app.run()


#view_func.__name__  : 返回的就是函数的名称
#通过分析源码可知，如果endpoint参数不写，默认就是函数名