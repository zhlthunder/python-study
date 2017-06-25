#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# USER_INFO={}
#
# ##针对登录验证的装饰器
# def check_login(func):
#     def inner(*args,**kwargs):
#         if USER_INFO.get('is_login',None): #使用get方法时不存在时不报错，且如果不存在时，可以设置一个默认值
#             ret=func(*args,**kwargs)
#             return ret
#         else:
#             print("请登录")
#     return inner
#
#
# #有两层验证，1，先验证是否登录了？ 2,验证是否是管理员；
# def check_admin(func):
#     def inner(*args,**kwargs):
#         if USER_INFO.get('is_login',None): #使用get方法时不存在时不报错，且如果不存在时，可以设置一个默认值
#             if USER_INFO.get('user_type',None)==2:
#                 ret=func(*args,**kwargs)
#                 return ret
#             else:
#                 print("无权限查看")
#         else:
#             print("请登录")
#     return inner
#
# @check_admin
# def index():
#     """
#     这是管理员的功能
#     :return:
#     """
#     print("index")
#
# @check_login
# def home():
#     """
#     普通用户的功能
#     :return:
#     """
#     print("home")
#
# def login():
#     user=input("请输入用户名：")
#     if user=='admin':
#         USER_INFO['is_login']=True
#         USER_INFO['user_type']=2
#     else:
#         USER_INFO['is_login']=True
#         USER_INFO['user_type']=1
#
#
#
# def main():
#     while True:
#         inp=input("1:登录；2：查看信息；3：超级管理员管理-->")
#
#         if inp=='1':
#             login()
#         elif inp=='2':
#             home()
#         elif inp=='3':
#             index()
#
# main()

#说明，上面的check_admind的装饰器存在代码重复的问题，如果有很多层的条件，就会导致代码重复很多，此处就引出了双重装饰器
#实现方式如下

USER_INFO={}

##只针对登录验证的装饰器
def check_login(func):
    def inner(*args,**kwargs):
        if USER_INFO.get('is_login',None): #使用get方法时不存在时不报错，且如果不存在时，可以设置一个默认值
            ret=func(*args,**kwargs)
            return ret
        else:
            print("请登录")
    return inner


##只针对超级用户验证的装饰器
def check_admin(func):
    def inner(*args,**kwargs):
        if USER_INFO.get('user_type',None)==2:
            ret=func(*args,**kwargs)
            return ret
        else:
            print("无权限查看")
    return inner

#一个函数可以被多个装饰器装饰
#双层装饰的流程如下：
#首先，index被check_admin装饰，用check_admin的内层inner函数替换index函数，即为新的index函数；然后新的index函数
#又被check_login装饰，用check_login的内层函数inner替换新的index函数，得到 新新index函数；
#所有可以得出结论是：从上到下依次是：　外层验证（验证是否登录）－＞内层验证（验证是否是超级用户）－＞原函数
#所以多重装饰的应用顺序就参考这个流程；
#多层装饰器，装饰的时候，是从下往上装饰； 执行的时候，从上往下执行；

@check_login    #先验证是否登录
@check_admin    #在验证是否是超级用户
def index():
    """
    这是管理员的功能
    :return:
    """
    print("index")

@check_login
def home():
    """
    普通用户的功能
    :return:
    """
    print("home")

def login():
    user=input("请输入用户名：")
    if user=='admin':
        USER_INFO['is_login']=True
        USER_INFO['user_type']=2
    else:
        USER_INFO['is_login']=True
        USER_INFO['user_type']=1



def main():
    while True:
        inp=input("1:登录；2：查看信息；3：超级管理员管理-->")

        if inp=='1':
            login()
        elif inp=='2':
            home()
        elif inp=='3':
            index()

main()


#装饰器总结：
#1.单层装饰器；
# 2.多层装饰器
# 即一个函数可以被N个装饰器去装饰，编译的时候，是从下往上去编译的，执行的时候，是从上往下去执行的
# 3.更牛逼的装饰器，请参考下面的博客
# http://www.cnblogs.com/wupeiqi/articles/4980620.html
# 举例：
#!/usr/bin/env python
#coding:utf-8

# def Before(request,kargs):
#     print 'before'
#
# def After(request,kargs):
#     print 'after'
#
#
# def Filter(before_func,after_func):
#     def outer(main_func):
#         def wrapper(request,kargs):
#
#             before_result = before_func(request,kargs)
#             if(before_result != None):
#                 return before_result;
#
#             main_result = main_func(request,kargs)
#             if(main_result != None):
#                 return main_result;
#
#             after_result = after_func(request,kargs)
#             if(after_result != None):
#                 return after_result;
#
#         return wrapper
#     return outer
#
# @Filter(Before, After)
# def Index(request,kargs):
#     print 'index'