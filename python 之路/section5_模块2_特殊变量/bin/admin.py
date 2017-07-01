#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#这个为主的可执行文件
##需求：我们需要把它的上一级的上一级目录　，即“section5_模块2 ” 添加到sys.path中去；
#因为一般组织代码结构是，第一级目录是：section5_模块2， 而 主运行脚本放到 section5_模块2/bin/ 下面，


##如果用下面的这种方式添加代码路劲的话，当操作环境变更时就无法执行了，即没用通用性
# import sys
# sys.path.append("C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 之路\section5_模块2")


##基于上面的问题，如果我们可以获取当前文件所在的路径，然后向上找它的父母了，就可以得出一个通用的查找和添加路径的方法

import sys
# print(__file__)
import os
# print(os.path.abspath(__file__))  ##获取某个文件的绝对路径

# 输出：
# C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section5_模块2/bin/admin.py
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 之路\section5_模块2\bin\admin.py

# 如果在命令行下，cd 到admin.py所在的路径后执行admin.py得到的输出为：
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 之路\section5_模块2\bin>python3 admin.py
#     admin.py  ##只拿到文件名
#     C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 之路\section5_模块2\bin\admin.py ##拿到文件的完整路径
#
# ##总结：
# print(__file__)  ##如果不是在admin.py所在的目录下执行，获取的就是文件的完整路径；如果是cd到admin.py所在的目录下执行，就只能获得文件名
# print(os.path.abspath(__file__)) ##无论在哪里执行，永远获取的是文件的完整路径


# ==》 此时，我们解决了第一个问题，即通过： os.path.abspath(__file__) 获取文件的绝对路径；

ret=os.path.dirname(os.path.abspath(__file__))
# print(ret)
#获取上一级目录的路径：
# 输出：
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 之路\section5_模块2\bin

rt=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(rt)
# 输出：
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 之路\section5_模块2
#获取上一级的上一级目录了

# 我们只要直接执行下面这句就可以了：
# 就可以将程序包的第一级目录加到sys.path中了，这样，无论把这个软件包放到哪里，都可以通过 软件包/bin/admin.py 来直接运行程序了

# @@@这句代码非常重要，是固定的用法
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



