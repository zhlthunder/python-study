#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
import time
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.find_element_by_id("kw").send_keys("链家")
browser.find_element_by_id("su").click()
for i in range(60):
    try:
        if u"链家_百度搜索" == browser.title: break
    except: pass
    time.sleep(1)

browser.find_element_by_link_text(u"链家，连接每个家的故事").click()
# print(browser.window_handles)
# ['CDwindow-676C9027328A189ECA898F18BB3783C5', 'CDwindow-EBDCFB5641D1ED8E6ECBA30FE71E5616']
# print(browser.current_window_handle)
# CDwindow-07B26A85D63BE8AC26ABE04950FBB004
# print(browser.current_url)
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E9%93%BE%E5%AE%B6&rsv_pq=cf8a2ce100008447&rsv_t=f6f7yNKv16I9ROlStt8b4sZCrLC9jhlWM8G9uWMZSz6ijDvJ%2FKmrh3S7ke4&rqlang=cn&rsv_enter=0&rsv_sug3=2&inputT=248&rsv_sug4=248
print(browser.title)  ##老的页面

browser.switch_to_window(browser.window_handles[1])
print(browser.title)

tt=browser.find_element_by_xpath('//*[@id="ershoufanglist"]/div/ul/li[2]/a/div[1]/div/p[2]/span[3]').text()
print(tt)
