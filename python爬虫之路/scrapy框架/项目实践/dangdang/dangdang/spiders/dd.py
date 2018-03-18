# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/cid4008154.html']

    def parse(self, response):

        ##先下载开始页的数据；
        item=DangdangItem()   #创建一个对象，用于存储数据
        item["title"]=response.xpath("//a[@name='itemlist-picture']/@title").extract()
        item["link"]=response.xpath("//a[@name='itemlist-picture']/@href").extract()
        item["comment"]=response.xpath("//a[@name='itemlist-review']/text()").extract()
        # print(item["title"],item["link"],item["comment"])
        yield item  #没爬取一页的数据，就将数据提交给 pipelines.py去处理，可以理解为压入一个数据存储的队列，内部机制会调度pipelines去处理数据；

        ##紧接着下载翻页的数据
        for i in range(2,31):#爬2~30页
            url="http://category.dangdang.com/pg"+str(i)+"-cid4008154.html"
            yield Request(url,callback=self.parse)   ##使用yield去返回，这样每次都可以从断点位置继续执行；和return 不同；

