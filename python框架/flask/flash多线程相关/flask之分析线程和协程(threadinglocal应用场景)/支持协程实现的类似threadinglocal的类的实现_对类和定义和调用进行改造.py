#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 下面代码的功能和 flask内部的 local.py 功能完全相同，可以通过搜索打开local.py


# import flask.globals
import  flask,threading
# from greenlet import getcurrent as get_ident  ##获取当前协程的ID，此处虽然导入时有波浪线，但可以正常使用，原因待确认
# from _thread import get_ident ##可以获取线程的唯一标识

try:
    from greenlet import getcurrent as get_ident  #先尝试导入协程相关的获取ID的模块， 即优先使用协程，如果没有安装协程的模块，就不支持协程
except ImportError:
    try:
        from thread import get_ident  ##如果上面的报错，表示不支持协程，再导入线程相关的获取ID的模块
    except ImportError:
        from _thread import get_ident


class Local(object):
    def __init__(self):
        object.__setattr__(self, '__storage__', {})
        object.__setattr__(self, '__ident_func__', get_ident)


    def __getattr__(self, name):
        try:
            return self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}

    def __delattr__(self, name):
        try:
            del self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)



local_values=Local()

def func(num):
    local_values.name=num
    import time
    time.sleep(1)
    print(local_values.name, threading.current_thread().name)


for i in range(20):
    th = threading.Thread(target=func, args=(i,), name='线程%s' % i)
    th.start()




"""
总结：
所以flask内部，保存你请求相关， session相关的一些针对不同客户端不用的信息，都是基于上面讲的local来实现的。
"""