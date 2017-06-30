#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# id_db={
#     37148199306143632:{
#         'name':"Alex li",
#         'age':22,
#         'addr':"Shandong"
#     },
#     220181993061418921:{
#         'name':"Shanpao",
#         'age':22,
#         'addr':"Dongbei"
#     },
#     220181993061418921:{
#         'name':"DaShanpao",
#         'age':22,
#         'addr':"Dongbei"
#     }
# }
# print(id_db)

# 备注：key必须是唯一的，如果两个key相同，就只显示一下，即字典的key是天然去重的。
id_db={
    37148199306143632:{
        'name':"Alex li",
        'age':22,
        'addr':"Shandong"
    },
    220181993061418921:{
        'name':"Shanpao",
        'age':22,
        'addr':"Dongbei"
    },
    220181993061418922:{
        'name':"DaShanpao",
        'age':22,
        'addr':"Dongbei"
    }
}
# print(id_db)

# print(id_db[220181993061418921])
# ##修改字典中的元素
# id_db[220181993061418921]['name']="wangminghu"
# print(id_db[220181993061418921])
# #为字典添加一个元素
# id_db[220181993061418921]['qq_of_wife']=123456
# print(id_db[220181993061418921])
#
# ##删除字典中元素
# # del id_db[220181993061418921]['addr']
# # print(id_db[220181993061418921])
#
# id_db[220181993061418921].pop('addr')
# print(id_db[220181993061418921])

# 获取值的方法
#获取的元素存在时，直接返回获取的元素，获取的元素不存在时，返回none
#而如果是直接使用字典名加key的方式，如果字典中没有这个key，就会使得程序出错，所以获取值时通常用get方法
# v=id_db.get(220181993061418921)
# print(v)
#
# v=id_db.get(123)
# print(v)
#
# v=id_db[123]
# print(v)
#
# 获取key和value
# print(id_db.keys())
# print(id_db.values())

# @@items：用于把字典转换成列表：
# print(id_db)
# print(id_db.items())
# 输出：
# C:\python3\python3.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section1/基本数据类型_字典.py"
# {37148199306143632: {'name': 'Alex li', 'age': 22, 'addr': 'Shandong'}, 220181993061418921: {'name': 'Shanpao', 'age': 22, 'addr': 'Dongbei'}, 220181993061418922: {'name': 'DaShanpao', 'age': 22, 'addr': 'Dongbei'}}
# dict_items([(37148199306143632, {'name': 'Alex li', 'age': 22, 'addr': 'Shandong'}), (220181993061418921, {'name': 'Shanpao', 'age': 22, 'addr': 'Dongbei'}), (220181993061418922, {'name': 'DaShanpao', 'age': 22, 'addr': 'Dongbei'})])


##使用update方法时，只讲dic2中存在而id_db中不存在的key：walue 添加到 id_db 中，相同的部分保持不变；
# dic2={
#     'name':"dffffff",
#     220181993061418922:{
#         'name':"DaShanpao",
#         'age':22,
#         'addr':"Dongbei"
#     }
# }
#
# id_db.update(dic2)
# print(id_db)

# 输出：
# C:\python3\python3.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section1/基本数据类型_字典.py"
# {37148199306143632: {'name': 'Alex li', 'age': 22, 'addr': 'Shandong'}, 220181993061418921: {'name': 'Shanpao', 'age': 22, 'addr': 'Dongbei'}, 220181993061418922: {'name': 'DaShanpao', 'age': 22, 'addr': 'Dongbei'}, 'name': 'dffffff'}

##场景2
# dic2={
#     'name':"dffffff",
#     220181993061418922:{
#         'name':"wwwwww",
#         'age':22,
#         'addr':"Dongbei"
#     }
# }
#
# id_db.update(dic2)
# print(id_db)
#
# 输出：
# C:\python3\python3.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section1/基本数据类型_字典.py"
# {37148199306143632: {'name': 'Alex li', 'age': 22, 'addr': 'Shandong'}, 220181993061418921: {'name': 'Shanpao', 'age': 22, 'addr': 'Dongbei'}, 220181993061418922: {'name': 'wwwwww', 'age': 22, 'addr': 'Dongbei'}, 'name': 'dffffff'}
# #备注：如果dic2 中存在和id_db中相同的key,但对应的vlaue 有更新，也需要将用新的value替换；


