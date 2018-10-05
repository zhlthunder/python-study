#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 前言
#     在web页面中经常会遇到table表格，特别是后台操作页面比较常见。本篇详细讲解table表格如何定位。
# 一、认识table
#     1.首先看下table长什么样，如下图，这种网状表格的都是table
# 二、table特征
#     1.table页面查看源码一般有这几个明显的标签：table、tr、th、td
#     2.<table>标示一个表格
#     3.<tr>标示这个表格中间的一个行
#     4.</th> 定义表头单元格
#     5.</td> 定义单元格标签，一组<td>标签将将建立一个单元格，<td>标签必须放在<tr>标签内

# 三、xpath定位table
#     1.举个例子：我想定位表格里面的“selenium自动化”元素，这里可以用xpath定位：.//*[@id='myTable']/tbody/tr[2]/td[1]
#  2.这里定位的格式是固定的，只需改tr和td后面的数字就可以了.如第二行第一列tr[2]td[1].
# 对xpath语法不熟悉的可以看这篇Selenium2+python自动化7-xpath定位
# 四、打印表格内容
#     1.定位到表格内文本值，打印出来，脚本如下：

url="file:///C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/selenium_d/selenium_weddriver%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/2.13%20table.html"
from selenium import  webdriver
driver=webdriver.Chrome()
driver.get(url)

# t=driver.find_element_by_xpath("//*[@id='myTable']/tbody/tr[2]/td[1]")
t=driver.find_element_by_xpath(".//*[@id='myTable']/tbody/tr[2]/td[1]")  ##和上面的方法定位结果相关，请知晓
print(t.text)


# 补充说明：有些小伙伴可能会遇到table在ifame上的情况，这时候就需要先切换iframe了。





















