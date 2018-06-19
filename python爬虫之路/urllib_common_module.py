#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import random
import urllib.request


##ip 代理池的构建方式1： 适用于 代理IP比较稳定的情况
import random
import urllib.request
ippools=[
    "183.128.240.215:666",
    "117.63.78.37:666",
    "117.63.78.77:66",
]

def ip(ippools):
    thisip=random.choice(ippools)
    print(thisip)
    proxy=urllib.request.ProxyHandler({"http":thisip}) #设置代理IP
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)



##ip 代理池的构建方式2： 适用于 代理IP不稳定的方式， 是通过API接口实时调用的
#需要确认一下接口的访问时间间隔限制，如果有限制，可能会出现问题
def ip_api():
    url='http://tvp.daxiangdaili.com/ip/?tid=123456&num=2&foreign=only'
    thisip=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    print(thisip)
    proxy=urllib.request.ProxyHandler({"http":thisip}) #设置代理IP
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)


##自定义用户代理池
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.5"
]

def ua(uapools):
    '''
    用途：从uapools中随机选取一个user-agent,并绑定为全局
    :param uapools:
    :return :
    '''
    thisua=random.choice(uapools)
    print("Current UA:%s"%thisua)
    headers=("User-Agent",thisua)
    opener=urllib.request.build_opener() #实例化一个opener对象；
    opener.addheaders=[headers]  ##添加头信息
    urllib.request.install_opener(opener)  ##将头信息安装为全局：


def spider_preporcess(url):
    '''
    用途：1. 根据网页的编码格式采用相应的编码格式；
          2. 如果网页采用加密的方式，需要进行相应的解码
    :param url:
    :return page_content:
    '''
    import urllib.request,re

     ##配置全局用户代理
    ua(uapools)
    # ##配置全局代理IP方式1，适用于代理IP稳定的情况
    # ip(ippools)
    # ##配置全局代理IP方式1，适用于代理IP不稳定的情况
    # ip_api()

    obj=urllib.request.urlopen(url)
    info=obj.info()
    # print(type(info))
    ##get chaset info
    pat1='charset=(.*?)\s'
    charsett=re.compile(pat1).findall(str(info))
    print(charsett)
    if charsett:
        if charsett[0]=='GB2312':
            decode_type='gbk'
        else:
            decode_type='utf-8'
    else:
        decode_type='utf-8'
    ##get   Content-Encoding
    pat2='Content-Encoding: (.*?)\s'
    zzip=re.compile(pat2).findall(str(info))
    print(zzip)
    data=urllib.request.urlopen(url).read()
    if zzip: ## page using zip
        if zzip[0]=='gzip':
            import zlib
            decompressed_data = zlib.decompress(data,16+zlib.MAX_WBITS)
            page_content=decompressed_data.decode(decode_type,'ignore')

    else: ##page not using zip
        page_content=data.decode(decode_type,'ignore')
    return page_content

