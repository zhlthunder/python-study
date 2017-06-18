#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


def login(username,passwd):
    """  #输入三个引号后直接回车，就会自动补全下面的 注释信息（入参， 返回值等）
    用于用户登录
    :param username: 用户输入的用户名
    :param passwd: 用户输入的密码
    :return: true 表示登录成功； false 表示登录失败；
    """
    f=open("db",'r')
    for line in f:
        line_list=line.strip().split("|")  #如何不加strip,可能会遇到错误；
        if line_list[0]==username and line_list[1]==passwd:
            return True
    return False


def register(username,password):
    """
    用户注册
    :param username: 输入的用户名
    :param password: 输入的密码
    :return: 默认返回None
    """
    f=open("db",'a')
    temp="\n"+username+"|"+password
    f.write(temp)
    f.close()


def main():
    t=input("1:登录；2：注册 -->")
    if t=="1":
        user=input("请输入用户名:")
        passwd=input("请输入密码:")
        ret=login(user,passwd)
        if ret==True:
            print("登录成功")
        else:
            print("登录失败")
    elif t=="2":
        user=input("请输入用户名：")
        passwd=input("请输入密码：")
        register(user,passwd)

main()

#函数和函数之间有两个空格是标准格式，如果用一个空格，就会有波浪线，提示不是完全标准；