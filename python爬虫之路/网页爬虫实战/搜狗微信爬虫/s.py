#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import  urllib.request
import re

keyword='python'
keyword=urllib.request.quote(keyword)
for i in range(1,5):
    thisurl='http://gzh.sogou.com/weixin?query='+keyword+'&type=2&page='+str(i)+'&ie=utf81'
    thispage=urllib.request.urlopen(thisurl).read().decode('utf-8','ignore')
    pat='<div class="txt-box">.*?href="(.*?)"'
    linklist=re.compile(pat,re.S).findall(thispage)
    for j in range(0,len(linklist)):
        # print(linklist[j])
        pat2='amp;'
        temp=linklist[j].replace(pat2,'')
        urllib.request.urlretrieve(temp,str(i)+str(j)+'.html')