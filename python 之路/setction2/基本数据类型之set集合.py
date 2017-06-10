#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#set :无序 不重复 的序列

##列表
# li=[11,222,11,222]
# print(li)
# list=[]   #这种创建方法内部也会自动调用__init__方法；
# list()  #会自动执行list的__init__方法，即为list的构造方法，即内部会执行for循环，循环每个元素后添加到一个列表中；
# list((11,22,33))# 将一个元祖转换成列表
#
# #a.set的创建方法
# se={"123","456"}
# # print(type(se))
# # 输出：
# # C:\python3\python3.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/setction2/基本数据类型之set集合.py"
# # <class 'set'>
#
#
# # set()  #会自动执行set的 ___init__方法
#
# s=set()  # 创建一个空的集合；
# li=[11,222,11,222]
# s1=set(li)
# print(s1)
# 输出：
# C:\python3\python3.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/setction2/基本数据类型之set集合.py"
# {11, 222}
#总结：
# 创建集合的两种方式:
# 1.s1={11,22}
# 2.s2=set() 或 s2=set([11,22])


#b. set的功能

# s=set()
# print(s)
# s.add(123)
# print(s)
# s.clear()
# print(s)


s1={11,22,33}
s2={22,33,44}
s3=s1.difference(s2)
#s1中存在，s2中不存在的
print(s3)
# 输出：{11}











