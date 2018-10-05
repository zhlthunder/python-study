#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 前言
#     前面有篇专门用js解决了浏览器滚动条的问题，生活总是多姿多彩，有的滚动条就在页面上，这时候又得仰仗js大哥来解决啦。
# 一、内嵌滚动条
#     1.下面这张图就是内嵌div带有滚动条的样子，记住它的长相。

# 二、纵向滚动
#
#     1.这个是div的属性：<div id="yoyoketang" name="yoyo" class="scroll">
#
#     2.这里最简单的通过id来定位，通过控制 scrollTop的值来控制滚动条高度
#
#     3.运行下面代码，观察页面是不是先滚动到底部，过五秒再回到顶部。（get里面地址是浏览器打开该页面的地址）

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("file:///C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/selenium_d/selenium_weddriver%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/2.24%E5%86%85%E5%B5%8C%E6%BB%9A%E5%8A%A8%E6%9D%A1.html")
# ##纵向底部
# js1='document.getElementById("yoyoketang").scrollTop=10000'
# driver.execute_script(js1)
# time.sleep(5)
# ##纵向顶部
# js2='document.getElementById("yoyoketang").scrollTop=0'
# driver.execute_script(js2)
#
# 三、横向滚动
#
#   1.先通过id来定位，通过控制scrollLeft的值来控制滚动条高度
#
# ##横向右侧
# js3='document.getElementById("yoyoketang").scrollLeft=10000'
# driver.execute_script(js3)
# time.sleep(5)
# ##横向左侧
# js4='document.getElementById("yoyoketang").scrollLeft=0'
# driver.execute_script(js4)
#
#
# 四、用class属性定位
#     1.js用class属性定位，返回的是一个list对象，这里取第一个就可以了。
#     2.这里要注意了，element和elements有很多小伙伴傻傻分不清楚。

##获取的class返回的是 list对象，取list的第一个
js5='document.getElementsByClassName("scroll")[0].scrollTop=10000'
driver.execute_script(js5)

time.sleep(5)
##控制横向滚动条的位置
js6='document.getElementsByClassName("scroll")[0].scrollLeft=10000'
driver.execute_script(js6)

# 有时候很多元素属性都一样时候，就可以用复数定位，取对应的第几个就可以了。















