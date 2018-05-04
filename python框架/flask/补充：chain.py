#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from itertools import chain
def f1(x):
    return x+1

func1_list=[f1,lambda x:x-1]

def f2(x):
    return x+10

#需求：依次执行f1,f2,lamda函数

new_fun_list=chain([f2],func1_list)
# print(new_fun_list)

for func in new_fun_list:
    print(func)

##chain的作用： 相当于拼接多个函数列表，生成一个整的函数列表

##也适用于两个基本数据类型组成的类别的拼接，相当于加个链子