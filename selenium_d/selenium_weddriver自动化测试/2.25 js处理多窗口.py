#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 前言
# 在打开页面上链接的时候，经常会弹出另外一个窗口（多窗口情况前面这篇有讲解：Selenium2+python自动化13-多窗口、句柄（handle）），
# 这样在多个窗口之间来回切换比较复杂，那么有没有办法让新打开的链接在一个窗口打开呢？
# 要解决这个问题，得从html源码上找到原因，然后修改元素属性才能解决。很显然js在这方面是万能的，于是本篇得依靠万能的js大哥了。
# 一、多窗口情况
#     1.在打baidu的网站链接时，会重新打开一个窗口
#     (注意：我的百度页面是已登录状态，没登录时候是不会重新打开窗口的)

# 二、查看元素属性：target="_blank"
# 1.查看元素属性，会发现这些链接有个共同属性：target="_blank"

# 三、去掉target="_blank"属性
# 1.因为此链接元素target="_blank"，所以打开链接的时候会重新打开一个标签页，那么解决这个问题，去掉该属性就可以了。
# 2.为了验证这个问题，可以切换到html编辑界面，手动去掉“_blank”属性。

# 3.删除“_blank”属性后，重新打开链接，这时候会发现打开的新链接会在原标签页打开。

# 四、js去掉target="_blank"属性
# 1.第一步为了先登录，我这里加载配置文件免登录了（不会的看这篇：Selenium2+python自动化18-加载Firefox配置）
# 2.这里用到js的定位方法，定位该元素的class属性
# 3.定位到该元素后直接修改target属性值为空



##chrome浏览器，无法通过配置文件记录登录状态，原因待继续排查？？？？？：
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium import webdriver
# option = webdriver.ChromeOptions()
# option.add_argument(r'--user-data-dir=C:\Users\lin\AppData\Local\Google\Chrome\User Data\Default\Default\Default') #设置成用户自己的数据目录
# driver = webdriver.Chrome(chrome_options=option)
# driver.get("https://www.baidu.com/")

##火狐浏览器，查看配置文件路径的方法：菜单 “帮助”--故障排查信息--显示文件夹
##当前火狐用户配置文件路径：C:\Users\lin\AppData\Roaming\Mozilla\Firefox\Profiles\5ickf9vm.default-1478654411172
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#加载配置文件免登录
profiledir=r'C:\Users\lin\AppData\Roaming\Mozilla\Firefox\Profiles\5ickf9vm.default-1478654411172'
profile=webdriver.FirefoxProfile(profiledir)
driver=webdriver.Firefox(profile)
# driver=webdriver.Firefox()  ##如果用这种方式，即不加载配置文件时，就无法实现自动登录
driver.get("http://www.baidu.com")

##修改元素属性：
js='document.getElementsByClassName("mnav")[0].target="";'
driver.execute_script(js)
driver.find_element_by_link_text("新闻").click()


# 参考代码：
# # coding:utf-8
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# # 加载配置文件免登录
# profileDir = r'C:\Users\Gloria\AppData\Roaming\Mozilla\Firefox\Profiles\1x41j9of.default'
# profile = webdriver.FirefoxProfile(profileDir)
# driver = webdriver.Firefox(profile)
# driver.get("https://www.baidu.com/")
# # 修改元素的target属性
# js = 'document.getElementsByClassName("mnav")[0].target="";'
# driver.execute_script(js)
# driver.find_element_by_link_text("糯米").click()


# 注意：并不是所有的链接都适用于本方法，本篇只适用于有这个target="_blank"属性链接情况。
#
# 本篇仅提供解决问题的办法和思路，不要完全照搬代码！！！








