#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
age=22
counter=0

for i in range(10):
    print("-->counter:",counter)
    if counter<3:
        inp=int(input("please input the guessing age:"))

        if inp==age:
            print("congratulations, you got it!!")
            break
        elif inp>age:
            print("think smarller")
        else:
            print("think bigger")
    else:
        continue_confirm=input("do you want to continue:y or n?")
        if continue_confirm=='y':
            counter=0
            continue
        else:
            print("bye")
            break
    counter+=1