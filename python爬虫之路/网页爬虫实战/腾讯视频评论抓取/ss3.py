#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


##获取全部评论的内容
import  urllib.request
import re
vid="1743283224"
cid='6234007573961970622'
num="20"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
         "Content-Type":"text/html;charset=utf-8"}
opener=urllib.request.build_opener()
headall=[]
for key,value in headers.items():
    headall.append((key,value))
opener.addheaders=headall
urllib.request.install_opener(opener)
##爬取当前评论页面

for j in range(0,10):
    print("第"+str(j)+"页")
    thisurl="https://video.coral.qq.com/varticle/"+vid+"/comment/v2?cursor="+cid
    ##关键点：每点一次加载更多，会使用当前页面中的commentid 来构成下一页的URL
    data=urllib.request.urlopen(thisurl).read().decode('utf-8','ignore')  ##获取的data都是unicode的编码
    commentpat='"content":"(.*?)"'
    lastpat='"last":"(.*?)"'
    commentall=re.compile(commentpat,re.S).findall(data)
    cid=re.compile(lastpat,re.S).findall(data)[0]  ##此处用于获取下一页对应的cid
    for i in range(0,len(commentall)):
        try:
            print("评论内容是："+eval('u"'+commentall[i]+'"'))
            print("-----------------------")
        except Exception as err:
            print(err)
