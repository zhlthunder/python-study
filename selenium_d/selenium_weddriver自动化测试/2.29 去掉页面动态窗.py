#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 我们在浏览网页时经常会碰到各种花样的弹窗，在做UI自动化测试的时候势必要处理这些弹窗，这里就介绍一下目前前端界两种弹窗的处理方法。
# 一、alert弹窗

# 这种弹窗是最简单的一种，Selenium里有自带的方法来处理它，用switch_to.alert先定位到弹窗，然后使用一系列方法来操作：
# accept - 点击【确认】按钮
#
# dismiss - 点击【取消】按钮（如有按钮）
#
# send_keys - 输入内容（如有输入框）

# 二、自定义弹窗
# 由于alert弹窗不美观，现在大多数网站都会使用自定义弹窗，使用Selenium自带的方法就驾驭不了了，此时就要搬出JS大法。这里举一个新世界教育官网首页的例子
# 大家能看到，图中的这种弹窗就是现在主流的表现形式，处理这种弹窗可以利用HTML DOM Style 对象，有一个display属性，可以设置元素如何被显示，
# 详细解释可以参考http://www.w3school.com.cn/jsref/prop_style_display.asp。将display的值设置成none就可以去除这个弹窗了：
# js = 'document.getElementById("doyoo_monitor").style.display="none";'

# 代码：
# encoding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://sh.xsjedu.org/")
time.sleep(1)
js='document.getElementById("doyoo_monitor").style.display="none";'
driver.execute_script(js)
