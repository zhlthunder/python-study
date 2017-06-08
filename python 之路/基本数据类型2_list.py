#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

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



# name=['Alex','jack','Rain','Eric','Monica','Fiona']
# # print(name)
# name.insert(-1,'Minghu')  #不支持-2
# # print(name)
# name.insert(4,'Minglong')
# # print(name)
# name2=name[2:7]
# print(name2)

# print(name)
# name.remove('Fiona')
# print(name)

# @@删除几个连续的元素
# print(name)
# del name[4:6]
# print(name)

##删除整个列表
# del name  #删除后再打印name就报错，name 不存在；
# print(name)

# @@修改某个元素
# print(name)
# name[4]="Wuminglong"
# print(name)

# @@间隔打印或取值；
# print(name)
# print(name[0:-1:1])
# print(name[0::1])
# print(name[::1])
# print(name[::2])
# print(name[::3])


# @@判断是包含某个元素
# name=['Alex','jack','Rain',9,33,22,131,'Eric','Monica','Fiona',12,9,33,44,124,121,111,4,7,9,8]
# print(9 in name)
# if 9 in name:
#     print ("9 is in name")

# @@计数
# name=['Alex','jack','Rain',9,33,22,131,'Eric','Monica','Fiona',12,9,33,44,124,121,111,4,7,9,8,3]
# count_of_ele=name.count(9)
# print("[%s] 9 is in name"% count_of_ele)
# count_of_ele=name.count(3)
# print("[%s] 3 is in name"% count_of_ele)


# @@替换列表中所有某个特定元素
# name=['Alex','jack','Rain',9,33,22,131,'Eric','Monica','Fiona',12,9,33,44,124,121,111,4,7,9,8,3]
# # if 9 in name:
# #     num_of_ele=name.count(9)
# #     position_of_ele=name.index(9)
# #     print("[%s] 9 is in name, position:[%s]"%(num_of_ele,position_of_ele))
#
# for i in range(name.count(9)):
#     ele_index=name.index(9)
#     name[ele_index]=999999999999
# print(name)

# @@extend方法
# name=['Alex','jack','Rain',9,33,22,131,'Eric','Monica','Fiona',12,9,33,44,124,121,111,4,7,9,8,3]
# name2=['zhangsan','lisi','zhaosha']
# name.extend(name2)
# print(name)
# print(name2)

# name=['Alex','jack','Rain',9,33,22,131,'Eric','Monica','Fiona',12,9,33,44,124,121,111,4,7,9,8,3]
# print(name)
# name.reverse()
# print(name)

# @@python3中，字符串和数字不支持一起排序，如果是python2,则可以进行排序
# name=['Alex','jack','Rain',9,33,22,131,'Eric','Monica','Fiona',12,9,33,44,124,121,111,4,7,9,8,3]
# name.sort()
# print(name)

# @@pop
# name=['Alex','jack','Rain',9,33,22,131,'Eric','Monica','Fiona',12,9,33,44,124,121,111,4,7,9,8,3]
# name.pop() ##默认删除最后一个元素
# print(name)
# name.pop(0) ##删除指定索引的元素
# print(name)

# @@copy
# name=['Alex','jack','Rain',9,33,22,131,'Eric','Monica','Fiona',12,9,33,44,124,121,111,4,7,9,8,3]
# name3=name.copy()
# #copy之后，在内存中就是两个独立空间，互不影响，无论哪个修改了，对另外一个都没有影响
# name[0]="ALEX"
# print(name)
# print(name3)

# @@copy为浅拷贝，即深层的列表没有拷贝，即两个指向同一个内存空间，这样，如果老的列表的内存列表内容修改，因为新的列表也指向相同的地址，所以也同步变化了
# copy 默认值拷贝第一层；因为第二层数据量有可能非常大；所以浅拷贝只对第一层进行拷贝；
# 备注：对于第二层的列表，在第一层中存储的只是内层列表的内存地址，是个指针；

import copy
name=['Alex','jack','Rain',[9,1,2,4],9,33,22,131,'Eric','Monica','Fiona',12,9,33,44,124,121,111,4,7,9,8,3]
name3=name.copy()
name4=copy.copy(name)  ##和上面的copy一样，也是浅层copy
name5=copy.deepcopy(name)  ##这个是完全拷贝，两个列表完全独立了

name[0]="ALEX"
name[3][3]=44444444
print(name)
print(name3)
print(name4)
print(name5)









