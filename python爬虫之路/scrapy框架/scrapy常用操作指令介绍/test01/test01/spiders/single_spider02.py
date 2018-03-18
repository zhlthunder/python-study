# -*- coding: utf-8 -*-
import scrapy


class SingleSpider02Spider(scrapy.Spider):
    name = 'single_spider02'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://iqianyue.com/']

    def parse(self, response):
        pass
