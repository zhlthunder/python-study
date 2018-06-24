#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import redis
import pymysql
import urllib.request
import re
import random


rconn=redis.Redis("172.17.0.8","6379") ##连接redisk服务器
#目标url: http://www.17k.com/book/1398783.html
"""
比如redis中存储的信息如下：
url--i--"1"  标识每个网址是否已经被爬取了,存储格式：键名--域名--值
"""

for i in range(0,5459058):
    isdo=rconn.hget("url",str(i))
    if isdo!=None: ##标识此页已经爬取了
        continue
    rconn.hset("url",str(i),"1")  ##数据库写入标识符
    try:
        data=urllib.request.urlopen("http://www.17k.com/book/"+str(i)+".html").read().decode('utf-8','ignore')
    except Exception as err:
        print(str(i)+str(err))
        continue
    pat='<a class="red" .*?>(.*?)</a>'
    rst=re.compile(pat,re.S).findall(data)
    if len(rst)==0:
        continue
    name=rst[0] ##获取小说名
    rconn.hset("rst",str(i),str(name))  ##将小说名存入redis中；


