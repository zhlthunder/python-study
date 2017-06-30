#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


##问题来了，实际的应用场景中，可能会用非常多的模块，如果美国模块都要导入，也是效率非常低
##比如现在：
# index.py 为主程序
# account.py commons.py  manager.py  为要调用的模块

##需求： 首先，模块名和字符串是不同的， 如果模块名也能通过字符串的形式导入的话，就可以达到我们的需求了
#即 python 如果支持以字符串的形式导入模块， 且支持以字符串的形式从模块中导入成员，就可以满足我们的需求了@@@@@

# __import__()  #以字符串的形式导入模块, 即下面的两种方式是一样的功能
# import commons as obj
# obj=__import__("commons")


def run():
    inp=input("请输入要访问的URL:")
    ##比如用户输入的URL 格式为  account/login
    m,f = inp.split('/')
    obj=__import__(m)
    if hasattr(obj,f):
        func=getattr(obj,f)
        func()
    else:
        print("404")

if __name__=='__main__':
    run()




