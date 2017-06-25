#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# li=[11,22,33,44]
#
# tt=filter(lambda x:x>22,li)
# # print(list(tt))
# print(tt)  #执行这条命令，在python2.7中会直接返回一个list,但在python3中会返回一个对象；
# # 输出：
# # <filter object at 0x016232D0>

#假设上面的filter产生的输出数据量非常大的话，那如果直接输出的话，会非常占内存，而如何只返回一个对象的话，
#就表示它具有生成数据的能力，只有你去循环它的时候才会输出元素，这样就避免占用内存的情况发生；

#再观察下面的两个命令
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study>python2
# Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> range(10)  #生成全部的元素
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> xrange(10)  #返回一个对象，具有生成数据的能力，在我们去循环它的时候才会生成数据；
# xrange(10)
# >>>

#即我们就引出了生成器
#生成器是使用函数创造出来的；

#普通函数
# def fun():
#     return 123
#
# ret=fun()

#下面对普通函数进行改造，让它变成生成器
#只有函数中出现了yield，那这个函数就是个生成器
# def fun():
#     yield 1
#     yield 2
#     yield 3
#
# ret=fun()
# print(ret)
# 输出：
# <generator object fun at 0x02A00DB0>
#执行函数时，没有打印内容，而是返回了一个对象；
#总结： 只要在普通的函数中出现了yield,那这个函数就变成了一个生成器

#下面是获取生成器输出的方法，即循环生成器返回的对象时，就获取了每个元素
# for i in ret:
#     print(i)
# 输出：
# 1
# 2
# 3

#说明：循环时的执行流程是：第一次执行yield 1, 第二次接着之前继续执行yield 2,依次类推，逐个执行；


#另外一种查看方式：
# def fun():
#     print(111)
#     yield 1
#     print(222)
#     yield 2
#     print(333)
#     yield 3
#
# ret=fun()
# r=ret.__next__()  #进入函数找到yield,将yield后面的数据获取，然后返回退出，即第一次执行时，输出 111  和 1
# print(r)
# r=ret.__next__() #进入函数，紧接着之前的断点继续执行，执行到下一下yield时，将yield后面的数据获取，然后返回退出，即这次输出 222和2
# print(r)
# r=ret.__next__()#进入函数，紧接着之前的断点继续执行，执行到下一下yield时，将yield后面的数据获取，然后返回退出，即这次输出 333和3
# print(r)

# 输出：
# 111
# 1
# 222
# 2
# 333
# 3

#即yield 会保存上次的执行位置，在进行循环时，会接着上次的位置继续执行，即顺序或断点是受yield控制的。


#基于生成器实现range的功能
#下面的myrange实现了和range相同的功能
# def myrange(arg):
#     start=0
#     while True:
#         yield start
#         start+=1
#         if start==arg:
#             break
#
# ret=myrange(10)
# for i in ret:
#     print(i)

#总结： 当一个函数中使用yield时，它就是一个生成器，
 # 是因为在代码编译的时候，遇到了yield,就会自动把这个函数编译成了一个生成器函数了
 #生成器只是一个具备生成能力的对象，即它只负责生成，如果我们要去拿元素，我们需要进入一个一个地取；

def myrange(arg):  #这就是一个生成器
    start=0
    while True:
        yield start
        start+=1
        if start==arg:
            break

ret=myrange(10)  #我们拿到了这个生成器的对象，这个对象是可以被迭代的，也就是迭代器；
#可以使用__next__() 方法来取值，只可以向后取，不可以向前取。
# 可以被迭代的对象就叫迭代器，可以使用__next__方法去逐个取值；
#且for循环内部就是使用了__next__方法来进行的循环；使用__next__时，如果取完了再取的话会报错，但使用for循环取值的时候不会报错；
#所以一般我们都是利用for循环来从生成器中取值的。

#生成器如何去写，就是使用yield实现的；
#迭代器如何去写，不需要去写，它是python 的一个内部功能，只要使用for循环（内部封装了迭代的功能）就可以了


#递归：

# def d():
#     return '123'
#
# def c():
#     r=d()
#     return r
#
# def b():
#     r=c()
#     return r
#
# def a():
#     r=b()
#     print(r)
#
# a()

# 输出：
# 123


def func(n):
    n+=1
    if n>=10:
        return 'end'
    return func(n)

ret=func(1)
print(ret)

#递归就是自己反复调用自己