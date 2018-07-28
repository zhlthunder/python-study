#!/usr/bin/env python
# -*- coding: utf-8 -*-

##正则表达式基础
import re
#普通字符作为原子
# stt="taoyunjiaoyu"
# pat='yun'
# ret=re.search(pat, stt)
# print(ret)

#非打印字符作为原子
# stt="""taoyunjiaoyu
# aa77
# """
# pat='\n'
# ret=re.search(pat, stt)
# print(ret)

##通用字符作为原子
# """
# \w  字母 数字 下划线
# \W 非字母 数字 下划线
# \d十进制数
# \D  非十进制数
# \s 空白字符
# \S 非空白字符
#
# """

#
# stt="taoy$7aunjiaoy 7u"
# pat='y\S'
# ret=re.search(pat, stt)
# print(ret)

##原子表
# [xyz]
# [^xyz]
# stt="taoyunjiaoyq"
# pat='y[^xyu]'
# ret=re.search(pat, stt)
# print(ret)


元字符：
##有特殊作用的字符称为元字符
# . 匹配换行符以外的任意字符
# ^匹配行首
# $匹配行尾
# *
# +
# ？
# {n}
# {n,m}
# {n,}
# |
# ()



# stt="taoyun777jioayu"
# pat='yunn|777'
# ret=re.search(pat, stt)
# print(ret)

#模式修正符
# re.I  忽略大小写
# re.S  让.可以匹配换行符
# re.M  匹配多行

# stt="""Taoyunjiaoyu77
# 66
# aa
# """
# pat=''
# ret=re.search(pat,stt,re.S)
# print(ret)

#正则匹配函数
match（）
search()
findall()

# stt="taoyun777jiotaoayu"
# pat='tao'
# ret=re.compile(pat).findall(stt)
# print(ret)


网址匹配
# str="href=http://www.baidu.com,http://sohu.cn"
# pat='[a-zA-Z]+://[^\s]*[.com|.cn]'
# ret=re.compile(pat).findall(str)
# print(ret)


电话号码匹配
# str="aasfdasdf025-78787878,ppppp0527-8787878"
# pat='\d{3}-\d{8}|\d{4}-\d{7}'
# ret=re.compile(pat).findall(str)
# print(ret)



#说明：
python2 ：有urllib, urllib2
python3: 只有urllib  (重新整合了python2中的urllib, urllib2的功能)


#chapter 2
#爬虫基本用法
# import urllib.request
# import re
# data=urllib.request.urlopen("http://128.1.2.250/asset_db_show/").read().decode('utf-8','ignore')
# pat='\d{4}'
# ret=re.compile(pat).findall(data)
# print(ret)


##基础功能函数
# urlopen() 打开一个网页的方法
# urlretrieve (网址，本地存储文件) 直接下载网页到本地
# urlcleanup() 清空系统缓存用
##先执行urllib.request.urlopen(url), 然后对这个对象再执行下面的方法：
# info() 查询爬取页面的简介信息
#getcode() 获取状态码
#geturl() 获取url




# import  urllib.request
# import os
# data=urllib.request.urlopen("http://128.1.2.250/asset_db_show/")
# print(data.info())
# print(data.getcode())
# dir='C:\cmdb'
# # print(dir)
# dir=os.path.join(dir,'test.html')
# urllib.request.urlretrieve("http://128.1.2.250/asset_db_show/",dir)
# urllib.request.urlcleanup()


##超时设置：timeout 参数
##urlopen 可以设置timeout, 可以根据不同网站的访问速度，设置合适的timeout
# import urllib.request
# data=urllib.request.urlopen("http://128.1.2.250/asset_db_show/",timeout=1).read().decode('utf-8','ignore')
# print(data)



##自动模拟http请求
#客户端如果要与服务器进行通信，需要通过http请求进行，http请求有很多种，比如get, post
#get 请求
# http://www.baidu.com/s?wd=python


##通过python模块实现http请求的方法
#使用urllib模块
# 1.简单的get请求
# import urllib.request
# data=urllib.request.urlopen("http://128.1.2.250/asset_db_show/").read().decode('utf-8','ignore')
# print(data)

#2.通过Request()对象发送get请求的方式：
# import urllib.request
# req=urllib.request.Request("http://128.1.2.250/asset_db_show/")
# data=urllib.request.urlopen(req).read().decode('utf-8')
# print(data)


#3.带参数的get请求
# import urllib.request
# key="测试"
# key=urllib.request.quote(key) ##因为URL中不可以包含中文，如果关键字是中文，需要调用这个方法对中文字符进行转码才可以
# url='http://www.baidu.com/s?wd='+key
# data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
# print(data)


