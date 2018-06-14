#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


import urllib.request

##urlopen 打开一个网页的方法
# urllib.request.urlopen("http://www.baidu.com")

#urlretrieve(网址，本地存储的文件) :直接下载文件到本地
# urllib.request.urlretrieve("https://www.zhibo8.cc/","C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python爬虫之路/download.html")

# urlcleanup()  ##用来清除系统缓存用的
# urllib.request.urlcleanup()

#info() 查询爬取的页面的简介信息
# data=urllib.request.urlopen("https://read.douban.com/provider/all")
# print(data.info())
# 输出：
# Date: Sun, 31 Dec 2017 01:49:00 GMT
# Content-Type: text/html; charset=utf-8
# Content-Length: 61854
# Connection: close
# Vary: Accept-Encoding
# Expires: Sun, 1 Jan 2006 01:00:00 GMT
# Pragma: no-cache
# Cache-Control: must-revalidate, no-cache, private
# Set-Cookie: profile="deleted"; max-age=0; domain=read.douban.com; expires=Thu, 01-Jan-1970 00:00:00 GMT; path=/
# Set-Cookie: bid=U02r5h3gAEg; Expires=Mon, 31-Dec-18 01:49:00 GMT; Domain=.douban.com; Path=/
# X-DOUBAN-NEWBID: U02r5h3gAEg
# X-DAE-Node: sindar5d
# X-DAE-App: ark
# Server: dae
# Strict-Transport-Security: max-age=15552000;
# X-Content-Type-Options: nosniff


##getcode() 返回网页爬取操作的状态码
# data=urllib.request.urlopen("https://read.douban.com/provider/all")
# print(data.getcode())
# 输出：
# 200


##geturl() 获取当前访问的页面的URL
data=urllib.request.urlopen("https://read.douban.com/provider/all")
print(data.geturl())
# 输出：
# https://read.douban.com/provider/all






