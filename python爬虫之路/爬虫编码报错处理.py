#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# http://blog.csdn.net/jim7424994/article/details/22675759

# import urllib.request
# res=urllib.request.urlopen('http://www.baidu.com')
# htmlBytes=res.read()
# print(htmlBytes.decode('utf-8'))


import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码
res=urllib.request.urlopen('http://www.baidu.com')
htmlBytes=res.read()
print(htmlBytes.decode('utf-8'))