#4.post请求
# import  urllib.request
# import urllib.parse
# posturl='http://www.baidu.com/mypost'
# postdata=urllib.parse.urlencode({
#     'name':'jack',
#     'pass':'123'
# }).encode('utf-8')
# req=urllib.request.Request(posturl,postdata) ##封装请求对象， 这是通过对象的方法来发送请求
# data=urllib.request.urlopen(req).read().decode("utf-8")
# print(data)


补充：
#使用urllib2模块, with python2.7
# 1.get方法
# import urllib2
# data=urllib2.urlopen('http://128.1.2.250/asset_db_show/').read()
# print(data)

#2. get方法，使用对象：
# import urllib2
# req=urllib2.Request('http://128.1.2.250/asset_db_show/')
# data=urllib2.urlopen(req).read()
# print(data)

#3.post请求
# import urllib2,json
# data={"ip_addr": "7.4.4.5"}
# url="http://128.1.2.250/asset/api/v1.0/r57005577/update"
# ddata=json.dumps(data)
# header_dict={'Content-Type':"application/json"}
# req = urllib2.Request(url=url,data=ddata,headers=header_dict)
# res_data = urllib2.urlopen(req).read()
# print(res_data)

#总结： urlib和urlib2的区别：可以简单认为是：把urlib.request 封装成 urlib2




# 爬虫的浏览器伪装的两种方法
# urllib.request.build_opener()  ##此处主要介绍这种方法
# urllib.request.Request.add_header()



#用户代理构建：
# import urllib.request
# url="http://www.baidu.com"
# headers=('User-Agent','IE10.2')
# opener=urllib.request.build_opener()
# opener.addheaders=[headers]
# data=opener.open(url).read()



##用户代理池的构建
# import urllib.request
# import re
# import random
#
# uapools=[
#     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; rv:59.0) Gecko/20100101 Firefox/59.0",
# ]
#
# def user_agent(pools):
#     ua=random.choice(pools)
#     print(ua)
#     headers=('User-Agent',ua)
#     opener=urllib.request.build_opener()
#     opener.addheaders=[headers]
#     urllib.request.install_opener(opener)

#调用方法
# url='http://128.1.2.250/asset_db_show/'
# user_agent(uapools)
# data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
# print(data)


#代理IP构建
import urllib.request
ip='128.1.2.250:80'
proxy=urllib.request.ProxyHandler({"http":ip})
opener=urllib.request.build_opener(proxy,urllib.request.ProxyHandler)
urllib.request.install_opener(opener)


##同时使用IP代理和UA代理
import urllib.request
import random
uapools=[
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; rv:59.0) Gecko/20100101 Firefox/59.0",
]
ip="128.1.2.250:80"
##构建IP代理
proxy=urllib.request.ProxyHandler({"http":ip})
opener=urllib.request.build_opener(proxy,urllib.request.ProxyHandler)
##构建UA代理
ua=random.choice(uapools)
headers=('User-Agent',ua)
opener.addheaders=[headers]
urllib.request.install_opener(opener)

url='http://128.1.2.250/asset_db_show/'
data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
print(data)



#xpath表达式
"""
对比：
xpath :效率高
正则表达式： 功能强大
==》故：优先选择xpath表达式，xpath解决不了的时候，就用正则表达式

xpath常用的语法：
/ 逐层提取
text() 取标签下面的文本
//标签名**  取所有标签名为**的标签
//标签名**[@属性名=‘属性值’]  提取某个属性名为特定值的所有特定标签
@属性名  代表取某个属性值

实例：
取标题：/html/head/title/text()
提取所有的div标签 //div
提取class="tool"的div 标签  //div[@class='tool']
"""


##如果在urllib中使用xpath来进行信息的提取，此时，你需要先安装 lxml模块，然后将网页数据通过lxml下的etree转化为treedata的形式
# 重要：python3.5及以上，在从lxml导入etree时会提示“红色波浪线”，直接忽略，不影响正常的使用

# 使用方式1： etree有波浪线，且etree.cp36-win32.pyd 这个文件一定要和平台保持一致（32系统上对应win32,64位系统上对应位amd64，但是在在lxml模块安装时自动生成的），否则无法执行
import urllib.request
from lxml import etree

data=urllib.request.urlopen('http://128.1.2.250/asset_db_show/').read().decode('utf-8','ignore')
print(data)
treedata=etree.HTML(data)
title=treedata.xpath("//title/text()")

#使用方式2：避免 etree有波浪线，但etree.cp36-win32.pyd 这个文件一定要和平台保持一致（32系统上对应win32,64位系统上对应位amd64，但是在在lxml模块安装时自动生成的），否则无法执行
from lxml import html
page_source='''
<html>
<a>link</a>
</html>
'''
# page=html.etree.HTML(page_source)
ret=page.xpath("/html/a/text()")
print(ret)






