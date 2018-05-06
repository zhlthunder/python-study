#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

class Mytype(type):
    def __init__(self,*args,**kwargs):
        print("init")
        super(Mytype,self).__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("call本质：调用类的__new__,再调用类的__init__")
        return super(Mytype,self).__call__(*args,**kwargs)

class Foo(metaclass=Mytype):  #通过Mytype的实例化来创建一个新的类，需要执行__init__,此时会打印 init
    pass


class Bar(Foo): ##这是一个派生类，如果一个类的基类是使用metaclass创建的，那这个类的在实例化的时候也要用metaclass来创建，所以也打印init
    pass

obj=Bar()  #既然已经实例化，这个，这个Bar可以看成是对象，对象+（），执行__call__方法，打印 call本质：调用类的__new__,再调用类的__init__
#
# 执行结果：
# init
# init
# call
