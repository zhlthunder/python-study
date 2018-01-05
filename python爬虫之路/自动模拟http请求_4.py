#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#自动模拟http请求：
#客户端如果要与服务器端进行通信，需要通过http请求进行，http请求有很多种，我们在此会介绍Post和get两种请求方式。
# 比如登录，搜索某些信息的时候会用到。

##自动get请求实践

#构造get请求的格式，大概格式如下：
# https://www.baidu.com/s?wd=zhuhong


# import urllib.request
# import re
# keyword="Python"
# url="http://www.baidu.com/s?wd="+keyword
# file=urllib.request.urlopen(url).read().decode('utf-8')
# print(len(file))
# pat="title:'Python_百度百科"
# ret=re.compile(pat).findall(file)
# print(ret)


##中文的搜索方式：
# import urllib.request
# import re
# keyword="微微"
# keyword=urllib.request.quote(keyword)  ##对于中文，需要进行编码格式的转换，否则会报错
# url="http://www.baidu.com/s?wd="+keyword
# file=urllib.request.urlopen(url).read().decode('utf-8')
# pat='{"title":(.*?),'
# ret=re.compile(pat).findall(file)
# print(ret)



##如何实现搜索多页
# import urllib.request
# import re
# keyword="python"
# for i in range(1,5):
#     url="http://www.baidu.com/s?wd="+keyword+"&pn="+str((i-1)*10)
#     file=urllib.request.urlopen(url).read().decode('utf-8')
#     pat='{"title":(.*?),'
#     ret=re.compile(pat).findall(file)
#     for j in range(0,len(ret)):
#         print(ret[j])


##自动POST请求实践
# 使用一个测试页面来进行测试：http://www.iqianyue.com/mypost
import urllib.request
import urllib.parse
posturl="http://www.iqianyue.com/mypost"
postdata=urllib.parse.urlencode({
    "name":"testname",
    "pass":"testpass"
}).encode('utf-8')
#进行post,就需要使用urllib.request下面的request（真实post地址，post数据）
req=urllib.request.Request(posturl,postdata)  ##提交post请求，返回提交后的URL地址；
data=urllib.request.urlopen(req).read().decode('utf-8')  ##打开已经进行post提交后的页面
print(data)
