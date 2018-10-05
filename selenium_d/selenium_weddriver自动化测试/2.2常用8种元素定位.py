#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
from selenium import webdriver
import time
driver=webdriver.Firefox()


# 2.2.3 find_element_by_id()
# 1.从上面定位到的元素属性中，可以看到有个id属性：id="kw"，这里可以通过它的id属性定位到这个元素。
# 2.定位到搜索框后，用send_keys()方法，输入文本。

# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("python")

# 2.2.4 find_element_by_name()
#    1.从上面定位到的元素属性中，可以看到有个name属性：name="wd"，这里可以通过它的name属性单位到这个元素。
#     说明：如果这里运行后会报错，说明这个搜索框的name属性不是唯一的，无法通过name属性直接定位到输入框
# driver.get("http://www.baidu.com")
# driver.find_element_by_name("wd").send_keys("python")

# 2.2.5 find_element_by_class_name()
# 1.从上面定位到的元素属性中，可以看到有个class属性：class="s_ipt"，这里可以通过它的class属性定位到这个元素。
# driver.get("http://www.baidu.com")
# ##备注，当有多个class时取其中一个： s_ipt nobg_s_fm_focus
# driver.find_element_by_class_name("s_ipt").send_keys("python")

# 2.2.6 find_element_by_tag_name()
# 1.从上面定位到的元素属性中，可以看到每个元素都有tag（标签）属性，如搜索框的标签属性，就是最前面的input。
# 2.很明显，在一个页面中，相同的标签有很多，所以一般不用标签来定位。以下例子，仅供参考和理解，运行肯定报错。
# driver.get("http://www.baidu.com")
# driver.find_element_by_tag_name("input").send_keys("python")


#  2.2.7 find_element_by_link_text()
# 1.定位百度页面上"hao123"这个按钮
# 查看页面元素：
# <a class="mnav" target="_blank" href="http://www.hao123.com">hao123</a>
# 2.从元素属性可以分析出，有个href = "http://www.hao123.com
#
# 说明它是个超链接，对于这种元素，可以用以下方法：
# driver.get("http://www.baidu.com")
# driver.find_element_by_link_text("hao123").click()


# 2.2.8 find_element_by_partial_link_text()
# 1.有时候一个超链接它的字符串可能比较长，如果输入全称的话，会显示很长，这时候可以用一模糊匹配方式，截取其中一部分字符串就可以了
# 2.如“hao123”,只需输入“ao123”也可以定位到
# driver.get("http://www.baidu.com")
# #partical_link是一种模糊匹配，对于超长的字符串，截取其中的一部分
# driver.find_element_by_partial_link_text("ao123").click()


# 2.2.9 find_element_by_xpath()
# 1.以上定位方式都是通过元素的某个属性来定位的，如果一个元素它既没有id、name、class属性也不是超链接，这么办呢？或者说它的属性很多重复的。这个时候就可以用xpath解决。
# 2.xpath是一种路径语言，跟上面的定位原理不太一样，首先第一步要先学会用工具查看一个元素的xpath。
# 3.按照上图的步骤，在FirePath插件里copy对应的xpath地址。
# driver.get("http://www.baidu.com")
# driver.find_element_by_xpath(".//*[@id='kw']").send_keys("python")

# 2.2.10 find_element_by_css_selector()
# 1.css是另外一种语法，比xpath更为简洁，但是不太好理解。这里先学会如何用工具查看，后续的教程再深入讲解
# 2.打开FirePath插件选择css
# 3.定位到后如下图红色区域显示

# driver.get("http://www.baidu.com")
# driver.find_element_by_css_selector("#kw").send_keys("hhhhh")

# 总结：
# selenium的webdriver提供了18种（注意是18种，不是8种）的元素定位方法，前面8种是通过元素的属性来直接定位的，后面的xpath和css定位更加灵活，需要重点掌握其中一个。
# 前八种是大家都熟悉的，经常会用到的：

# 1.id定位：find_element_by_id(self, id_)
# 2.name定位：find_element_by_name(self, name)
# 3.class定位：find_element_by_class_name(self, name)
# 4.tag定位：find_element_by_tag_name(self, name)
# 5.link定位：find_element_by_link_text(self, link_text)
# 6.partial_link定位find_element_by_partial_link_text(self, link_text)
# 7.xpath定位：find_element_by_xpath(self, xpath)
# 8.css定位：find_element_by_css_selector(self, css_selector）

# 这八种是复数形式（2.8和2.27章节有介绍）
# 9.id复数定位find_elements_by_id(self, id_)
# 10.name复数定位find_elements_by_name(self, name)
# 11.class复数定位find_elements_by_class_name(self, name)
# 12.tag复数定位find_elements_by_tag_name(self, name)
# 13.link复数定位find_elements_by_link_text(self, text)
# 14.partial_link复数定位find_elements_by_partial_link_text(self, link_text)
# 15.xpath复数定位find_elements_by_xpath(self, xpath)
# 16.css复数定位find_elements_by_css_selector(self, css_selector

# 这两种是参数化的方法，会在以后搭建框架的时候，会经常用到PO模式，才会用到这个参数化的方法（将会在4.2有具体介绍）
# 17.find_element(self, by='id', value=None)
# 18.find_elements(self, by='id', value=None)