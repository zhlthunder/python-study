#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#自动模拟http请求：
#客户端如果要与服务器端进行通信，需要通过http请求进行，http请求有很多种，我们在此会将Post和get两种请求方式。
# 比如登录，搜索某些信息的时候会用到。

#构造get请求的格式，大概格式如下：
# https://www.baidu.com/s?wd=zhuhong

##实例
import urllib.request
import re
keyword="Python"
url="https://www.baidu.com/s?wd="+keyword
file=urllib.request.urlopen(url).read().decode('utf-8')
pat='title="(.*?)"'
ret=re.compile(pat).findall(file)
print(ret)



