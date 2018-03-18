#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from  scrapy.spiders import Spider

class FirstSpider(Spider):
    name="First"
    allowed_domains=["baidu.com"]
    start_urls=["http://www.baidu.com"]

    def parse(self, response):
        pass