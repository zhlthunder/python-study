#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 数据流的种类：
# 顺序， 选择，循环

##正序输出乘法表：

# for i in range(1,10):
#     for j in range(1,i+1):
#         str="%s*%s=%s "%(i,j,i*j)
#         print(str,end='')
#     print('\n')

##逆序乘法表
for i in range(9,0,-1):
    for j in range(i,0,-1):
        str="%s*%s=%s "%(i,j,i*j)
        print(str,end='')
    print('\n')