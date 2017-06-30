#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

user="jack"
passwd="123"

username=input("please input username:")
password=input("please input password:")
#
#type 1:
# if username==user:
#     print("correct usrname")
#     if password==passwd:
#         print("welcome to login!!")
#     else:
#         print("wrong password")
# else:
#     print("wrong usrname")


# type 2:
if username==user and password==passwd:
    print("welcome to login!!")
else:
    print("invalid usrname or password...")
