#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#1.获取类中私有字段的方法说明


#共有方法和共用字段，内部外部都可以访问
#私有字段，内部可以访问，外部可以访问

#面向对象，私有属性的问题， __age
# class  Foo(object):
#     def __init__(self):
#         self.name='tom'
#         self.__age=18  ##
#
# obj=Foo()
# print(obj.name)
# print(obj.__age) ##这条命令执行时会报错：
# AttributeError: 'Foo' object has no attribute '__age'
#即类的私有属性，在外面是无法访问的，如果要方法，可以用下面的方法：


# class  Foo(object):
#     def __init__(self):
#         self.name='tom'
#         self.__age=18  ##
#
#     def get_age(self):
#         return self.__age
#
# obj=Foo()
# print(obj.get_age())




##私有字段，另外的一个获取的方法如下：

class  Foo(object):
    def __init__(self):
        self.name='tom'
        self.__age=18  ##


obj=Foo()
print(obj._Foo__age)  #用这种方法也可以获取到。
