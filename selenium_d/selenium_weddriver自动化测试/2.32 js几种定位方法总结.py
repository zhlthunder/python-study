#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 前言
# 本篇总结了几种js常用的定位元素方法，并用js点击按钮，对input输入框输入文本
#
# 一、以下总结了5种js定位的方法
# 除了id是定位到的是单个element元素对象，其它的都是elements返回的是list对象
# 1.通过id获取
# document.getElementById(“id”)
# 2.通过name获取
#  document.getElementsByName(“Name”)
#
# 返回的是list
#
# 3.通过标签名选取元素
# document.getElementsByTagName(“tag”)
# 4.通过CLASS类选取元素
# document.getElementsByClassName(“class”)
# 兼容性：IE8及其以下版本的浏览器未实现getElementsByClassName方法
# 5.通过CSS选择器选取元素
# document.querySelectorAll(“css selector")
# 兼容性：IE8及其以下版本的浏览器只支持CSS2标准的选择器语法

# 代码参考：
# coding: utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://cnblogs.com/yoyoketang")

#定位首页管理按钮：id=blog_nav_contact
js1 = 'document.getElementById("blog_nav_contact").click();'
driver.execute_script(js1)

#输入账号
js2 = 'document.getElementsByClassName("input-text")[0].value="悠悠";'
driver.execute_script(js2)

#输入密码
js3 = 'document.getElementsByClassName("input-text")[1].value="xxx";'
driver.execute_script(js3)

#勾选记住密码
js4 = 'document.getElementsByName("remember_me")[0].click();'
driver.execute_script(js4)

#点击登录按钮
js5 = 'document.querySelectorAll(#signin)[0].click();'
driver.execute_script(js5)