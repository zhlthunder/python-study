# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem  ##所有的导入，都是从核心目录，也就是项目的根目录，即第一层目录；
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4008154.html']  ##第一页的url
     ##scrapy会自动爬取第一个url,爬取后的信息都在response中；并自动执行parse（）方法
    def parse(self, response):

        ##先下载开始页的数据；
        item=DangdangItem()   #创建一个对象，用于存储数据
        item["title"]=response.xpath("//a[@name='itemlist-picture']/@title").extract()
        item["link"]=response.xpath("//a[@name='itemlist-picture']/@href").extract()
        item["comment"]=response.xpath("//a[@name='itemlist-review']/text()").extract()
        # print(item["title"],item["link"],item["comment"])
        yield item  #每爬取一页的数据，就将数据提交给 pipelines.py去处理，可以理解为压入一个数据存储的队列，内部机制会调度pipelines去处理数据；

        ##紧接着下载翻页的数据
        for i in range(2,31):#爬2~30页
            url="http://category.dangdang.com/pg"+str(i)+"-cid4008154.html"
            yield Request(url,callback=self.parse)   ##使用yield去返回，这样每次都可以从断点位置继续执行；和return 不同；

"""
爬虫的思维的， 先有一个开始的URL，然后对这个页面的源码进行分析，提取需要的信息，
然后构造后续的URL，
基于上面的思维，scrapy的架构设计就匹配了这种思想；

绿线是数据流向，首先从初始 URL 开始，Scheduler 会将其交给 Downloader 进行下载，下载之后会交给 Spider 进行分析，Spider 分析出来的结果有两种：
一种是需要进一步抓取的链接，例如之前分析的“下一页”的链接，这些东西会被传回 Scheduler ；另一种是需要保存的数据，它们则被送到 Item Pipeline 那里，
那是对数据进行后期处理（详细分析、过滤、存储等）的地方。另外，在数据流动的通道里还可以安装各种中间件，进行必要的处理。

困惑，对上面的callback的用法不是很理解，感觉会有重复调用的问题；
参考：
https://blog.csdn.net/tchenjx/article/details/51661173


"""