#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 用户代理池：
# 所谓的用户代理池，即将不同的用户代理组件成为一个池子，随后随机调用
#百度搜索用户代理：http://blog.csdn.net/u012175089/article/details/61199238

import urllib.request
import re
import random
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.5"
]

def ua(uapools):
    thisua=random.choice(uapools)
    print(thisua)
    headers=("User-Agent",thisua)
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)

##下面调用糗事百科爬虫的例子
url="https://www.qiushibaike.com/"
for i in range(0,2):
    ua(uapools)
    thisurl="https://www.qiushibaike.com/8hr/page/"+str(i+1)+"/"
    # print(thisurl)
    data=urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")
    pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
    ret=re.compile(pat,re.S).findall(data) #  re.S表示.号可以匹配换行，即当要匹配的字符串是多行时，需要加上这个修正符
    # print(len(ret))
    # print(ret)
    for j in range(0,len(ret)):
        print(ret[j])
        print("------")

##备注： 这个爬取糗事百科式，也存在报错的问题，待继续排查。。。。。？