##场景3
# dic2={
#     'name':"dffffff",
#     220181993061418922:{
#         'name':"DaShanpao",
#     }
# }
#
# id_db.update(dic2)
# print(id_db)
#
# 输出：
# C:\python3\python3.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section1/基本数据类型_字典.py"
# {37148199306143632: {'name': 'Alex li', 'age': 22, 'addr': 'Shandong'}, 220181993061418921: {'name': 'Shanpao', 'age': 22, 'addr': 'Dongbei'}, 220181993061418922: {'name': 'DaShanpao'}, 'name': 'dffffff'}
# ##备注：子字典结构发生的变化也要更新到原字典中去

# @@判断是否存在
# id_db.has_key()  # only for python2

# print(220181993061418922 in id_db)
# output: True

# @@setdefault:取一个key,如果存在就返回对应的值，如果不存在就添加一个key:define_default_value
# dic2={
#     'name':"dffffff",
#     220181993061418922:{
#         'name':"DaShanpao",
#     }
# }
# print(dic2.setdefault(220181993061418922))#存在就返回
#
# print(dic2.setdefault(220181993061418923)) #不存在就追加一个
# print(dic2)
#
# print(dic2.setdefault(220181993061418924,"testing")) #不存在就追加一个
# print(dic2)
# 输出：
# C:\python3\python3.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section1/基本数据类型_字典.py"
# {'name': 'DaShanpao'}
# None
# {'name': 'dffffff', 220181993061418922: {'name': 'DaShanpao'}, 220181993061418923: None}
# testing
# {'name': 'dffffff', 220181993061418922: {'name': 'DaShanpao'}, 220181993061418923: None, 220181993061418924: 'testing'}


##fromkeys
# dic3={}
# print(dic3.fromkeys([1,2,33,44],'dddd'))
# 输出：
# C:\python3\python3.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section1/基本数据类型_字典.py"
# {1: 'dddd', 2: 'dddd', 33: 'dddd', 44: 'dddd'}

# @@popitem
# print(id_db.popitem())  #随机删除一个元素，不建议使用
# print(id_db)
#
# 输出：
# C:\python3\python3.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section1/基本数据类型_字典.py"
# (220181993061418922, {'name': 'DaShanpao', 'age': 22, 'addr': 'Dongbei'})
# {37148199306143632: {'name': 'Alex li', 'age': 22, 'addr': 'Shandong'}, 220181993061418921: {'name': 'Shanpao', 'age': 22, 'addr': 'Dongbei'}}


##循环一个字典
# for k,v in id_db.items():  ##此方法效率非常低，因为有一个dict to list的转换过程，推荐用方法2
#     print(k,v)
# 输出：
# C:\python3\python3.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section1/基本数据类型_字典.py"
# 37148199306143632 {'name': 'Alex li', 'age': 22, 'addr': 'Shandong'}
# 220181993061418921 {'name': 'Shanpao', 'age': 22, 'addr': 'Dongbei'}
# 220181993061418922 {'name': 'DaShanpao', 'age': 22, 'addr': 'Dongbei'}


# ##循环一个字典 ，方法2
# for key in id_db:
#     print(key)
#     print(id_db[key])
#
# 输出：
# C:\python3\python3.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section1/基本数据类型_字典.py"
# 37148199306143632
# {'name': 'Alex li', 'age': 22, 'addr': 'Shandong'}
# 220181993061418921
# {'name': 'Shanpao', 'age': 22, 'addr': 'Dongbei'}
# 220181993061418922
# {'name': 'DaShanpao', 'age': 22, 'addr': 'Dongbei'}

