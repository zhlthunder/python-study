#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##没有装饰器时的实现方式：
# LOGIN_USER={'is_login':False}
#
# def changepwd():
#     #pass  #同样对于这个函数也要进行登录验证，如果有无数多个其它的函数，都要进行相同的操作，即登录验证；
#     if LOGIN_USER['is_login']: ##这是登录验证的代码，
#         pass
#     else:
#         print("请登录！！")
#
# def manager():
#     if LOGIN_USER['is_login']: ##这是登录验证的代码，
#         print("欢迎%s登录" % LOGIN_USER['current_user'])
#     else:
#         print("请登录！！")
#
# def login(user,pwd):
#     if user=="alex" and pwd=="123":
#         LOGIN_USER['is_login']=True
#         LOGIN_USER['current_user']=user
#         manager()
#
# def main():
#     while True:
#         inp=input("1:后台管理；2:登录 -->:")
#         if inp=='1':  #如何直接输入1，就直接执行了manager函数了，虽然有报错，但问题是 用户没有登录时我也可以访问这个函数，这是不对的，需要进行是否登录的验证；
#             manager()
#         elif inp=='2':
#             username=input("请输入用户名：")
#             passwd=input("请输入密码：")
#             login(username,passwd)
#
# main()


##使用装饰器实现：
#总结，装饰器应用最多的场景就是进行登录验证用
LOGIN_USER={'is_login':False}

def outer(func):
    def inner(*args,**kwargs):
        if LOGIN_USER['is_login']:
            r=func()
            return r
        else:
            print("请登录！！")
    return inner


@outer
def manager():
        print("欢迎%s登录管理页面" % LOGIN_USER['current_user'])
@outer
def changepw():
        print("欢迎%s登录修改密码页面" % LOGIN_USER['current_user'])
@outer
def order():
        print("欢迎%s登录订单页面" % LOGIN_USER['current_user'])

def login(user,pwd):
    if user=="alex" and pwd=="123":
        LOGIN_USER['is_login']=True
        LOGIN_USER['current_user']=user
        manager()

def main():
    while True:
        inp=input("1:后台管理；2:登录 ;3:查订单；4：修改密码-->:")
        if inp=='1':  #如何直接输入1，就直接执行了manager函数了，虽然有报错，但问题是 用户没有登录时我也可以访问这个函数，这是不对的，需要进行是否登录的验证；
            manager()
        elif inp=='2':
            username=input("请输入用户名：")
            passwd=input("请输入密码：")
            login(username,passwd)
        elif inp=='3':
            order();
        elif inp=='4':
            changepw()

main()


