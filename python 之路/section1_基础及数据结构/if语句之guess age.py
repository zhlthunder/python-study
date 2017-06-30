#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

age=22
inp=int(input("please input the guessing age:"))

if inp==age:
    print("congratulations, you got it!!")
elif inp>age:
    print("think smarller")
else:
    print("think bigger")
