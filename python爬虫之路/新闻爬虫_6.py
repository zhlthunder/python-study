#!/usr/bin/env python
#author:zhl

# 需求：将腾讯新闻首页所有新闻都爬到本地
# 思路：先爬首页，通过正则表达式获取所有新闻然后依次爬各新闻，并存储到本地


import urllib.request
import re
data=urllib.request.urlopen("http://www.baidu.com").read()
print(len(data))
urllib.request.urlretrieve("http://www.baidu.com","test.html")

