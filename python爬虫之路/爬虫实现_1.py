#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##最简单的爬虫的实现代码
# import urllib.request
# data=urllib.request.urlopen("https://www.csdn.net/").read() ##读取到的是一个文件，需要用read读取
# print(data)

##从网页中提取QQ群
# import urllib.request
# import re
# data=urllib.request.urlopen("http://edu.51cto.com/course/1158.html").read()
# pat="\d{5}"
# qq=re.compile(pat).findall(data)
# 上面的代码报如下的错误：
# TypeError: cannot use a string pattern on a bytes-like object


# 改进的代码：
# import urllib.request
# import re
# data=urllib.request.urlopen("http://edu.51cto.com/course/1158.html").read().decode('utf-8')
# pat="学习交流群\((\d+)\)"
# qq=re.compile(pat).findall(data)
# print(qq)



##作业：从指定完整提取出版社信息，并写入文件中
import urllib.request
import re
import xlsxwriter

data=urllib.request.urlopen("https://read.douban.com/provider/all").read().decode('utf-8')
pat="<div class=\"name\">(.*?)</div>"
ret=re.compile(pat).findall(data)
# print(ret)
#将结果写入excel文件中
endfile='C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python爬虫之路/publisher.xlsx'
wb1=xlsxwriter.Workbook(endfile)
#创建一个sheet工作对象
ws=wb1.add_worksheet()
for a in range(len(ret)):
    c=ret[a]
    b=0
    ws.write(a,b,c)
wb1.close()
print("文件合并完成")


