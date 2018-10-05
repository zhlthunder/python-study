#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 本篇主要介绍单选框和复选框的操作
# 一、认识单选框和复选框
#     1.先认清楚单选框和复选框长什么样
# 2.各位小伙伴看清楚哦，上面的单选框是圆的；下图复选框是方的，这个是业界的标准，要是开发小伙伴把图标弄错了，可以先抽他了。
# 二、radio和checkbox源码
#     1.上图的html源码如下，把下面这段复制下来，写到文本里，后缀改成.html就可以了。

# 三、单选：radio
#   1.首先是定位选择框的位置
# 2.定位id，点击图标就可以了，代码如下
#  3.先点击boy后，等十秒再点击girl，观察页面变化

url="file:///C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/selenium_d/selenium_weddriver%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/2.12%20radiobox,checkbox.html"
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(url)
# driver.find_element_by_id("boy").click()
# time.sleep(3)
# driver.find_element_by_id("girl").click()

# 四、复选框：checkbox
#   1.勾选单个框，比如勾选selenium这个，可以根据它的id=c1直接定位到点击就可以了。
# driver.find_element_by_id("c1").click()


# 五、全部勾选：
#     1.全部勾选，可以用到定位一组元素，从上面源码可以看出，复选框的type=checkbox,这里可以用xpath语法：.//*[@type='checkbox']
# checkboxs=driver.find_elements_by_xpath(".//*[@type='checkbox']")    ##这里需要注意".//*[@type='checkbox']" 和 "//*[@type='checkbox']"的实际定位结果相同
# for i in checkboxs:
#     i.click()
#
#    2.这里注意，敲黑板做笔记了：find_elements是不能直接点击的，它是复数的，所以只能先获取到所有的checkbox对象，然后通过for循环去一个个点击操作
#
#

# 六、判断是否选中：is_selected()
#     1.有时候这个选项框，本身就是选中状态，如果我再点击一下，它就反选了，这可不是我期望的结果，那么可不可以当它是没选中的时候，我去点击下；
# 当它已经是选中状态，我就不点击呢？那么问题来了：如何判断选项框是选中状态？
#     2.判断元素是否选中这一步才是本文的核心内容，点击选项框对于大家来说没什么难度。获取元素是否为选中状态，打印结果如下图。
#     3.返回结果为bool类型，没点击时候返回False,点击后返回True，接下来就很容易判断了，既可以作为操作前的判断，也可以作为测试结果的判断。

##没点击之前，判断选项框的状态
s=driver.find_element_by_id("boy").is_selected()
print(s)
driver.find_element_by_id("boy").click()
#点击后，判断元素是否为选中状态
r=driver.find_element_by_id("boy").is_selected()
print(r)



















