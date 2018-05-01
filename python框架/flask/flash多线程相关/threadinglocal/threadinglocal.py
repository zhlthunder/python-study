#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# refer: http://www.cnblogs.com/wupeiqi/articles/8202353.html
# flask的request和session设置方式比较新颖，如果没有这种方式，那么就只能通过参数的传递。
#
# flask是如何做的呢？
#
# 1. 本地线程，保证即使是多个线程，自己的值也是互相隔离。

# 常规的多线程实现方法如下：
# import threading
# class Foo(object):
#     def __init__(self):
#         self.name=0
#
# local_values=Foo()
# def func(num):
#     local_values.name = num
#     import time
#     time.sleep(1)
#     print(local_values.name, threading.current_thread().name)
#
#
# for i in range(20):
#     th = threading.Thread(target=func, args=(i,), name='线程%s' % i)
#     th.start()


# 执行结果如下： 即所有的线程获取的结果都是19，这是有问题的。
# 19 线程3
# 19 线程1
# 19 线程0
# 19 线程2
# 19 线程8
# 19 线程5
# 19 线程4
# 19 线程7
# 19 线程11
# 19 线程12
# 19 线程9
# 19 线程6
# 19 线程10
# 19 线程14
# 19 线程13
# 19 线程15
# 19 线程16
# 19 线程17
# 19 线程18
# 19 线程19


##基于threadinglocal的实现方式, 而flask中不是直接使用它，而是借鉴了它的实现思想（！！！重要）

import threading
local_values = threading.local()  ##可以理解为：来了一个线程时，就开辟一个专用的空间给你使用，保存这个线程独有的值

def func(num):
    local_values.name = num
    import time
    time.sleep(1)
    print(local_values.name, threading.current_thread().name)


for i in range(20):
    th = threading.Thread(target=func, args=(i,), name='线程%s' % i)
    th.start()

# 输出：
# 2 线程2
# 1 线程1
# 0 线程0
# 8 线程8
# 7 线程7
# 6 线程6
# 5 线程5
# 4 线程4
# 3 线程3
# 12 线程12
# 11 线程11
# 10 线程10
# 9 线程9
# 15 线程15
# 14 线程14
# 13 线程13
# 19 线程19
# 18 线程18
# 17 线程17
# 16 线程16

