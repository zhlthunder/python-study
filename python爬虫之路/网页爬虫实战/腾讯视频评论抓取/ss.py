#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


##单页深度评论
import  urllib.request
import re
vid="j6cgzhtkuonf6te"
cid='6227734628246412645'
num="20"
url="https://video.coral.qq.com/filmreviewr/c/upcomment/"+vid+"?commentid="+cid+"&reqnum="+num
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
         "Content-Type":"text/html;charset=utf-8"}
opener=urllib.request.build_opener()
headall=[]
for key,value in headers.items():
    headall.append((key,value))
opener.addheaders=headall
urllib.request.install_opener(opener)
##爬取当前评论页面
data=urllib.request.urlopen(url).read().decode('utf-8','ignore')  ##获取的data都是unicode的编码
titlepat='"title":"(.*?)"'
commentpat='"content":"(.*?)"'
titleall=re.compile(titlepat,re.S).findall(data)
commentall=re.compile(commentpat,re.S).findall(data)
for i in range(0,len(titleall)):
    try:
        print("评论标题是："+eval('u"'+titleall[i]+'"'))
        print("评论内容是："+eval('u"'+commentall[i]+'"'))
        print("-----------------------")
    except Exception as err:
        print(err)
