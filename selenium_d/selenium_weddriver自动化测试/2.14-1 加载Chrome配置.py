#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 一、加载Chrome配置  （未验证）
# chrome加载配置方法，只需改下面一个地方，username改成你电脑的名字（别用中文！！！）

'--user-data-dir=C:\Users\username\AppData\Local\Google\Chrome\User Data'
# coding:utf-8
# from selenium import webdriver
# # 加载Chrome配置
# option = webdriver.ChromeOptions()
# option.add_argument('--user-data-dir=C:\Users\Gloria\AppData\Local\Google\Chrome\User Data')
# driver = webdriver.Chrome(chrome_options=option)
# driver.implicitly_wait(30)
# driver.get("http://www.cnblogs.com/yoyoketang/")

# 二、Wap测试（未测试）
# 1.做Wap测试的可以试下，伪装成手机访问淘宝，会出现触屏版
# coding:utf-8
# from selenium import webdriver
# option = webdriver.ChromeOptions()
# # 伪装iphone登录
# # option.add_argument('--user-agent=iphone')
# # 伪装android
# option.add_argument('--user-agent=android')
# driver = webdriver.Chrome(chrome_options=option)
# driver.get('http://www.taobao.com/')