#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

class Foo(object):
    def __add__(self, other):
        return 123

obj1=Foo()
#当执行：
obj1+2  #就会自动执行obj1的__add__方法，就和 ‘对象（）’ 会自动执行对象的__call__方法一样，也是一个语法糖
#上面的2可以看成是int类的一个对象，所以 两个对象相加时也一样会调用这个方法

obj2=Foo()
v=obj1+obj2
print(v)  #输出 123


class Foo(object):
    def __init__(self,num):
        self.num=num

    def __add__(self, other):
        data=self.num+other.num
        return Foo(data)

obj1=Foo(11)
obj2=Foo(22)
v=obj1+obj2
print(v)

##其它对于加减乘除都可以使用

#可以查看下flask的源码中支持的 __方法__
#在local.py中查看


from flask import Flask


print("----------------------------------")


class Foo():
    def __str__(self):
        print("aaaa")
        return '123'

obj=Foo()
print(obj) ##语法糖： print(obj) 会自动执行对象的__str__方法