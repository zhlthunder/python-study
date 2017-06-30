#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# count = 0
# while True:
#     print("你是风儿我是沙,缠缠绵绵到天涯...",count)
#     count +=1

# count = 0
# while True:
#     print("你是风儿我是沙,缠缠绵绵到天涯...",count)
#     count +=1
#     if count == 100:
#         print("该结束了，哈哈哈哈..")
#         break

# count = 0
# while True:
#     if count>50 and count<60:
#         count+=1
#         continue
#     print("你是风儿我是沙,缠缠绵绵到天涯...",count)
#     count +=1
#     if count == 100:
#         print("该结束了，哈哈哈哈..")
#         break


my_age = 28

count = 0
while count < 3:
    user_input = int(input("input your guess num:"))

    if user_input == my_age:
        print("Congratulations, you got it !")
        break
    elif user_input < my_age:
        print("Oops,think bigger!")
    else:
        print("think smaller!")
    count += 1 #每次loop 计数器+1
else:
    print("猜这么多次都不对,你个笨蛋.")