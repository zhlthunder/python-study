#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import csv

def writecsv(path,data):
    with open(path,"w") as f:
        writer=csv.writer(f)
        for row in data:
            writer.writerow(row)


path=r'C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 语法基础\d15_自动化办公与鼠标键盘模拟\2.读写csv文件\bb.csv'
writecsv(path,[[1,2,3],[4,5,6],[7,8,9]])

