#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# import functools
#
# def func(a1,a2):
#     print(a1,a2)
#
# new_func=functools.partial(func,666) #生成一个新的函数，但对函数进行了一次封装，先封装了一个实参,即帮助我们完成了第一个参数的传递
# new_func(999)


# import functools
#
# def func(a1,a2,a3,a4):
#     print(a1,a2,a3,a4)
#
# new_func=functools.partial(func,666,77,88)
# new_func(999)


#如果是指定参数，就都要指定,否则会报错
import functools

def func(a1,a2,a3,a4):
    print(a1,a2,a3,a4)

new_func=functools.partial(func,a1=666,a2=77,a3=88)
new_func(a4=999)
