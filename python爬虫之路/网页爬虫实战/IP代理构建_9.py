#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#IP 代理，即让爬虫使用代理IP去爬取网站；
#http://www.66ip.cn/   IP 代理的免费提取网站
# http://www.xicidaili.com/

#通过API 获取代理IP
import urllib.request
import re
url="http://www.66ip.cn/nmtq.php?getnum=1&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=2&proxytype=2&api=66ip"
data=urllib.request.urlopen(url).read().decode("GBK","ignore")
print(len(data))
urllib.request.urlretrieve(url,"test.html")
pat="(\d{2,3}\..*?)<br"
ret=re.compile(pat).findall(data)
print(ret)