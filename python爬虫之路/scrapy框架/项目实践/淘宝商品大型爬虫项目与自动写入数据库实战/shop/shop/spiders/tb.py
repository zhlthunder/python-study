# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import ssl
from scrapy.http import Request
import re
from shop.items import ShopItem


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['taobao.com']
    start_urls = ['http://taobao.com/']

    def parse(self, response):
        key="坚果"
        for i in range(0,10):
            url="https://s.taobao.com/search?q="+str(key)+"&js=1&stats_click=search_radio_all%3A1&ie=utf8&s="+str(i*44)
            yield Request(url=url,callback=self.page)

    def page(self,response):
        body=response.body.decode("utf-8",'ignore')
        patid='"nid":"(.*?)"' ##提取全部商品的id
        allid=re.compile(patid).findall(body)
        # print(allid)

        for j in range(0,len(allid)):
            thisid=allid[j]
            url1="https://detail.tmall.com/item.htm?id="+str(thisid)
            # print(url1)
            yield Request(url=url1,callback=self.next,dont_filter=True)

    def next(self,response):
        data=response.body.decode("utf-8",'ignore')
        item=ShopItem()
        item['title']=response.xpath("//title/text()").extract()
        item['link']=response.url

        pat='"reservePrice":"(.*?)"'
        price=re.compile(pat).findall(data)[0]
        # print(print(price))
        item['price']=price

        ##提取评论数
        patid='id=(.*?)$'
        thisid=re.compile(patid).findall(response.url)[0]
        ##构造包含评论的url
        commenturl="https://dsr-rate.tmall.com/list_dsr_info.htm?itemId="+thisid
        # print(commenturl)
        # ssl._create_default_https_context=ssl._create_unverified_context() ##这里的作用后续继续确认一下
        commentdata=urllib.request.urlopen(commenturl).read().decode('utf-8','ignore')
        # print(len(commentdata))
        patt='"rateTotal":(.*?)}'
        comment=re.compile(patt).findall(commentdata)[0]
        # print(comment)
        item['commnet']=comment

        # print(item['title'][0])
        # print(item['link'])
        # print(price)
        # print(comment)
        ##此处打印调试已经通过，传递到pipeline中，打印和写入数据库的功能有点问题，待继续调试；
        yield item





