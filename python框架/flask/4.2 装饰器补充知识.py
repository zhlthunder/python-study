#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


##type 1:
def ff():
    pass

print(ff.__name__)   ##输出函数名 ff

#type 2:

def wrapper(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

@wrapper
def ff():
    pass

print(ff.__name__)  ##输出的函数名为inner,即已经被装饰过了

##type 3:
import functools

def wrapper(func):
    @functools.wraps(func)  ##帮忙设置函数的元信息，可以理解为将函数的名称等信息恢复成原来函数的新
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

##总结：inner对函数内容进行替换，而 functools.wraps 实现函数名的恢复

@wrapper
def ff():
    pass
print(ff.__name__)