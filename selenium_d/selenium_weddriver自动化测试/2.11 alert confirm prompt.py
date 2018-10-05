#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 前言
# 不是所有的弹出框都叫alert，在使用alert方法前，先要识别出到底是不是alert。先认清楚alert长什么样子，下次碰到了，就可以用对应方法解决。
# alert\confirm\prompt弹出框操作主要方法有：
# text：获取文本值
# accept() ：点击"确认"
# dismiss() ：点击"取消"或者叉掉对话框
# send_keys() ：输入文本值 --仅限于prompt,在alert和confirm上没有输入框
#
# 一、认识alert\confirm\prompt
#      1.如下图，从上到下依次为alert\confirm\prompt，先认清楚长什么样子，以后遇到了就知道如何操作了。
# 2.html源码如下（有兴趣的可以copy出来，复制到txt文本里，后缀改成html就可以了，然后用浏览器打开）：

# 二、alert操作
#
#    1.先用switch_to_alert()方法切换到alert弹出框上
#     2.可以用text方法获取弹出的文本 信息
#     3.accept()点击确认按钮
#     4.dismiss()相当于点右上角x，取消弹出框
#    （url的路径，直接复制浏览器打开的路径）

# url="file:///C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/selenium_d/selenium_weddriver%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/2.11%20%E5%BC%B9%E7%AA%97.html"
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get(url)
# time.sleep(4)
# driver.find_element_by_id("alert").click()
# time.sleep(3)
# t=driver.switch_to_alert()
# ##打印警告窗的文本内容
# print(t.text)
# #点警告窗确认按钮
# t.accept()
# # t.dismiss() #相当于点x按钮，取消



# 三、confirm操作
#    1.先用switch_to_alert()方法切换到alert弹出框上
#     2.可以用text方法获取弹出的文本 信息
#     3.accept()点击确认按钮
#     4.dismiss()相当于点取消按钮或点右上角x，取消弹出框
# （url的路径，直接复制浏览器打开的路径）

# url="file:///C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/selenium_d/selenium_weddriver%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/2.11%20%E5%BC%B9%E7%AA%97.html"
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get(url)
# time.sleep(4)
# driver.find_element_by_id("confirm").click()
# time.sleep(3)
# t=driver.switch_to_alert()
# ##打印警告窗的文本内容
# print(t.text)
# #点警告窗确认按钮
# # t.accept()
# # t.dismiss() #相当于点x按钮，取消




# 四、prompt操作
#    1.先用switch_to_alert()方法切换到alert弹出框上
#     2.可以用text方法获取弹出的文本 信息
#     3.accept()点击确认按钮
#     4.dismiss()相当于点右上角x，取消弹出框
#     5.send_keys()这里多个输入框，可以用send_keys()方法输入文本内容
# （url的路径，直接复制浏览器打开的路径）


# url="file:///C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/selenium_d/selenium_weddriver%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/2.11%20%E5%BC%B9%E7%AA%97.html"
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get(url)
# time.sleep(4)
# driver.find_element_by_id("prompt").click()
# time.sleep(3)
# t=driver.switch_to_alert()
# ##打印警告窗的文本内容
# print(t.text)
# t.send_keys("hello selenium2")  ##send_keys有问题，待继续排查 ？？？？
# #点警告窗确认按钮
# # t.accept()
# # t.dismiss() #相当于点x按钮，取消



# 五、select遇到的坑
#     1.在操作百度设置里面，点击“保存设置”按钮时，alert弹出框没有弹出来。（Ie浏览器是可以的）
#     2.分析原因：经过慢慢调试后发现，在点击"保存设置"按钮时，由于前面的select操作后，失去了焦点
#     3.解决办法：在select操作后，做个click()点击操作

# s = driver.find_element_by_id("nr")
# Select(s).select_by_visible_text("每页显示20条")
# time.sleep(3)
# s.click()

 # 六、最终代码 加2.10   补充alert相关
 ##遗留问题：直接把代码贴在此处时，会发生报错，提示找不到元素，原因待继续排查？？？


# 这一篇应该比较简单，alert相关的内容比较少，虽然有一些页面也有弹窗，但不是所有的弹窗都叫alert。
#
# alert的弹出框界面比较简洁，调用的是Windows系统弹窗警告框，没花里胡哨的东西，还是很容易区分的。



















