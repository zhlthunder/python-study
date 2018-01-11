#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#IP 代理，即让爬虫使用代理IP去爬取网站；
#http://www.66ip.cn/   IP 代理的免费提取网站
# http://www.xicidaili.com/

#通过API 获取代理IP
# import urllib.request
# import re
# url="http://www.66ip.cn/nmtq.php?getnum=1&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=2&proxytype=2&api=66ip"
# data=urllib.request.urlopen(url).read().decode("GBK","ignore")
# print(len(data))
# urllib.request.urlretrieve(url,"test.html")
# pat="(\d{2,3}\..*?)<br"
# ret=re.compile(pat).findall(data)
# print(ret)


#IP代理的构建：
#目的： 在对方看来，你就不是使用自己的IP去访问对方，而是使用代理IP访问对方，是一种避免被屏蔽的有效的方法
import urllib.request
# ip='122.114.31.177:808' #代理IP
# ##代理IP配置，并安装为全局
# #————————————————————————
# proxy=urllib.request.ProxyHandler({"http":ip})  ##将代理IP封装成一个对象的格式
# # print(proxy)
# opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)
#————————————————————————
url="http://www.baidu.com"
data1=urllib.request.urlopen(url).read()
data=data1.decode("GBK","ignore")
# print(data)
print(len(data))
fh=open("test.html","w")
fh.write(data)
fh.close()

