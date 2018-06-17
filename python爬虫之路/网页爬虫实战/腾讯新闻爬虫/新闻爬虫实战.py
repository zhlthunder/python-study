#!/usr/bin/env python
#author:zhl

# 需求：将腾讯新闻首页所有新闻都爬到本地
# 思路：先爬首页，通过正则表达式获取所有新闻然后依次爬各新闻，并存储到本地



# 先爬取一个新闻页面测试一下是否可以爬取
import urllib.request
import re
# url="https://news.qq.com/a/20180616/016127.htm"

##技巧1@@@浏览器伪装的方法：
# headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
# opener=urllib.request.build_opener()
# opener.addheaders=[headers]
# data=opener.open(url).read().decode('utf-8','ignore')
###############

# data=urllib.request.urlopen(url).read().decode("gbk",'ignore')
# ##技巧2@@@  解码相关说明：1. 使用utf-8和 html页面中 的 charset=gb2312 解码时都显示的乱码，使用gbk解码时正常；看来解码方式还是要多尝试压
# print(type(data))
# print(data)


# 技巧3@@@
# data=urllib.request.urlopen(url).read().decode('gbk','ignore')
#说明：
#第二个参数 ignore ，表示即使编码错误，也忽略错误，继续进行编码，避免不必要的中断。
#第一个参数最好参照网页中的 “charset="gbk"” 字段进行设置，否则会出现编码错误
#使用下面的命令来验证网页是否爬取成功
# urllib.request.urlretrieve(url,"test.html")
# print(len(data))




#现在继续完成我们的需求，按照如下的步骤进行
#1.爬取新闻首页
#2.得到各新闻链接
#3.爬取新闻链接
#4.寻找有没有frame, 这种情况下，是一个跳转的网址，需要获取对应的跳转的网址；
#5.若有，抓取frame下对应对应的网页；
#6.若无，直接抓取当前页面；


# # 技巧4@@@##重要：通过下面的命令确认网页的编码格式和是否压缩
# import urllib.request
# import re
# url="http://news.qq.com/"
# finfo=urllib.request.urlopen(url)
# print(finfo.info())
# 输出：
# Date: Sun, 17 Jun 2018 01:47:04 GMT
# Content-Type: text/html; charset=GB2312
# Transfer-Encoding: chunked
# Connection: close
# Server: squid/3.5.24
# Vary: Accept-Encoding
# Expires: Sun, 17 Jun 2018 01:48:04 GMT
# Cache-Control: max-age=60
# Vary: Accept-Encoding
# Content-Encoding: gzip
# Vary: Accept-Encoding
# X-Cache: HIT from shanghai.qq.com
# 从输出中得到为  charset=GB2312，必须用gbk编码的方式去解码
# data=urllib.request.urlopen(url).read().decode('gbk,'ignore')
# print(len(data))
# print(data)


 # 技巧5@@@##重要，另外一种编码错误的处理办法##如果试了各种 格式，包括utf-8, UTF-8(网页源码上查询到的格式)， GB2312( info（）函数中查看的格式)
#总之，试了各种方法，一直报错或下载的数据是乱码，已经崩溃了，最后找到如下的网站的介绍，才解决：因为网页是压缩后的，所以要先解压
# http://blog.csdn.net/hfut_jf/article/details/51276110
##实例如下：
# import urllib.request,sys
# def url_info(url):
#     finfo=urllib.request.urlopen(url)
#     print(finfo.info())
# url='http://new.qq.com/omn/20180105C033FU.html'
# url_info(url)
# url="http://news.qq.com/"
# url_info(url)
# data=urllib.request.urlopen(url).read().decode('gbk','ignore')
# print(data)
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


##应用页面解码判断的实例：
# import urllib.request
# import re
# import zlib
# import sys
# url="http://news.qq.com/"
# data=urllib.request.urlopen(url).read()
# decompressed_data = zlib.decompress(data,16+zlib.MAX_WBITS)
# text=decompressed_data.decode('gbk')  #因为网页的编码格式是gb2312,所以这里必须用 gbk,如何用 utf-8还是会报错；
# print(text)


#最终结论，编制一个函数，判断网页是否采用加密的方法，已经采用的编码算法，并采用相应的方法进行处理的通用子函数
##通用函数1
def spider_preporcess(url):
    import urllib.request,re
    obj=urllib.request.urlopen(url)
    info=obj.info()
    # print(type(info))
    ##get chaset info
    pat1='charset=(.*?)\s'
    charsett=re.compile(pat1).findall(str(info))
    print(charsett)
    if charsett[0]=='GB2312':
        decode_type='gbk'
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



##通用函数2： 应用浏览器伪装技术
def agent(url):
    import urllib.request
    headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    data=opener.open(url).read().decode('utf-8','ignore')
    return data

# url="http://news.qq.com/"  ##压缩网页
# # url='http://new.qq.com/omn/20180105C033FU.html'  #非压缩网页
# ret=spider_preporcess(url)
# print(ret)







##最后来完成我们的新闻爬虫需求：
url="http://news.qq.com/"
ret=spider_preporcess(url)
print(len(ret))
#要匹配的目标字符串 <a target="_blank" class="linkto" href="https://news.qq.com/a/20180616/000493.htm">
#将目标网址的地方换成 .*?即可
pat='<a target="_blank" class="linkto" href="(.*?)">'
alllink=re.compile(pat).findall(ret)
# print(alllink)
print(len(alllink))
for i in range(0,len(alllink)):
    thislink=alllink[i]
    # thispage=urllib.request.urlopen(thislink).read().decode("utf-8","ignore")
    thispage=spider_preporcess(thislink)
    pat1="<frame src=(.*?)>"
    isframe=re.compile(pat1).findall(thispage)  ##判断是否有跳转的网址，并获取跳转的网址
    print(len(isframe))
    if not len(isframe):
        data=spider_preporcess(thislink)
        # urllib.request.urlretrieve(thislink,str(i)+".html")  ##直接使用retrieve会出现乱码，原因待继续确认，先不用这种方法
        fp=open(str(i)+".html",'w')
        fp.write(data)
        fp.close()
    else:
        flink=isframe[0]
        data=spider_preporcess(flink)
        # urllib.request.urlretrieve(flink,str(i)+".html")##直接使用retrieve会出现乱码，原因待继续确认，先不用这种方法
        fp=open(str(i)+".html",'w')
        fp.write(data)
        fp.close()
    if i==5:
        break



