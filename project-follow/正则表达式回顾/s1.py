#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 1.需求：设计一个正则表达式来过滤一个字符串中的10到59
# import re
# pat=r"[1-5][0-9]"
# match=re.findall(pat,'10,20,30,40,50,55,66,88,xy,1x,2y')
# if match:
#     print(match)

#2.需求： 过滤字符串中的只含2个字符的字母，并且第一个字母是大写A或B或C
# import re
# pat=r"[A-C][a-zA-Z]"
# match=re.findall(pat,'xy,1,2,3,4,Az,Cy')
# if match:
#     print(match)

#3.需求：过滤一个字符串中的含有3个字母的独立字符
