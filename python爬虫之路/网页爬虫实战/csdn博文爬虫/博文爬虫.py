#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import urllib.request
import re
url='https://blog.csdn.net/'
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
##安装为全局：
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
pat=' <h2>.*?<a href="(.*?)" target="_blank" data-track-click=.*?>.*?</a>.*?</h2>'
alllink=re.compile(pat,re.S).findall(data)
# print(alllink)
for i in range(0,len(alllink)):
    thislink=alllink[i]
    urllib.request.urlretrieve(thislink,str(i)+'.html')
