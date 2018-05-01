#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# class Foo(object):
#     def __setattr__(self, key, value):
#         print(key,value)
#
#     def __getattr__(self, item):
#         print(item)
# obj=Foo()
# obj.x=123  ##当执行这个方法时，会自动调用对象的__setattr__方法，key=x, value=123
# obj.x  #执行这个方法时，会自动调用__getattr__方法


##基于下面的这个方法，来对S3中的class的定义进行进一步的修改

class Foo(object):
    def __init__(self):
        # self.storage={}  ##会引发递归调用__setattr__而报错，所以采用下面的写法
        object.__setattr__(self, '__storage__', {})  ##完成和 self.storage={} 相同的功能

    def __setattr__(self, key, value):
        self.storage={'k1':'v1'}
        print(key,value)

    def __getattr__(self, item):
        print(item)
obj=Foo()
obj.x=123  ##当执行这个方法时，会自动调用对象的__setattr__方法，key=x, value=123
obj.x  #执行这个方法时，会自动调用__getattr__方法

"""
# 报错信息： RecursionError: maximum recursion depth exceeded  为递归错误
因为：__setattr__ 和__getattr_ 执行的条件是：   “对象.xxxx”_
而我们在构造函数中使用了self.storage={}， 这样就触发了__setattr__ 执行；
解决办法，换一种写法为：object.__setattr__(self, '__storage__', {})
"""
