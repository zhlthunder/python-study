#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


##需求：写一个购物小程序
# 1.用户启动时先输入工资
# 1.用户启动程序后，打印商品列表；
# 2.允许用户选择购买商品
# 3.允许用户不断的购买各种商品；
# 4.购买时，检测余额是否足够，如果够，直接扣款，否则打印“余额不足”
# 5.允许用户主动退出程序，退出是打印已够列表；


salary=input("请输入工资：")
if salary.isdigit():
    salary=int(salary)
else:
    exit("invalid data type")

welcome_msg="weclome to the shopping mall".center(50,'-')
print(welcome_msg)

exit_flag=False
product_list=[
    ('iphone',5888),
    ('Mac air',8888),
    ('Mac pro',9888),
    ('xiaomi 2',19.9),
    ('coffe',30),
    ('tesla',3000000),
    ('bike',300),
    ('cloth',200),
]

shop_car=[]

while not exit_flag:
    print("product list:".center(50,'#'))
    for index,product in enumerate(product_list):
        print(index,".",product[0],product[1])
    user_choice=input("[q=quit,c=check]select the time to buy:")
    if user_choice.isdigit(): #选择的是商品
        user_choice=int(user_choice)
        if user_choice < len(product_list):
            p_item=product_list[user_choice]
            if p_item[1]<= salary: ##买得起
                shop_car.append(p_item)  #放入购物车
                salary-=p_item[1]  #扣钱
                print("added [%s] into shop car,your current balance is \033[31;1m[%d]\033[0m"%   ##python做颜色格式化的固定格式
                      (p_item,salary))
            else:
                print("your balance is [%s],can not afford this ..."% salary)
    else:
        if user_choice=='q' or user_choice=='quit':
            print("purchased product as below:".center(50,'*'))
            for item in shop_car:
                print(item[0])
            print("END".center(50,'*'))
            print("your balance is \033[41;1m[%d]\0330m"%salary)  ##python做颜色格式化的固定格式
            exit_flag=True

        elif user_choice=='c' or user_choice=='check':
            print("purchased product as below:".center(50,'*'))
            for item in shop_car:
                print(item[0])
            print("END".center(50,'*'))
            print("your balance is [%d]"%salary)



 ##python做颜色格式化的固定格式
# \033[31;1m[%d]\0330m   这是为%d 设置颜色，固定格式：
# 开始为：\033[31;1m
# 结束为：\0330m