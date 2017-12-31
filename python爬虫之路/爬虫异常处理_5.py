#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#异常处理：爬虫在运行过程中，很多时候都会遇到这样活那样的异常。
#我们不希望遇到异常就停止，下次再执行又从头执行，我们希望它可以跳过异常继续执行；

# 常见状态码即含义
# 301: moved permanently ：重定向到新的URL，悠久的
#302： Found  重定向到临时的URL，非永久
#304 not modified: 请求资源未更新
#400： bad request  非法请求
#401 ： unauthorized 请求未经授权
#403 forbidden  禁止访问
#404 not found 没有找到对应页面
#500 inernal server error 服务器内部出现错误
#501 not implemented  服务器不支持实现请求所需要的功能


#URLError HTTPError
# HTTPError 是URLError的子类
# URLError 会返回异常状态码和异常原因；
# URLError 没有异常状态码，所以不能直接代替HTTPError，如果要代替，需要判断是有状态码

# URLError 出现的原因：
# 1）连接不上服务器
# 2）远程的URL不存在
#3）当前无网络
#4）触发了HTTPError


import urllib.request
import urllib.error

try:
    urllib.request.urlopen("http://blog.csdn.net/nav/ai")  #此处的网站没有反爬，需要找到一个反爬的网站再执行一下看看
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)


#爬虫的浏览器伪装技术
# 在我们访问一个网站时，会在请求报文的报头中标准我本地的浏览器的信息，这样在访问的时候，会记录到如下的信息
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36
# 所以，如果我们要伪装成浏览器，那么就需要在访问的时候修改一下报头
# urlopen() 不支持此功能
# 需要引入高级的方法,有如下的两种方法：
# urllib.request.build_opener()
# urllib.request.Request.add_header()

import urllib.request
url="http://blog.csdn.net"
#头文件格式 header=(User-Agent,具体的用户代理值)
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
print(len(data))