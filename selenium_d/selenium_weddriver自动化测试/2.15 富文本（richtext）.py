#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##待我的博客开通后继续确认此章节？？？？

# 前言
#      富文本编辑框是做web自动化最常见的场景，有很多小伙伴不知从何下手，本篇以博客园的编辑器为例，解决如何定位富文本，输入文本内容
# 一、加载配置
#     1.打开博客园写随笔，首先需要登录，这里为了避免透露个人账户信息，我直接加载配置文件，免登录了。

# 补充：
# {
# https://www.cnblogs.com/xmlbw/p/4498113.html
# 一、加载所有Chrome配置
#
# 　　用Chrome地址栏输入chrome://version/，查看自己的“个人资料路径”，然后在浏览器启动时，调用这个配置文件，代码如下：
# }

from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument(r'--user-data-dir=C:\Users\lin\AppData\Local\Google\Chrome\User Data\Default') #设置成用户自己的数据目录
driver = webdriver.Chrome(chrome_options=option)

# 二、打开编辑界面
#     1.博客首页地址：bolgurl = "http://www.cnblogs.com/"
#     2.我的博客园地址：yoyobolg = bolgurl + "yoyoketang"
#     3.点击“新随笔”按钮，id=blog_nav_newpost
driver.get("http://www.cnblogs.com/")