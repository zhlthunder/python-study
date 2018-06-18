#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl



# import urllib.request
# res=urllib.request.urlopen('http://www.baidu.com').read().decode('utf-8','ignore')
# print(len(res))
#
# ##参考问题跟踪1， 可以解决遇到的编码问题；


from urllib_common_module import *
import urllib.request
url='http://www.baidu.com'
res=spider_preporcess(url)
print(res)