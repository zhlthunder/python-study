#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#三元运算符：
# if  1==1:
#     name="alex"
# else:
#     name="SB"
# print(name)

#如何1==1 条件成立， 让 name= "if 1==1"前面的值，否则name就等于 else后面的语句；
# name="alex" if 1==1 else "SB"  ##可以看做是if else的简写；
# print(name)

#lambda 表达式, 比如下面的简单的函数可以用lamda表达式来实现；但只能用一行，且只可以用于简单的赋值；
# def f1(a1):
#     return a1+10
#
# ret=f1(10)
# # print(ret)
# 输出： 20
#
# f2=lambda a1:a1+10  # f2的定义的功能和上面的f1定义的功能完全相同；
# ret=f2(10)
# print(ret)
# 输出： 20
#lambda可以带两个参数
# f2=lambda a1,a2:a1+a2+100
# ret=f2(3,3)
# print(ret)
# 输出：106

#lanmda中的参数可以有默认值；
# f2=lambda a1,a2=10:a1+a2+100
# ret=f2(3)
# print(ret)
# 输出：113


# #取绝对值 abs()
# print(abs(-1))
# 输出：1

#all()  any()

# False的值包括：
# print(bool(0))  #false
# print(bool(None))  #false
# print(bool(""))  #false 空字符串
# print(bool(" "))  #true
# print(bool([]))  #false
# print(bool({}))  #false
# print(bool(()))  #false

# print(all([1,2,3,4]))   #true
#all中接收可以别迭代的对象，比如列表，只有列表中的元素都为真是，才为真
# print(all([1,2,3,""]))  #false
# print(all([1,2,3,[]]))  #false
# print(all([1,2,3,{}]))  #false

#all()  :表示 所有为真是才为真
#any(): 只要一个为真即为真；
# print(any([1,0,"",None]))  #True



# ascii() # 自动会去执行某个对象的 __repr__方法；
# class Foo:
#     def __repr__(self):
#         return "1111"
# n=ascii(Foo())
# print(n)
# 输出：1111

# #bin() oct()   hex() 进制转换
# print(bin(5))  #0b101   把十进制转换为二进制
# print(oct(9))  #0o11   把十进制转换为八进制
# print(hex(15)) #0xf    把十进制转换为十六进制


##bytes  将字符串转换为字节；
#使用方法bytes(要转换的字符串，encoding=***)
#一个汉字，用utf-8编码时是3个字节， 用GBK编码时是2个字节；
# s="李杰"
# print(bytes(s,encoding="utf-8"))
# print(bytes(s,encoding="gbk"))
# # 输出：
# # b'\xe6\x9d\x8e\xe6\x9d\xb0'
# # b'\xc0\xee\xbd\xdc'

#字节转换成字符串的方法,使用str()方法
# a=1
# print(a,type(a))
# b=str(a)
# print(b,type(b))
# 输出：
# 1 <class 'int'>
# 1 <class 'str'>

##字节要转换成字符串，就要用str方法，且也要指定encoding的编码方式；
# s="李杰"
# n=bytes(s,encoding="utf-8")
# print(n)
# p=str(n,encoding="utf-8")
# print(p)
# 输出：
# b'\xe6\x9d\x8e\xe6\x9d\xb0'
# 李杰



