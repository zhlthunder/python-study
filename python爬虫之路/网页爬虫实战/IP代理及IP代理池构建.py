#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#IP 代理，即让爬虫使用代理IP去爬取网站；

##1：代理IP的获取方式
#http://daxiangdaili.com/ 商用，建议用这个
# http://www.xicidaili.com/  ，测试用，建议用这个

#此处以http://daxiangdaili.com/  为例进行介绍
"""
在首页，需要登录后才可以使用， 点击“提取IP”打开相应的代理IP的提取页面或通过API提取
总结一下：
1.通过页面上提交请求获取
2.通过API提交获取：比如 http://tvp.daxiangdaili.com/ip/?tid=123456&num=2
==>
基于上面的两种方式，所以代理IP池的构建也相应的有两种方式：
1.已经获取代理IP的情况下，直接构建；
2.通过API调用动态获取并构建的方式
"""


#通过API 获取代理IP
# import urllib.request
# import re
# url="http://www.66ip.cn/nmtq.php?getnum=1&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=2&proxytype=2&api=66ip"
# data=urllib.request.urlopen(url).read().decode("GBK","ignore")
# print(len(data))
# # urllib.request.urlretrieve(url,"test.html")
# pat="(\d{2,3}\..*?)<br"
# ret=re.compile(pat).findall(data)
# print(ret)


#IP代理的构建：
#目的： 在对方看来，你就不是使用自己的IP去访问对方，而是使用代理IP访问对方，是一种避免被屏蔽的有效的方法
# import urllib.request
#
# #采用第一种方式（已知代理IP的情况下）构建代理IP
# ip='122.114.31.177:808' #代理IP
# ##代理IP配置，并安装为全局
# #————————————————————————
# proxy=urllib.request.ProxyHandler({"http":ip})  ##将代理IP封装成一个对象的格式
# # print(proxy)
# opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)
# #————————————————————————
# url="http://www.baidu.com"
# data1=urllib.request.urlopen(url).read()
# data=data1.decode("gbk","ignore")
# # print(data)
# print(len(data))
# fh=open("test.html","w")
# fh.write(data)
# fh.close()




##ip 代理池的构建方式1： 适用于 代理IP比较稳定的情况
# import random
# import urllib.request
# ippools=[
#     "123.57.207.2:3128",
#     # "117.63.78.37:666",
#     # "117.63.78.77:66",
# ]
#
# def ip(ippools):
#     thisip=random.choice(ippools)
#     print(thisip)
#     proxy=urllib.request.ProxyHandler({"http":thisip}) #设置代理IP
#     opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
#     urllib.request.install_opener(opener)
#     print("finished")


###################################################################
##ip 代理池的构建方式2： 适用于 代理IP不稳定的方式， 是通过API接口实时调用的
#需要确认一下接口的访问时间间隔限制，如果有限制，可能会出现问题
import urllib.request
def ip_api():
    url='http://tvp.daxiangdaili.com/ip/?tid=123456&num=2&foreign=only'
    thisip=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    print(thisip)
    proxy=urllib.request.ProxyHandler({"http":thisip}) #设置代理IP
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)




###################################################################
##IP代理池构建的改进的方法，一次提取多个; 但下面的代码流程设计不是很高明，待摸索更好的方法；
import urllib.request
def ip_api_modify():
    url='http://tvp.daxiangdaili.com/ip/?tid=123456&num=2&foreign=only'
    ippools=[]
    ip_list=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    for thisip in ip_list:
        print(thisip.decode('utf-8','ignore'))
        ippools.append(thisip.decode('utf-8','ignore'))
    return ippools




def ip_proxy(ippools,time):
    thisip=ippools[time]
    proxy=urllib.request.ProxyHandler({"http":thisip}) #设置代理IP
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)


# 改进的IP构建方法如何调用：
x=0
for i in range(0,35):
    try:
        if x%10==0:
            ippool=ip_api_modify()
            ip_proxy(ippool,x%10)
        else:
            ip_proxy(ippool,x%10)
    except Exception as err:
        print(err)

###################################################################

###################################################################
# 改进方法：同时使用用户代理池和IP代理池的方法：
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.5"
]


import urllib.request
import random
def ip_api_modify():
    url='http://tvp.daxiangdaili.com/ip/?tid=123456&num=2&foreign=only'
    ippools=[]
    ip_list=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    for thisip in ip_list:
        print(thisip.decode('utf-8','ignore'))
        ippools.append(thisip.decode('utf-8','ignore'))
    return ippools




def ip_proxy(ippools,time,pools):
    thisip=ippools[time]
    ua=random.choice(pools)
    headers=("User-Agent",ua)
    proxy=urllib.request.ProxyHandler({"http":thisip}) #设置代理IP
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)


# 改进的IP构建方法如何调用：
x=0
for i in range(0,35):
    try:
        if x%10==0:
            ippool=ip_api_modify()
            ip_proxy(ippool,x%10,uapools)
        else:
            ip_proxy(ippool,x%10,uapools)
    except Exception as err:
        print(err)
###################################################################