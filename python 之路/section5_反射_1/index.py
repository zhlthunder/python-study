#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


#需求：
##反射主要应用场景： web框架的路由系统
#以目前的知识，实现的方法如下，如果有很多的函数，用下面的方法效率就很低了。
# import commons
#
# def run():
#     inp=input("请输入要访问的URL:")
#     if inp=="login":
#         commons.login()
#     elif inp=="logout":
#         commons.logout()
#     elif inp=="home":
#         commons.home()
#     else:
#         print("404")
#
# if __name__=='__main__':
#     run()

##上面的方法效率很低，如果我们可以根据用户输入的内容自动的找到commons模块中的函数，就可以省略上面的无数个if else语句了
##反射完成的就是这样的功能


# import commons
# def run():
#     inp=input("请输入要访问的URL:")
#     ##用户输入的url为字符串类型
#     #反射就是：利用字符串的形式去对象（模块）中操作（寻找）成员；
#     func=getattr(commons,inp)
#     func()
#
# if __name__=='__main__':
#     run()

##使用上面的方法有一个问题，即如果找不到对应的成员时，就会报错；解决方法如下：

import commons
def run():
    inp=input("请输入要访问的URL:")
    ##用户输入的url为字符串类型
    #反射就是：利用字符串的形式去对象（模块）中操作（寻找,检查 删除 设置）成员；@@@@@@@
    if hasattr(commons,inp):  ##判断是否有这个成员
        func=getattr(commons,inp)
        func()
    else:
        print("404")

if __name__=='__main__':
    run()

##还有另外两个方法
# setattr()  #去模块中设置某个成员
# delattr()  #去模块中把某个成员删除
#说明，执行import  module_name 后，实际是把模块整个加载到内存中了，所有setattr 和 delattr 实际上就是在
# 内存中进行的操作，硬盘上存储的文件没有变化，当我们执行reload时，又会恢复成原来的样子了
##所有delattr 和 setattr都是在内存中进行操作@@@@@！



