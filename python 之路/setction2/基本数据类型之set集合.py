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
##@1
# s=set()
# print(s)
# s.add(123)
# print(s)
# s.clear()
# print(s)

##@2
s1={11,22,33}
s2={22,33,44}
# s3=s1.difference(s2)
# #s1中存在，s2中不存在的
# print(s3)
# # 输出：{11}
#
# s4=s2.difference(s1)
# #s2中存在，s1中不存在的
# print(s4)
# # 输出：{44}

#对称差集
# s5=s1.symmetric_difference(s2)
# print(s5)
# 输出：{11, 44}

#上面的几种模式，s1和s2都保持不变；

# print(s1)
# s1.difference_update(s2)
# print(s1)

#因为带了update，会将结果更新到调用方法的那个集合中去；
# 输出：
# {33, 11, 22}
# {11}

#因为带了update，会将结果更新到调用方法的那个集合中去；
# print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)
# 输出：
# {33, 11, 22}
# {11, 44}



#@discard 移除某个元素，不存在不报错；
s1={11,22,33}
# s1.discard(11)
# print(s1)
# #不存在111，也不报错
# s1.discard(111)
# print(s1)

#@remove, 移除不存在的元素会报错；
# s1.remove(11)
# print(s1)
# s1.remove(1111)
# print(s1)

#pop 随机移除一个元素，可以获得移除的元素
# ret=s1.pop()
# print(ret)
# print(s1)
# 输出：
# 33
# {11, 22}


# #@取交集
# s1={11,22,33}
# s2={22,33,44}
# # s3=s1.intersection(s2)
# # print(s3)
# # 输出：
# # {33, 22}
# s1.intersection_update(s2)
# print(s1)
# 输出：{33, 22}

#@判断
# s1={11,22,33}
# s2={22,33,44}
# print(s1.isdisjoint(s2)) #如果没有交集返回True,否则返回false
#
# s1={11,22,33}
# s2={22,33}
# print(s1.issubset(s2)) #判断是否为子集
# print(s1.issuperset(s2)) #判断是否为父集


#@取并集合
# s1={11,22,33}
# s2={22,33,44}
# s3=s1.union(s2)
# print(s3)


# #@update方法
# s1={11,22,33}
# li=[11,222,333,444]
# s1.update(li)
# print(s1)
# # 输出：{33, 11, 333, 22, 444, 222}
# #update 内部进行了一个循环，逐个调用update方法来添加元素；
# s1.update("zhlthunder")
# print(s1)
# 输出：
# {'u', 33, 'z', 'd', 11, 'l', 333, 'h', 't', 'e', 'r', 'n', 22, 444, 222}


#@带双下划线的方法
li=[11,22,33] #会自动执行list的__init__方法
li()  #会自动执行list的__call__方法





