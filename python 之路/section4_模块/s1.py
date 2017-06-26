#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#模块分为：
#内置模块，  自定义模块， 第三方模块；
#python中称为  模块， 在其它语言中称为   类库；

import sys
# print(sys.argv)  #打印函数的参数；

#模块都要先导入后使用；
#模块的存在形式：  .py文件  和 文件夹

#导入同级目录下的.py文件；
# import s2  #会把s2中的所有内容都加载到内存中；
# s2.login()
# s2.logout()
# 输出：
# login
# logout

#导入同级目录下的文件夹下的.py文件
# import lib.commons
# lib.commons.f1()
# 输出：
# F1


#为什么要用模块？
#就是为将代码归类，这样 无论是代码整洁度还是 调用的方便性上都有很大的提升；也便于进行代码的组织和管理；

#模块导入的原则是什么？
#就是依据sys.path中定义的路径从上到下逐个查找，找到第一个后就停止了

# import  sys
# for item in sys.path:
#     print(item)
#
# 输出：
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 之路\section4_模块  #当前执行的脚本所在的目录
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study #工程所在的目录，只在pycharm中有此，在linux或命令行下，都没有此目录，这是pycharm增加的一个目录，所以为了保持代码通用性，要忽略这个目录；
# C:\python3\python36.zip
# C:\python3\DLLs
# C:\python3\lib
# C:\python3
# C:\python3\lib\site-packages  #第三方模块的安装路径

#如何添加新的路径到 sys.path
# sys.path.append(diretory**)

##重要：我们自定义的模块，一定不要和系统模块重名，否则会出错；



##模块导入的方法有哪些：
#import type1:
# import s2
# import lib.commons

#import type2:
# from s2 import login
# login()
# 输出：
# login

#import type3:
# from s2 import *  #不建议使用这种方式
# login()
# logout()
# 输出：
# login
# logout


# #import type4:
# from lib import commons
# commons.f1()
# 输出：
# F1

#import type5:
# from lib import commons as lib_commons  #用于解决不同文件夹下的文件的文件名相同的情况下使用

##模块导入方法总结：
#1.对于同级目录下的.py文件，推荐： import s2 导入， 然后用 s2.login()执行；
#2 对于同级目录下的文件夹下的文件，推荐：from lib import commons，　然后使用　commons.f1()执行；


#安装第三方模块：
#源码安装方式： 借用源码包--python setup.py install
#pip3 安装方式： pip3 install requests 即可；
#pycharm安装方式

import requests
