# -*- coding: utf-8 -*-
import scrapy
from baidunews.items import BaidunewsItem

class N1Spider(scrapy.Spider):
    name = 'n1'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']
    allid=['LocalNews', 'LocalNews', 'civilnews', 'InternationalNews', 'EnterNews', 'SportNews', 'FinanceNews', 'TechNews', 'MilitaryNews', 'InternetNews', 'DiscoveryNews', 'LadyNews', 'HealthNews', 'PicWall']


    def parse(self, response):
        print(self.allid)
