#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##新的问题， 如果要导入的模块在当前目录下的文件夹下，该如何自动查找和导入呢？



def run():
    inp=input("请输入要访问的URL:")
    ##比如用户输入的URL 格式为  account/login

    m,f = inp.split('/')
    ##如果安装以前的方式去导入的话，应该为： Import lib.account
    ##此处的m就相当于上面的account, 所有我们需要做字符串的拼接，即加上 lib.
    obj=__import__("lib."+m,fromlist=True)
    if hasattr(obj,f):
        func=getattr(obj,f)
        func()
    else:
        print("404")

if __name__=='__main__':
    run()

# 输出：
# 请输入要访问的URL:account/login
# 炫酷的登录页面

# 请输入要访问的URL:commons/home
# 炫酷的主页面

# 请输入要访问的URL:manager/order
# 炫酷的订单页面


# 总结：
# 我们在这里就是伪造了一个web框架的路由系统，
# 反射：基于字符串的形式去对象中操作其成员；
# getattr()  hasattr()  delattr()  setattr()

# 扩展：
# 导入模块：
# import  ###
# from $$ import  ###
#
# obj=__import__("###")
# obj=__import__("@@@.###",fromlist=True)
