# -*- coding: utf-8 -*-
import scrapy,re
from baidunews.items import BaidunewsItem
from scrapy.http import Request

class N1Spider(scrapy.Spider):
    name = 'n1'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']
    # start_urls = ['http://news.baidu.com/widget?id=LocalNews&ajax=json']

    allid=['LocalNews', 'LocalNews', 'civilnews', 'InternationalNews', 'EnterNews', 'SportNews', 'FinanceNews', 'TechNews', 'MilitaryNews', 'InternetNews', 'DiscoveryNews', 'LadyNews', 'HealthNews', 'PicWall']
    allurl=[]
    ##在for循环中构造所有的栏目的url
    for k in range(0,len(allid)):
        thisid=allid[k]
        thisurl="http://news.baidu.com/widget?id="+thisid+"&ajax=json"
        allurl.append(thisurl)
        # print(allurl)

    ##parse中遍历每个栏目的url,然后通过yield提交请求，并指定next来处理响应
    def parse(self,response):
        for m in range(0,len(self.allurl)):
            print("第"+str(m)+"个栏目")
            yield Request(self.allurl[m],callback=self.next)
    ##，需要在parse函数中配置一个while循环，使用time.sleep()函数来控制延时；

    ##next函数中解析没有栏目的js数据，从中提取中每个新闻的url,
    def next(self, response):
        data=response.body.decode("utf-8","ignore")
        pat1='"url":"(.*?)"'
        pat2='"m_relate_url":"(.*?)"'
        url1=re.compile(pat1,re.S).findall(data)
        url2=re.compile(pat2,re.S).findall(data)
        if(len(url1)!=0):
            url=url1
        else:
            url=url2
        # print(url)
        for i in range(0,len(url)):
            # print(url[i])
            ###url address transfer
            thisurl=re.sub("\\\/","/",url[i])
            print(thisurl)
            yield Request(thisurl,callback=self.next2,dont_filter=True)

     ##next2用于处理最终的每个新闻网页
    def next2(self,response):
        item=BaidunewsItem()
        item["link"]=response.url
        item["title"]=response.xpath("/html/head/title/text()").extract()
        item["content"]=response.body
        yield item




