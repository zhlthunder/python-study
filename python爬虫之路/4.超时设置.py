#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

'''
由于网络速度或对方服务器的问题，我们爬取一个网页的时候，都需要时间。我们访问一个网页，如果该网页长时间未响应，
那么我们的系统就会判断该网页超时了，即无法打开网页。
所以需要根据不同的网页的访问速度，来设置合适的timeout时间，兼顾效率和可用性

'''

import urllib.request
for i in range(0,100):
    try:
        data=urllib.request.urlopen("http://yum.iqianyue.com",timeout=1).read().decode('utf-8')  ##设置超时时间为1s
        print(len(data))
    except Exception as err:
        print("出现异常")

# 备注：循环多次访问时，有时会出现异常，这时可以通过调整timeout来进行