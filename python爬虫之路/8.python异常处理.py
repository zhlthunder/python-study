#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 异常处理格式
'''
try:
    程序
except Exception as 异常名称：
    异常处理部分
'''

#type 1:到出错的位置停止了
try:
    for i in range(10):
        print(i)
        if(i==4):
            print(jkk)
    print("end")
except Exception as err:
    print(err)

# 输出：
# 0
# 1
# 2
# 3
# 4
# name 'jkk' is not defined

# type2:异常发生后，程序继续执行

for i in range(10):
    try:
        print(i)
        if(i==4):
            print(jkk)
    except Exception as err:
        print(err)
print("end")

# 输出：
# 0
# 1
# 2
# 3
# 4
# name 'jkk' is not defined
# 5
# 6
# 7
# 8
# 9
# end