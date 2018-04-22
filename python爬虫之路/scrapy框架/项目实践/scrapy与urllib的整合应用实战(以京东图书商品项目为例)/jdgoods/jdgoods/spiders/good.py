# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import re
import random
from jdgoods.items import JdgoodsItem
from lxml import etree
from scrapy.http import Request

class GoodSpider(scrapy.Spider):
    name = 'good'
    allowed_domains = ['jd.com']
    #将入口url注释掉，使用入口函数(start_requests)来处理第一次访问的网址
    # start_urls = ['http://jd.com/']

    def start_requests(self):
        ua=[
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
       ]

    #说明，因为UA 代理的有效性的问题，可能需要多次执行后才可以获取一次成功的情况，不要着急。

        req1=urllib.request.Request("https://book.jd.com/")
        req1.add_header("User-Agent",random.choice(ua))
        allpddata=urllib.request.urlopen(req1).read().decode("utf-8","ignore")

        ##说明：因https://book.jd.com/ 源码中，第一级子类不是以html，而是以js的方式提供的，过滤时有问题，后续待继续
        # 研究如何从js中提取url,此次先只以wenxuezongheguan为例来进行介绍；
        print(len(allpddata))
        pat1='"URL":"https:....channel.jd.com..(p_wenxuezongheguan).html","YFLAG":"1"}]'
        allpd=re.compile(pat1).findall(allpddata)
        print(allpd)
        print("11111111")
        catall=[]
        for i in allpd:
            thispd="https://channel.jd.com/"+i+".html"
            req2=urllib.request.Request(thispd)
            req2.add_header("User-Agent",random.choice(ua))
            pddata=urllib.request.urlopen(req2).read().decode("utf-8","ignore")
            # print(len(pddata))
            # print("222222")

            #pat2='href="//list.jd.com/list.html?cat=([0-9,]*?)[&"]'  此次的？必须替换成.，否则无法提取出来内容
            pat2='href="//list.jd.com/list.html.cat=([0-9,]*?)[&"]'
            catdata=re.compile(pat2).findall(pddata)
            for j in catdata:
                catall.append(j)
        print(len(catall))
        # print(catall[0])
        print("333333")
        catall2=set(catall) #使用set()实现去重
        print(len(catall2))

        ##获取每个频道的总页数
        allurl=[] #[{'频道号':"每个频道的总页数"}]
        x=0 ##为了测试，让循环尽快结束
        for m in catall2:
            thispdnum=m
            # print(thispdnum)
            req3=urllib.request.Request("https://list.jd.com/list.html?cat="+str(thispdnum))
            req3.add_header("User-Agent",random.choice(ua))
            listdata=urllib.request.urlopen(req3).read().decode("utf-8","ignore")
            print(len(listdata))
            print("55555")
            pat3="<em>共<b>(.*?)</b>"
            allpage=re.compile(pat3).findall(listdata)
            print(allpage)
            print("444444")
            if(len(allpage)>0):
                pass
            else:
                allpage=[1]
            allurl.append({thispdnum:allpage[0]})

            #为了测试
            if(x>2):
                break
            x+=1

        ##下面依次来爬取各页，提取需要获取的信息
        x=0
        for n in catall2:
            thispage=allurl[x][n]
            for p in range(1,int(thispage)+1):
                thispageurl="https://list.jd.com/list.html?cat="+str(n)+"&page="+str(p)
                print(thispageurl)
                yield Request(thispageurl,callback=self.parse)
            x+=1
            if(x==len(catall2)):
                break


    def parse(self, response):
        #频道1，频道2
        #需要提取的字段：
        #  <span class="curr">小说</span>   对应一级频道
        # <span class="curr">科幻小说</span>  对应二级频道
        pd=response.xpath("//span[@class='curr']/text()").extract()
        if(len(pd)==0):
            pd=["缺省","缺省"]
        if(len(pd)==1):
            pda=pd[0]
            pd=[pda,"缺省"]
        pd1=pd[0]
        pd2=pd[1]
        print(pd1)
        print(pd2)
        ##图书名
