#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##本节作业：计算器
#作业需求分析：
#比如表达式为 8-3*3+(3*5+(6/8))+(2=5)/8
# 1.从前往后找，找到第一个 括号开头，括号结尾，中间不包含括号的
#2，\(中间不包含括号)\

# def 处理加减乘除(表达式):
#     pass
# def 处理括号(表达式):
#     while true:
#         re.split("\((中间不包含括号)\)",表达式,1)  ##每次只找满足要求的第一个括号内部的内容
#         tt=处理加减乘除(匹配)
#         用tt替换上面的表达式，继续去寻找下一个满足要求的括号

##下面的这个脚本待解决的问题：---遗留问题
#1.除法得到小数怎么弄？
#2. 2-（7-98）=2--2 错误，如何处理成 2-（-2），进而处理成2+2

import re
import time

def basic_computer(arg):
    ret=eval(arg)
    return ret

def process_str(arg):
    while True:
        ret=re.split("\(([^()]*)\)",arg,1)
        if ret[0]==arg:
            rr=basic_computer(ret[0])
            return rr
        else:
            # print(ret[1])
            rr=basic_computer(ret[1])
            # print(rr,type(rr))
            arg=re.sub("\(([^()]*)\)",str(rr),arg,1)
            print(arg)
            time.sleep(1)



if __name__=="__main__":
    # ss="(1+2)+(2+2)"
    ss="1+2-(3/3-2+(9-8))+4-(9-2)"
    rt=process_str(ss)
    print(rt)

# 输出：
# 1+2-(3/3-2+1)+4-(9-2)
# 1+2-0.0+4-(9-2)
# 1+2-0.0+4-7
# 0.0


#
# ss="1+2-(4/3-2+(9-8))+4-(2-9)"
# ret=eval("9-8")
# # ret=str(ret)
# # print(type(ret),ret)
#
# cc=re.sub("\(([^()]*)\)",str(ret),ss)
# print(cc)
