#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
from selenium import webdriver
import time
driver=webdriver.Chrome()


# 前言
# 前面的几篇都是讲如何定位一个元素，有时候一个页面上有多个对象需要操作，如果一个个去定位的话，比较繁琐，这时候就可以定位一组对象。
# webdriver 提供了定位一组元素的方法，跟前面八种定位方式其实一样，只是前面是单数，这里是复数形式：find_elements
#
#
# 本篇拿百度搜索作为案例，从搜索结果中随机选择一条搜索结果，然后点击查看。
# 一、定位搜索结果
#     1.在百度搜索框输入关键字“测试部落”后，用firebug查看页面元素，可以看到这些搜索结果有共同的属性。
#    2.从搜索的结果可以看到，他们的父元素一样：<h3 class="t">
#     3.标签都一样，且target属性也一样：<a target="_blank" />
#     4.于是这里可以用css定位（当然用xpath也是可以的）

driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(u"测试部落")
driver.find_element_by_id("kw").submit()
s=driver.find_elements_by_css_selector("h3.t>a")
# 二、确认定位结果
#     1.前面的定位策略只是一种猜想，并不一定真正获取到自己想要的对象的，也行会定位到一些不想要的对象。
#     2.于是可以获取对象的属性，来验证下是不是定位准确了。这里可以获取href属性，打印出url地址。
for i in s:
    print(i.get_attribute("href"))

# 三、随机函数
#     1.搜索结果有10条，从这10条中随机取一个就ok了
#     2.先导入随机函数：import random
#     3.设置随机值范围为0~9：a=random.randint(0~9)

# 四、随机打开url
#     1.从返回结果中随机取一个url地址
#     2.通过get方法打卡url
#     3.其实这种方式是接口测试了，不属于UI自动化，这里只是开阔下思维，不建议用这种方法

# import random
# t=random.randint(0,9)
# a=s[t].get_attribute("href")
# driver.get(a)


# 五、通过click点击打开
#     1.前面那种方法，是直接访问url地址，算是接口测试的范畴了，真正模拟用户点击行为，得用click的方法

import random
# 设置随机值
t = random.randint(0, 9)
# 随机取一个结果点击鼠标
s[t].click()

# 不知道有小伙伴有没注意一个细节，前面在搜索框输入关键字后，我并没有去点击搜索按钮，而是用的submit的方法，submit相当于回车键。
# 具体的操作对象方法，下篇详细介绍。本篇主要学会定位一组对象，然后随机操作其中的一个。




















