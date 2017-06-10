#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# @@元祖，为不可变列表；
#
#
# >>> r=(1,2,3,4,5)
# >>> type(r)
# <class 'tuple'>

# @@元组只支持两个方法， count 和 index
# ages=(11,22,33,44,55)
# print(ages.count(11))
# print(ages.index(44))



# @@字符串：
# @@移除输入中的空格, 默认是移除空格，也可以移除其它的指定字符
# username=input("pleaser input username:")
# if username.strip()=="tom":
#     print('welcome')


# @@字符串分割成列表，列表组合成字符串
# names="alex,jack,tony,eric"
# print(type(names))
# print(names)
# name2=names.split(",")
# print(type(name2))
# print(name2)
#
# name3="/".join(name2)
# print(type(name3))
# print(name3)

# # @@判断是否存在某个元素
# name="alex li"
# print('' in name)
#
# #首个字母大写
# print(name.capitalize())

# @@字符串格式化

# msg="Hello,{name},it's been a long {age} since lat time spoke"
# msg1=msg.format(name="tom",age=123)
# print(msg1)
#
# msg="Hello,{0},it's been a long {1} since lat time spoke"
# msg2=msg.format('Alex',23)
# print(msg2)

# @@切片
# name="alex li"
# print(name[2:4])


# @@center方法
# name="alex li"
# print(name.center(40,'-'))


# name="alex li"
# print(name.find('e')) #返回元素的下标
# print(name.find('l')) ##找到多个时，返回第一个的下标
# print(name.find('p')) ##找不到返回-1

##判断输入是否为数字
# age=input("your age:")
# if age.isdigit():
#     age=int(age)
# else:
#     print("invalid data type")

##判断是否有特殊字符
# name="aasdfa!tony"
# print(name.isalnum())
# name="aasdfa4tony"
# print(name.isalnum())

# ##判断以什么开始和结束
# name="alex3elff"
# print(name.endswith("elff"))
# print(name.startswith("alex"))

#大写和小写的转换
# name="alex3elff"
# print(name.upper())
# name="ALEX"
# print(name.lower())


