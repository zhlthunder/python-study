#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 前言
# 元素定位可以说是学自动化的小伙伴遇到的一道门槛，学会了定位也就打通了任督二脉，前面分享过selenium的18般武艺，再加上五种js的定位大法。
# 这些还不够的话，今天再分享一个定位神器jquery，简直逆天了！
#
# 一、jquery搜索元素
# 1.按F12进控制台
# 2.点全部按钮
# 3.右侧如果没出现输入框，就点下小箭头按钮
# 4.输入框输入jquery定位语法，如：$("#input1")
#
# 5.点运行按钮
# 6.左边会出现定位到的元素，如果有多个会以list列表的形式展示出。

# 二、jquery定位语法
# 1.jquery语法可以学下w3school的教程：http://www.w3school.com.cn/jquery/jquery_syntax.asp
#
# 2.格式如下：
# $(selector).action()
# --selector:这里的定位语法和css的定位语法是一致的，如：id就是#，class就是点（.）,tag标签名前面就无符号
# --action:这个是定位元素之后的操作行为事件，如click

# 三、jquery行为
# 1.发送文本语法：$(selector).val(输入文本的值)
# 2.清空文本语法：$(selector).val('')   # 空字符串，两个单引号
# 3.点击按钮：$(selector).click()

# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://passport.cnblogs.com/user/signin")
driver.implicitly_wait(20)
# 输入账号
username = "$('#input1').val('上海-悠悠')"
driver.execute_script(username)
# 清空文本
# time.sleep(5)
# clear = "$('#input1').val('')"
# driver.execute_script(clear)
# 输入密码
psw = "$('#input2').val('yoyo')"
driver.execute_script(psw)
# 点击登录按钮
button = "$('#signin').click()"
driver.execute_script(button)