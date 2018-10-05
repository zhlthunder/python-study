#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 前言
# 有时候元素明明已经找到了，运行也没报错，点击后页面没任何反应。这种问题遇到了，是比较头疼的，因为没任何报错，只是click事件失效了。
# 本篇用2种方法解决这种诡异的点击事件失效问题
# 一、遇到的问题
# 1.在练习百度的搜索设置按钮时，点保存设置按钮，alert弹出没弹出（代码没报错，只是获取alert失败），相信不只是我一个人遇到过
#
# 二、点击父元素 （未验证）
# 1.遇到这种问题，应该是前面操作select后导致的后遗症（因为我注释掉select那段是可以点击成功的）。
# 2.第一种解决办法，先点击它的父元素一次，然后再点击这个元素。

# 3.实现代码如下

##方法1：先点击父元素，
from selenium import  webdriver
driver=webdriver.Chrome()
# driver.find_element_by_id("gxszButton").click()
# driver.find_element_by_class_name("prefpanelgo").click()


# 三、js直接点击
#
# 1.遇到这种诡异问题，是时候出绝招了：js大法。
# 2.用js直接执行点击事件
##方法:2： 用js直接去点击
# js='document.getElementsByClassName("prefpanelgo")[0].click();'
# driver.execute_script(js)



# 参考代码：
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)
time.sleep(3)
mouse = driver.find_element("link text", "设置")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(3)
driver.find_element("link text", "搜索设置").click()
time.sleep(3)
s = driver.find_element("id", "nr")
Select(s).select_by_visible_text("每页显示20条")
# 方法一：先点父元素 交流QQ群：232607095
# driver.find_element("id", "gxszButton").click()
# driver.find_element("class name", "prefpanelgo").click()
# 方法二：用js直接去点击 交流QQ群：232607095
js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
driver.execute_script(js)
##处理alert窗口
alert=driver.switch_to_alert()
alert.accept()
