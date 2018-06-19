#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


import urllib.request
import re
keyword="连衣裙"  ##不同商品，只修改这里就可以把所有的商品的图片下载到本地
keyword=urllib.request.quote(keyword)
for i in range(1,35):
    thisurl='https://s.taobao.com/search?q='+keyword+'&s='+str((i-1)*44)
    thispage=urllib.request.urlopen(thisurl).read().decode('utf-8','ignore')
    pat='"pic_url":"//(.*?)"'
    piclist=re.compile(pat).findall(thispage)
    # print(piclist)
    for j in range(0,len(piclist)):
        urllib.request.urlretrieve('http://'+piclist[j],str(i)+str(j)+'.jpg')
