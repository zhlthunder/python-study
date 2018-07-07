#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

"""
python对协程的支持是通过generator实现的

"""

def run():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30

##协程的最简单风格，控制函数分阶段执行，节约线程或进程的切换；
##返回的是一个生成器
m=run()
print(m)  #输出： <generator object run at 0x0353E180>  是一个生成器
print(next(m))   #输出 1，10
print(next(m))   #输出 2，20
print(next(m))   #输出 3，30