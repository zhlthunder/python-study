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


# def outer(func):
#     def inner():
#         print("log")
#         return func()
#     return inner
#
# @outer
# def f1():
#     print("F1")
#
# @outer
# def f2():
#     print("F2")
#
# @outer
# def f100():
#     print("F100")


##type2:

# def outer(func):
#     def inner():
#         print("before")
#         ret=func()
#         print("after")
#         return ret
#     return inner
#
# @outer
# def f1():
#     print("F1")
#
# f1()

# 输出：
# before
# F1
# after

#通过装饰器,在不改变函数内部结构的情况下,在执行函数之前或之后执行一些操作;



#相关知识讲解

#相同的函数名定义多个函数体时，最后定义的一个生效；
# def f1():
#     print("123")
#
# def f1():
#     print("456")
#
# #f1函数最后执行print("456")


#函数代码整体可以做为参数进行传递；
# def f1():
#     print("123")
#
# def f2(xxx):
#     xxx()
#
# f2(f1)
# # 输出：
# 123


#正式开始讲解装饰器：
# def outer(func):
#         print(123,func)
#         return "111"
# @outer
# def f1():
#     print("F1")

#“@+函数名”这个组合放到某个函数的上面，就具有了魔法功能：
#1.会自动执行ourter函数，之前我们知道的函数执行的方式是 outer(),所以@outer可以实现相同的功能，并且将它下面紧跟的函数的函数名当做参数进行传递；
#2.将outer函数的返回值重新复制给f1
  #重要，即执行此句时，就自动执行了outer函数，并把f1函数名作为参数传入；执行结束后，会将outer的返回值返回给f1
#在本例子中，执行结束后，f1="111",即这样我们就实现了对函数的修改，我们可以将f1替换成一个字符串，也可以将它替换成一个函数，见下叙述


# 输出：
# 123 <function f1 at 0x03438468>


#按照下面的定义方式，outer函数返回的是一个函数inner,即执行@outer后，f1就会被重新赋值为inner函数了，即
# 修改了f1函数，即相当于在outer内部重新定义了一个新的函数，并把它赋值给f1;
# def outer(func):
#     def inner():
#         pass
#     return inner
#
# @outer
# def f1():
#     print("F1")


#实现inner函数的功能；
# def outer(func):
#     def inner():  #定义新的f1函数
#         print("before")
#         func()  #执行老的f1函数
#         print("after")
#     return inner
#
# @outer
# def f1():
#     print("F1")
#
# f1()
#输出： #可见，f1函数已经被修改了，被替换成inner函数了；
# before
# F1
# after

#总结，一旦一个函数被装饰器装饰了，则这个函数就会被重新赋值为 装饰器的内层函数了；

#定义函数，未调用，函数内部不执行；
#函数名代指整个函数体；


#装饰器流程剖析之返回值

def outer(func):
    def inner():
        print("before")
        ret=func()
        print("after")
        return ret
    return inner

@outer
def f1():
    print("F1")
    return "FFFFF"

rr=f1()
print(rr)
# 输出：
# before
# F1
# after
# FFFFF
