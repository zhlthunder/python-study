#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# obj=__import__("lib.account")
# print(obj)
# 输出：
# <module 'lib' (namespace)>

##即这种方式 只导入了 lib 模块

obj=__import__("lib.account",fromlist=True)
print(obj)
# 输出：  即此时导入的就是 accout.py 模块了
# <module 'lib.account' from 'C:\\Users\\lin\\PycharmProjects\\python_study_1s\\python_study\\git-zhl\\python-study\\python 之路\\section5_反射_3\\lib\\account.py'>
