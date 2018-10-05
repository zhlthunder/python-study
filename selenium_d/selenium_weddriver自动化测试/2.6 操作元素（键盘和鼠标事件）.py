#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from selenium import webdriver
import time
driver=webdriver.Firefox()


# 前言
# 在前面的几篇中重点介绍了一些元素的定位方法，定位到元素后，接下来就是需要操作元素了。本篇总结了web页面常用的一些操作元素方法，可以统称为行为事件
# 有些web界面的选项菜单需要鼠标悬停在某个元素上才能显示出来（如百度页面的设置按钮）。

# 2.6.1 简单操作
#     1.点击（鼠标左键）页面按钮：click()
#     2.清空输入框：clear()
#     3.输入字符串：send_keys()
#     4.send_keys()如果是发送中文的，前面需加u，如：u"中文",
# 因为这里是输入到windows系统了，windows系统是GBK编码，我们的脚本是utf-8,需要转码为Unicode国际编码，这样才能识别到。

# driver.get("http://www.baidu.com")
# #implicitly_wait是隐式等待，作用是全局的。
# # driver.implicitly_wait(10)  ##使用这句会报错，查了一下，是版本兼容性的问题，先忽略，不用这个
# driver.find_element_by_id("kw").clear()
# #send_keys 里如果是中文的haul，前面要加u
# driver.find_element_by_id("kw").send_keys(u"上海-悠悠")
# driver.find_element_by_id("su").click()



# 2.6.2 submit提交表单
# 1.在前面百度搜索案例中，输入关键字后，可以直接按回车键搜索，也可以点搜索按钮搜索。
# 2.submit()一般用于模拟回车键。

# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys(u"测试部落")
# ##submit()模拟enter键提交表单
# driver.find_element_by_id("kw").submit()


# 2.6.3 键盘操作
#     1.selenium提供了一整套的模拟键盘操作事件，前面submit()方法如果不行的话，可以试试模拟键盘事件
#     2.模拟键盘的操作需要先导入键盘模块：from selenium.webdriver.common.keysimport Keys
#     3.模拟enter键，可以用send_keys(Keys.ENTER)
##
# from selenium.webdriver.common.keys import Keys
# driver.get("http://www.hordehome.com")## 网站登录有问题，此代码待测试
# time.sleep(3)
# driver.find_element_by_id("search-button").click()
# driver.find_element_by_id("search-term").clear()
# driver.find_element_by_id("search-term").send_keys("selenium")
# #模拟enter键盘操作回车按钮
# driver.find_element_by_id("search-term").send_keys(Keys.ENTER)

# 4.其它常见的键盘操作：
#     键盘F1到F12：send_keys(Keys.F1)把F1改成对应的快捷键：
#
#     复制Ctrl+C：send_keys(Keys.CONTROL,'c')
#
#     粘贴Ctrl+V：send_keys(Keys.CONTROL,'v')
#
#     全选Ctrl+A：send_keys(Keys.CONTROL,'a')
#
#     剪切Ctrl+X：send_keys(Keys.CONTROL,'x')
#
#     制表键Tab:  send_keys(Keys.TAB)
#
#     这里只是列了一些常用的，当然除了键盘事件，也有鼠标事件


# 2.6.4 鼠标悬停事件
#     1.鼠标不仅仅可以点击(click),鼠标还有其它的操作，如：鼠标悬停在某个元素上，鼠标右击，鼠标按住某个按钮拖到
#     2.鼠标事件需要先导入模块：from selenium.webdriver.common.action_chainsimport ActionChains
#         perform() 执行所有ActionChains中的行为；
#         move_to_element() 鼠标悬停。
#     3.这里以百度页面设置按钮为例：

from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()##使用chrome浏览器没有问题，使用火狐浏览器报错，推测还是浏览器兼容性的问题
driver.get("http://www.baidu.com")
time.sleep(3)
##将鼠标悬停在搜索设置按钮上
mouse=driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.implicitly_wait(5)
driver.find_element_by_link_text("搜索设置").click()

# 4.除了常用的鼠标悬停事件外，还有
#    右击鼠标：context_click()
#    双击鼠标：double_click()
#    依葫芦画瓢，替换上面案例中对应的鼠标事件就可以了
#    selenium提供了一整套完整的鼠标和键盘行为事件，功能还是蛮强大滴。下一篇介绍多窗口的情况下如何处理。























































































