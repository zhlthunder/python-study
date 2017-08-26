#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from wsgiref.simple_server import make_server
import time
from jinja2 import Template


def index():
    # return 'index'
    data=open('Views/index.html').read()
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
    data=open('Views/test.html').read()
    return data
