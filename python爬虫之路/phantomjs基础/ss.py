#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import time
from selenium import webdriver
browser=webdriver.PhantomJS(executable_path=r"C:\python3\phantomjs-2.1.1\bin\phantomjs.exe")
browser.get("https://www.baidu.com/")
# browser.get_screenshot_as_file("test.jpg")
browser.find_element_by_xpath('//*[@id="kw"]').clear()
browser.find_element_by_xpath('//*[@id="kw"]').send_keys("爬虫")
browser.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(5)  #重要， phantomjs模拟了人访问时，如果因为网速的问题会出现延时，如果不加，会导致网页加载有问题，切记
##这也就是pantomjs的好的地方，同步和异步加载的内容都可以获取到，比urllib和scrapy好一些
# browser.get_screenshot_as_file("test.jpg")
data=browser.page_source
browser.quit()
print(len(data))
import re
title=re.compile("<title>(.*?)</title>").findall(data)
print(title)