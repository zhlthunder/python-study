#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
age=22

for i in range(10):
    if i<3:
        inp=int(input("please input the guessing age:"))

        if inp==age:
            print("congratulations, you got it!!")
            break
        elif inp>age:
            print("think smarller")
        else:
            print("think bigger")
    else:
        print("you tried too many times, goodbye!!")
        break