#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl




#type1：定义函数传递到模板中执行，函数可以带参数
##重要：xss攻击相关：https://blog.csdn.net/u011300968/article/details/75352519


# from flask import Flask,render_template
# app = Flask(__name__)
#
#
# def func1(arg):
#     return arg+":阿斯顿发送到发送到"
#
# @app.route('/')
# def index():
#     return render_template("s7.html",ff=func1)
#
# if __name__ == '__main__':
#     app.run()


from flask import Flask,render_template,Markup
app = Flask(__name__)


def func1(arg):
    # return "<input type='text' value='%s' />"%(arg)
    return Markup("<input type='text' value='%s' />"%(arg))

@app.route('/')
def index():
    return render_template("s7.html",ff=func1)

if __name__ == '__main__':
    app.run()

"""
总结：flask 的jinjia2模板语言，支持在后端定义函数，传递到前端，然后在前端执行；
如果定义的函数中包含 html语句，就会存在xss攻击的风险， flask中规避的方法：
方法1：在前端使用 |safe (即管道符加safe)的方法，格式如下：
{{ff("六六")|safe}}

方法2：在后端使用Markup 对要传递的字符串进行格式化，范例如下：
Markup("<input type='text' value='%s' />"%(arg))

备注：不采取上面的措施时，前端看到的信息如下；
 <input type='text' value='六六' />

"""

# type2: 宏定义
"""
可以通过宏定义，在前端页面中定义一个程序块，格式举例如下，这样就可以在前端生成4个input框

 {% macro xx(name, type='text', value='') %}
        <input type="{{ type }}" name="{{ name }}1" value="{{ value }}">
        <input type="{{ type }}" name="{{ name }}2" value="{{ value }}">
        <input type="{{ type }}" name="{{ name }}3" value="{{ value }}">
        <input type="{{ type }}" name="{{ name }}4" value="{{ value }}">
  {% endmacro %}

 {{xx('n')}}
"""