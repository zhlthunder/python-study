#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#需求，代码分为业务线+基础代码，现在如果要对代码进行完善，推荐的方式是进对基础代码进行修改；

#基础代码
#修改前：
# def f1():
#     print("F1")
#
# def f2():
#     print("F2")
#
# def f100():
#     print("F100")

#修改后：修改方法1，修改在每个基础函数中修改代码；
# def f1():
#     print("log")
#     print("F1")
#
# def f2():
#     print("log")
#     print("F2")
#
# def f100():
#     print("log")
#     print("F100")



#修改方式2，定义了一个另外的函数，完成功能的扩展
# def outer():
#     print("log")
#
# def f1():
#     outer()
#     print("F1")
#
# def f2():
#     outer()
#     print("F2")
#
# def f100():
#     outer()
#     print("F100")

# ==》最好的方式是使用装饰器；
# 在软件开发过程中，有个开放封闭原则，即 函数的内部对所有的人来说是封闭的（即应该是黑盒子），对外只开发接口，同一添加功能是，不要在函数内部进行修改

# ==》是否有一种方式，就是在不修改函数内部结构的前提下，在函数的外部，为函数额外添加一个功能呢？ 就是装饰器


# 实现方式如下：


def outer(func):
    def inner():
        print("log")
        return func()
    return inner

@outer
def f1():
    print("F1")

@outer
def f2():
    print("F2")

@outer
def f100():
    print("F100")