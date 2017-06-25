#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

def manager():
    pass

def login():
    pass

def main():
    inp=input("1:后台管理；2:登录 -->:")
    if inp=='1':
        manager()
    elif inp=='2':
        username=input("请输入用户名：")
        passwd=input("请输入密码：")
        login()