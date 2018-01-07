#!/usr/bin/env python
#author:zhl

# 需求：将腾讯新闻首页所有新闻都爬到本地
# 思路：先爬首页，通过正则表达式获取所有新闻然后依次爬各新闻，并存储到本地



# 先爬取一个新闻页面测试一下是否可以
# import urllib.request
# import re
# url="http://new.qq.com/omn/20180105C033FU.html"
##浏览器伪装相关
# headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
# opener=urllib.request.build_opener()
# opener.addheaders=[headers]
# data=opener.open(url).read().decode('gbk','ignore')

# data=urllib.request.urlopen(url).read().decode('gbk','ignore')
#说明：
#第二个参数 ignore ，表示即使编码错误，也忽略错误，继续进行编码，避免不必要的中断。
#第一个参数最好参照网页中的 “charset="gbk"” 字段进行设置，否则会出现编码错误
#使用下面的命令来验证网页是否爬取成功
# urllib.request.urlretrieve(url,"test.html")
# print(len(data))


#现在继续完成我们的作业，按照如下的步骤进行
#1.爬取新闻首页
#2.得到各新闻链接
#3.爬取新闻链接
#4.寻找有没有frame, 这种情况下，是一个跳转的网址，需要获取对应的跳转的网址；
#5.若有，抓取frame下对应对应的网页；
#6.若无，直接抓取当前页面；

# import urllib.request
# import re
# url="http://news.qq.com/"

##重要：通过下面的命令确认网页的编码格式和是否压缩，重要
# finfo=urllib.request.urlopen(url)
# print(finfo.info())

# 从输出中得到为  charset=GB2312，必须用gbk编码的方式去读取
# data=urllib.request.urlopen(url).read().decode('GB2312','ignore')
# print(len(data))
# print(data)

##总结，试了各种 格式，包括utf-8, UTF-8(网页源码上查询到的格式)， GB2312( info（）函数中查看的格式)
#总之，试了各种方法，一直报错或下载的数据是乱码，已经崩溃了，最后找到如下的网站的介绍，才解决：因为网页是压缩后的，所以要先解压
# http://blog.csdn.net/hfut_jf/article/details/51276110

# import urllib.request,sys
# def url_info(url):
#     finfo=urllib.request.urlopen(url)
#     print(finfo.info())
#
# url='http://new.qq.com/omn/20180105C033FU.html'
# url_info(url)
# url="http://news.qq.com/"
# url_info(url)
# sys.exit()
# 输出：
# Date: Sat, 06 Jan 2018 13:15:09 GMT
# Content-Type: text/html; charset=GB2312
# Transfer-Encoding: chunked
# Connection: close
# Server: squid/3.5.24
# Vary: Accept-Encoding
# Vary: Accept-Encoding
# Expires: Sat, 06 Jan 2018 13:17:10 GMT
# Cache-Control: max-age=120
# Vary: Accept-Encoding
# Vary: Accept-Encoding
# X-Cache: MISS from shanghai.qq.com
#
#
# Date: Sat, 06 Jan 2018 13:15:09 GMT
# Content-Type: text/html; charset=GB2312
# Transfer-Encoding: chunked
# Connection: close
# Server: squid/3.5.24
# Vary: Accept-Encoding
# Expires: Sat, 06 Jan 2018 13:16:10 GMT
# Cache-Control: max-age=60
# Vary: Accept-Encoding
# Content-Encoding: gzip
# Vary: Accept-Encoding
# X-Cache: HIT from shanghai.qq.com




import urllib.request
import re
import zlib
import sys
url="http://news.qq.com/"
#直接使用下面的一行报错，因为页面是压缩的。 且页面是使用gb2312编码的，所以要用gbk进行解码
# text=urllib.request.urlopen(url).read().decode('gbk')
#报错信息： UnicodeDecodeError: 'gbk' codec can't decode byte 0x8b in position 1: illegal multibyte sequence
##所以需要采用如下的方法，对页面进行解压才可以
data=urllib.request.urlopen(url).read()
decompressed_data = zlib.decompress(data,16+zlib.MAX_WBITS)
text=decompressed_data.decode('gbk')  #因为网页的编码格式是gb2312,所以这里必须用 gbk,如何用 utf-8还是会报错；
print(len(text))

#要匹配的目标字符串 <a target="_blank" class="linkto" href="http://new.qq.com/omn/20180105C033FU.html"
#将目标网址的地方换成 .*?即可
pat='<a target="_blank" class="linkto" href="(.*?)"'
alllink=re.compile(pat).findall(text)
# print(alllink)
print(len(alllink))
for i in range(0,len(alllink)):
    thislink=alllink[i]
    thispage=urllib.request.urlopen(thislink).read().decode("gbk","ignore")
    pat1="<frame src=(.*?)>"
    isframe=re.compile(pat1).findall(thispage)  ##判断是否有跳转的网址，并获取跳转的网址
    print(len(isframe))
    if not len(isframe):
        urllib.request.urlretrieve(thislink,str(i)+".html")
    else:
        flink=isframe[0]
        urllib.request.urlretrieve(flink,str(i)+".html")



