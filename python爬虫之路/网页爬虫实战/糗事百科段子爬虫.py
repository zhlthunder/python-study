#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 自动换页相关
# https://www.qiushibaike.com/8hr/page/10/

# 需要匹配的段子的格式范例：
# <div class="content">
# <span>
#
#
# 新来的同事小李，每天早上总是提前到办公室。把领导办公室的卫生打扫的一尘不染，把领导的杯子刷干净，泡好茶。然后，在用领导的高级茶叶给自己泡上，坐在领导的椅子上享受会……
#
# </span>
#
# </div>

# 代码实现：@@重要：验证一个网站是否需要UA代理
#先验证一下 ，不添加UA 代理是否可以访问
# import  urllib.request
# import re
# url="https://www.qiushibaike.com/"
# urllib.request.urlopen(url)
# 报如下的错误，即做了反爬的限制，需要使用浏览器代理才可以爬取
#     raise RemoteDisconnected("Remote end closed connection without"
# http.client.RemoteDisconnected: Remote end closed connection without response


# @@需求的最终实现：
# 下面通过添加UA代理的方法来爬取：
import urllib.request
import re
##浏览器伪装，添加UA代理
#________________________
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
##将UA代理安装为全局
urllib.request.install_opener(opener)
#_________________________
url="https://www.qiushibaike.com/"
for i in range(0,35):
    print(i)
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

##备注，网站好像做了反扒的手段，爬取多页时会出错，此代码待继续调试 。。。。？
#只爬取5页时，确认没有问题。
