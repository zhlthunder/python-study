#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 前言
# 江湖传言，武林中流传八种定位，其中xpath是宝刀屠龙，css是倚天剑。
# 除了这八种，其实还有十种定位方法，眼看就快失传了，今天小编让失传已久的定位方法重出江湖！

# 一、十八种定位方法
#
# 前八种是大家都熟悉的，经常会用到的
#
# 1.id定位：find_element_by_id(self, id_)
# 2.name定位：find_element_by_name(self, name)
# 3.class定位：find_element_by_class_name(self, name)
# 4.tag定位：find_element_by_tag_name(self, name)
# 5.link定位：find_element_by_link_text(self, link_text)
# 6.partial_link定位find_element_by_partial_link_text(self, link_text)
# 7.xpath定位：find_element_by_xpath(self, xpath)
# 8.css定位：find_element_by_css_selector(self, css_selector）
#
# 这八种是复数形式
#
# 9.id复数定位find_elements_by_id(self, id_)
# 10.name复数定位find_elements_by_name(self, name)
# 11.class复数定位find_elements_by_class_name(self, name)
# 12.tag复数定位find_elements_by_tag_name(self, name)
# 13.link复数定位find_elements_by_link_text(self, text)
# 14.partial_link复数定位find_elements_by_partial_link_text(self, link_text)
# 15.xpath复数定位find_elements_by_xpath(self, xpath)
# 16.css复数定位find_elements_by_css_selector(self, css_selector)
#
# 这两种就是快失传了的
#
# 17.find_element(self, by='id', value=None)
# 18.find_elements(self, by='id', value=None)
#
# 二、element和elements傻傻分不清
# 1.element方法定位到是是单数，是直接定位到元素
# 2.elements方法是复数，这个学过英文的都知道，定位到的是一组元素，返回的是list队列
# 3.可以用type()函数查看数据类型
# 4.打印这个返回的内容看看有什么不一样

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
# ##这里是定位的单个id
# element=driver.find_element_by_id("kw")
# print(type(element))
# print(element)
#
# ##这里定位时多个class,
# elements=driver.find_elements_by_class_name("mnav")
# print(type(elements))
# print(elements)


# 三、elements定位方法
# 1.前面2.8章节讲过定位一组元素用elements的方法，elements也可以用于单数定位。
#
# 2.这里重点介绍下用elements方法如何定位元素，当一个页面上有多个属性相同的元素时，然后父元素的属性也比较模糊，不太好定位。
# 这个时候不用怕，换个思维，别老想着一次定位到，可以先把相同属性的元素找出来，取对应的第几个就可以了。
#
# 3.如下图，百度页面上有六个class一样的元素，我要定位“地图”这个元素。
# 4.取对应下标即可定位了。


#参考代码：
# coding:utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 这里用的css语法
s = driver.find_elements("css selector", ".mnav")
# '地图'在第3个位置
print(s[2].text)
s[2].click()
# 这个写法也是可以的
# driver.find_elements("css selector", ".mnav")[3].click()














