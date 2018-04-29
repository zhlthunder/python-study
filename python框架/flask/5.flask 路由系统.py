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
"""

@app.route('/',methods=['GET','POST'],endpoint='n1')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
