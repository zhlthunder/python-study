#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 万恶的字符串拼接：
# 　　python中的字符串在C语言中体现为是一个字符数组，每次创建字符串时候需要在内存中开辟一块连续的空，
# 并且一旦需要修改字符串的话，就需要再次开辟空间，万恶的+号每出现一次就会在内从中重新开辟一块空间

# 字符串格式化输出

# name = "alex"
# print ("i am %s " % name)

# PS: 字符串是 %s;整数 %d;浮点数%f
# 字符串常用功能：
#
#     移除空白
#     分割
#     长度
#     索引
#     切片


# @@列表：
# 创建列表：
# name_list = ['alex', 'seven', 'eric']
# 或
# name_list ＝ list(['alex', 'seven', 'eric'])
#
# 基本操作：
#
#     索引
#     切片
#     追加
#     删除
#     长度
#     切片
#     循环
#     包含

# >>> name
# ['minglong', 'minghu', 'jack', 9]
# >>> name[1]
# 'minghu'
# >>>


# >>> name=["minglong","minghu","jack",9,11,10,'tome',11,222,45]
# >>> name[-1]
# 45
# >>> name[-2]
# 222
# >>>

# >>> name
# ['minglong', 'minghu', 'jack', 9, 11, 10, 'tome', 11, 222, 45]
# >>> name[0:2]
# ['minglong', 'minghu']


# >>> name
# ['minglong', 'minghu', 'jack', 9, 11, 10, 'tome', 11, 222, 45]
# >>> name[2:4]
# ['jack', 9]
# >>>

# >>> name
# ['minglong', 'minghu', 'jack', 9, 11, 10, 'tome', 11, 222, 45]
# >>> name[-3:-1]
# [11, 222]
# >>>

# >>> name
# ['minglong', 'minghu', 'jack', 9, 11, 10, 'tome', 11, 222, 45]
# >>> name[-3:-1]
# [11, 222]
# >>> name[-3:]
# [11, 222, 45]
# >>>

# >>> name
# ['minglong', 'minghu', 'jack', 9, 11, 10, 'tome', 11, 222, 45]
# >>> name[:3]
# ['minglong', 'minghu', 'jack']
# >>> name[:3][1:2]
# ['minghu']

# @@修改元素
# >>> name
# ['minglong', 'minghu', 'jack', 9, 11, 10, 'tome', 11, 222, 45]
# >>> name[1]="wangminghu"
# >>> name
# ['minglong', 'wangminghu', 'jack', 9, 11, 10, 'tome', 11, 222, 45]
# >>>

# @@插入
# >>> name
# ['minglong', 'wangminghu', 'jack', 9, 11, 10, 'tome', 11, 222, 45]
# >>> name.insert(2,"minggou")
# >>> name
# ['minglong', 'wangminghu', 'minggou', 'jack', 9, 11, 10, 'tome', 11, 222, 45]
# >>>


# >>> name
# ['minglong', 'wangminghu', 'minggou', 'jack', 9, 11, 10, 'tome', 11, 222, 45]
# >>> name.append("alex")
# >>> name
# ['minglong', 'wangminghu', 'minggou', 'jack', 9, 11, 10, 'tome', 11, 222, 45, 'alex']
# >>>

# >>> name
# ['minglong', 'wangminghu', 'minggou', 'jack', 9, 11, 10, 'tome', 11, 222, 45, 'alex']
# >>> name.remove("minggou")
# >>> name
# ['minglong', 'wangminghu', 'jack', 9, 11, 10, 'tome', 11, 222, 45, 'alex']
# >>>















