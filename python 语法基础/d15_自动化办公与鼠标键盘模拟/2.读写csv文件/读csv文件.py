#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
#参考： https://www.cnblogs.com/unnameable/p/7366437.html
##报错解决办法： https://blog.csdn.net/stone9159/article/details/79038629

import csv

def readcsv(path):
    with open(path,encoding="utf-8") as f:
        allfileinfo=csv.reader(f)
        print(allfileinfo)
        # for line in allfileinfo:
        #     print(line)
        inlist=list(allfileinfo)
        return inlist


path=r'C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 语法基础\d15_自动化办公与鼠标键盘模拟\2.读写csv文件\aa.csv'
ret=readcsv(path)
print(ret)


# ##返回的数据格式：
# [['按时发达发顺丰'], ['按时发达发顺丰'], ['按时发达发顺丰'], ['按时发达发顺丰'], ['按时发达发顺丰'], ['按时发达发顺丰'], ['按时发达发顺丰'], ['按时发达发顺丰'], ['按时发达发顺丰'], ['按时发达发顺丰']]
