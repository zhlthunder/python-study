#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
"""
我是注释
"""


##模块中特殊变量
#
# __name__
# __file__

# ##用户定义的全局变量
# NAMEINFO="aaaaa"


##s2.py 是个空文件

import s2
# print(vars(s2))  ##可以输出s2模块中所有的变量


# ==> 我们需要关心的特殊的变量包括：

# __doc__
# __file__
# __cached__
# __name__
# __package__


#__doc__  #获取文件的注释
# print(__doc__)
# 输出：  我是注释
#即将当前执行的 py文件的注释封装到 __doc__中去了；

#__cache__
#当py脚本 中导入某个模块时，会自动生成这个模块对应的字节码



#__file__
#当我们运行s1,就可以使用__file__ 获取当前运行的py文件所在的路径
print(__file__)
# 输出：
# C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section5_模块2/s1.py

