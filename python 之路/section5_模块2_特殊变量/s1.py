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
# print(__file__)
# 输出：
# C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/section5_模块2/s1.py


#__package__
# print(__package__)
# 输出为none,即输出当前文件的_package__为 none;

# from bin import admin
# print(admin.__package__)
# 输出：
# bin
#总结：即__package__ 表示你的这个模块在哪里，就是返回所在包的名字；
# 比如  admin.py在 bin  文件夹（包）中；所有返回为bin
# 而当前我们执行s1.py时,它就是主文件，它没有在任何文件夹（包），所有返回NOne



#__name__
#特性，比如我现在执行s1.py， 那s1模块中的 __name__="__main__",而其它程序调用s1模式时，则不等于__main__
#即只有执行当前文件时候，当前文件的特殊变量 __name__="__main__"


##举例,比如在s1.py中定义了如下的代码，则 执行s1.py时 和 别的脚步中导入s1时都会执行run函数
# def run():
#     print("running")
# run()


##但如果使用下面的方法写，则执行有在执行当前脚步 s1.py时，run函数才会执行， 在其它脚步中导入s1都不会执行run函数；
def run():
    print("running")

if __name__=="__main__":
    run()

##就是基于这个特性，我们一般会在代码的主脚本中增加如下的两段代码
#即只有你执行我时，才会执行此脚本，如果你导入我，我就不会执行；即一般主程序文件中都会有这句；

##@@@@@@重要
if __name__=="__main__":
    run()


##总结：
# __doc__
# __file__  @@@重要
# __package__
# __cached__
# __name__  @@重要



# @@@sumarry at last:
__file__
# @@@这句代码非常重要，是固定的用法
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

__name__
##@@@@@@重要
if __name__=="__main__":
    run()