#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 前言
# 通常在做断言之前，都要先获取界面上元素的属性，然后与期望结果对比。本篇介绍几种常见的获取元素属性方法。
# 一、获取页面title
# 1.有很多小伙伴都不知道title长在哪里，看下图左上角。
# 2.获取title方法很简单，直接driver.title就能获取到。

from selenium import  webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
# time.sleep(3)
# title=driver.title
# print(title)

# 二、获取元素的文本
# 1.如下图这种显示在页面上的文本信息，可以直接获取到
# 2.查看元素属性：<a id="setf" target="_blank" onmousedown="return ns_c({'fm':'behs','tab':'favorites','pos':0})
# " href="//www.baidu.com/cache/sethelp/help.html">把百度设为主页</a>
# 3.通过driver.text获取到文本
time.sleep(2)
# text=driver.find_element_by_id("setf").text
# print(text)
#
# 三、获取元素的标签
# 1.获取百度输入框的标签属性

##获取元素的标签
# tag=driver.find_element_by_id("kw").tag_name
# print(tag)



# 四、获取元素的其它属性
# 1.获取其它属性方法:get_attribute("属性")，这里的参数可以是class、name等任意属性
# 2.如获取百度输入框的class属性

##获取元素的其它属性
# name=driver.find_element_by_id("kw").get_attribute("class")
# print(name)
#
#
# 五、获取输入框内的文本值
# 1、如果在百度输入框输入了内容，这里输入框的内容也是可以获取到的
##获取输入框的内容
# driver.find_element_by_id("kw").send_keys("hhhhhhhhhhhh")
# value=driver.find_element_by_id("kw").get_attribute("value")
# print(value)
#
# 六、获取浏览器名称
# 1.获取浏览器名称很简单，用driver.name就能获取到
#
# # 获取浏览器名称
# driver.name