#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 利用Python，将多个excel文件合并为一个文件
#
# 思路
# 利用python xlrd包读取excle文件，然后将文件内容存入一个列表中，再利用xlsxwriter将内容写入到一个新的excel文件中。

#将多个Excel文件合并成一个
import xlrd        ##用于读取excel表
import xlsxwriter  ##用于写excel表

#打开一个excel文件
def open_xls(file):
    fh=xlrd.open_workbook(file)
    return fh

#获取excel中所有的sheet表
def getsheet(fh):
    return fh.sheets()

#获取sheet表的行数
def getnrows(fh,sheet):
    table=fh.sheets()[sheet]
    return table.nrows

#读取文件内容并返回行内容
def getFilect(file,shnum):
    fh=open_xls(file)
    table=fh.sheets()[shnum]
    num=table.nrows
    for row in range(num):
        rdata=table.row_values(row)
        datavalue.append(rdata)
    return datavalue

#获取sheet表的个数
def getshnum(fh):
    x=0
    sh=getsheet(fh)
    for sheet in sh:
        x+=1
    return x


if __name__=='__main__':
    #定义要合并的excel文件列表
    allxls=['C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python爬虫之路/实例--用python合并多个excel文件/excel1.xlsx','C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python爬虫之路/实例--用python合并多个excel文件/excel2.xlsx']
    #存储所有读取的结果
    datavalue=[]
    for fl in allxls:
        fh=open_xls(fl)
        x=getshnum(fh)
        for shnum in range(x):
            print("正在读取文件："+str(fl)+"的第"+str(shnum)+"个sheet表的内容...")
            rvalue=getFilect(fl,shnum)
    #定义最终合并后生成的新文件
    endfile='C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python爬虫之路/实例--用python合并多个excel文件/excel3.xlsx'
    wb1=xlsxwriter.Workbook(endfile)
    #创建一个sheet工作对象
    ws=wb1.add_worksheet()
    for a in range(len(rvalue)):
        for b in range(len(rvalue[a])):
            c=rvalue[a][b]
            ws.write(a,b,c)
    wb1.close()
    print("文件合并完成")



