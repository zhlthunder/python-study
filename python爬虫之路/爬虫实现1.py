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
import urllib.request
import re
data=urllib.request.urlopen("http://edu.51cto.com/course/1158.html").read().decode('utf-8')
pat="学习交流群\((\d+)\)"
qq=re.compile(pat).findall(data)
print(qq)