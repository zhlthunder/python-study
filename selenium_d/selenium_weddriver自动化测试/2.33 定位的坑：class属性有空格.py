#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 前言
# 有些class属性中间有空格，如果直接复制过来定位是会报错的InvalidSelectorException: Message:
# The given selector u-label f-dn is either invalid or does not result in a WebElement. The following error occurred:
# InvalidSelectorError: Compound class names not permitted
# 这个报错意思是说定位语法错了。
#
# 一、定位带空格的class属性
# 1.以126邮箱为例：http://mail.126.com/，定位账号输入框
# 2.如果直接复制过来用class属性定位是会报错的

# 二、class属性科普
# 1.class属性中间的空格并不是空字符串，那是间隔符号，表示的是一个元素有多个class的属性名称，在整个HTML文档，使用CSS中的同一个class类可能是一个或多个！
# (class属性是比较特殊的一个，除了这个有多个属性外，其它的像name,id是没多个属性的)

# 三、class定位
# 1.既然知道class属性有空格是多个属性了，那定位的时候取其中的一个就行（并且要唯一），也就是说class="j-inputtext dlemail"，
# 取j-inputtext 和dlemail都是可以的，这样这个class属性在页面上唯一就行
# 2.那么问题来了：如何才知道这个元素的某个属性是不是在页面上是唯一的呢？

# 四、判断元素唯一性
# 1.F12切换到HTML界面，在搜索框输入关键字搜索，如：j-inputtext，然后按回车搜索，看页面上有几个class属性中有j-inputtext这个属性的，就知道是不是唯一的了。

# 五、class属性不唯一怎么办
# 1.如果这个class的多个属性都不是唯一的咋办呢，元素不唯一也不用怕，可以用复数定位，把所有的相同元素定位出来，按下标取第几个就行。

# 六、css定位
# 1.css来定位class属性的元素前面加个点（.）就行,然后空格变成点（.）就能定位了
# 2.当然css也可以取class属性的其中一个属性（页面上唯一的）来定位，定位方法是灵活多变的

# 代码：
# coding:utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://mail.126.com/")
driver.implicitly_wait(20)
driver.switch_to.frame("x-URS-iframe")
# 方法一：取单个class属性
driver.find_element_by_class_name("dlemail").send_keys("yoyo")
driver.find_element_by_class_name("dlpwd").send_keys("12333")
# 方法二：定位一组取下标定位（乃下策）
# driver.find_elements_by_class_name("j-inputtext")[0].send_keys("yoyo")
# driver.find_elements_by_class_name("j-inputtext")[1].send_keys("12333")
# 方法三：css定位
# driver.find_element_by_css_selector(".j-inputtext.dlemail").send_keys("yoyo")
# driver.find_element_by_css_selector(".j-inputtext.dlpwd").send_keys("123")
# 方法四：取单个class属性也是可以的
# driver.find_element_by_css_selector(".dlemail").send_keys("yoyo")
# driver.find_element_by_css_selector(".dlpwd").send_keys("123")