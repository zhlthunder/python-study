#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import random
#完成5位随机验证码的生成
def valiate1():
    string =''
    for i in range(5): #设置验证码位数
        rand_num = random.randint(0,61) #一共有62种可能的情况
        if rand_num < 10:
            string += str(rand_num)
        elif 10 <= rand_num <= 35:
            string += chr(rand_num+55) #随机产生A-Z
        else:
            string += chr(rand_num+61) #随机产生a-z3
    return string
print(valiate1())
#该方法数字，大写字母，小写字母出现的概率相同
def valiate2():
    string =''
    for i in range(5): #设置验证码位数
        rand_num = random.randint(0,9)
        rand_alpha = chr(random.randint(97,122))
        rand_Alpha = chr(random.randint(65,90))
        res =random.choice([str(rand_num),rand_alpha,rand_Alpha])
        string += res
    return string
print(valiate2())