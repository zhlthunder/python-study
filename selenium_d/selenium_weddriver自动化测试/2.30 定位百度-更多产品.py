#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 练习题2：定位百度首页上更多产品里面的‘全部产品’

# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)
driver.maximize_window()
time.sleep(2)
e = driver.find_element_by_link_text("更多产品")
ActionChains(driver).move_to_element(e).perform()
time.sleep(1)

##定位方法1
# ele = driver.find_element_by_name("tj_more")
# # 经确认，是可以定位到元素的
# print(ele.text)
# # 这一步点击失效了
# ele.click()

##定位方法2
# js大法好，完美解决ckick失效问题
js = "document.getElementsByName('tj_more')[0].click()"
driver.execute_script(js)