# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title=scrapy.Field()  #存储商品名
    link=scrapy.Field()  #存储商品的链接
    comment=scrapy.Field() #存储商品的评论数