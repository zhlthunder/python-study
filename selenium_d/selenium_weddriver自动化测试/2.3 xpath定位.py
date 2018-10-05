#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from selenium import webdriver
import time
driver=webdriver.Firefox()


# 前言
# 在上一篇简单的介绍了用工具查看目标元素的xpath地址，工具查看比较死板，不够灵活，有时候直接复制粘贴会定位不到。这个时候就需要自己手动的去写xpath了，这一篇详细讲解xpath的一些语法。
# 什么是xpath呢？
# 官方介绍：XPath即为XML路径语言，它是一种用来确定XML文档中某部分位置的语言。反正小编看这个介绍是云里雾里的，通俗一点讲就是通过元素的路径来查找到这个元素的。
#
# 2.3.1 xpath:属性定位
# 1.xptah也可以通过元素的id、name、class这些属性定位，如下图：
# 2.于是可以用以下xpath方法定位
# driver.get("http://www.baidu.com")
# #用xpath通过id属性来定位
# # driver.find_element_by_xpath("//*[@id='kw']").send_keys("python")
# # #用xpath通过name属性来定位
# # driver.find_element_by_xpath("//*[@name='wd']").send_keys("python")
# #用xpath通过class属性来定位
# driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("python")

# 2.3.2 xpath:其它属性
# 1.如果一个元素id、name、class属性都没有，这时候也可以通过其它属性定位到
#
# 2.3.3 xpath:标签
# 1.有时候同一个属性，同名的比较多，这时候可以通过标签筛选下，定位更准一点
# 2.如果不想制定标签名称，可以用*号表示任意标签
# 3.如果想制定具体某个标签，就可以直接写标签名称

driver.get("http://www.baidu.com")
##用xpath通过其它属性来定位
# driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys("python")
##用xpath,指定标签名，通过id属性来定位
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("python")
##用xpath,指定标签名，通过name属性来定位
# driver.find_element_by_xpath("//*[@name='wd']").send_keys("python")


# 2.3.4 xpath:层级
# 1.如果一个元素，它的属性不是很明显，无法直接定位到，这时候我们可以先找它老爸（父元素）。
# 2.找到它老爸后，再找下个层级就能定位到了。
# 3.如上图所示，要定位的是input这个标签，它的老爸的id=s_kw_wrap。
# 4.要是它老爸的属性也不是很明显，就找它爷爷id=form。
# 5.于是就可以通过层级关系定位到。

# driver.get("http://www.baidu.com")
##通过定位它老爸来定位input输入框，定位时发生报错，可能是不唯一造成的。
# driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input").send_keys("python")
##通过定位它爷爷来定位input输入框,下面两种方式相同
# driver.find_element_by_xpath('//form[@id="form"]/span/input').send_keys("python")
# driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("python")


# 2.3.5 xpath:索引
# 1.如果一个元素它的兄弟元素跟它的标签一样，这时候无法通过层级定位到。因为都是一个父亲生的，多胞胎兄弟。
# 2.虽然双胞胎兄弟很难识别，但是出生是有先后的，于是可以通过它在家里的排行老几定位到。
# 3.如下图三胞胎兄弟。
# 4.用xpath定位老大、老二和老三（这里索引是从1开始算起的，跟Python的索引不一样）。

# ##用xpath定位老大
# driver.find_element_by_xpath("//select[@id='nr']/option[1]").click()
# ##用xpath定位老二
# driver.find_element_by_xpath("//select[@id='nr']/option[2]").click()

# 2.3.6 xpath:逻辑运算
# 1.xpath还有一个比较强的功能，是可以多个属性逻辑运算的，可以支持与（and）、或（or）、非（not）
# 2.一般用的比较多的是and运算，同时满足两个属性
# driver.get("http://www.baidu.com")
# #xpath逻辑运算
# driver.find_element_by_xpath("//*[@id='kw' and @autocomplete='off']").send_keys("python")

#
# 2.3.7 xpath:模糊匹配
# 1.xpath还有一个非常强大的功能，模糊匹配。
# 2.掌握了模糊匹配功能，基本上没有定位不到的。
# 3.比如我要定位百度页面的超链接“hao123”,在上一篇中讲过可以通过by_link,也可以通过by_partial_link，模糊匹配定位到。当然xpath也可以有同样的功能，并且更为强大。

driver.get("https://www.baidu.com")
##xpath模糊匹配功能
# driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()
# driver.find_element_by_xpath("//*[contains(text(),'o123')]").click()

##xpath也可以模糊匹配某个属性
# driver.find_element_by_xpath("//*[contains(@id,'kw')]").send_keys("python")
##xpath模糊匹配以什么开头,定位失败，应该是不唯一的问题，同上
# driver.find_element_by_xpath("//*[starts-with(@id,'s_kw_')]/input").send_keys("python")
##xpath模糊匹配以什么结束,定位失败，应该是不唯一的问题，同上
# driver.find_element_by_xpath("//*[ends-with(@id,'kw_wrap')]/input").send_keys("python")
#xpath支持最强的正则表达式,定位失败，原因待排查
driver.find_element_by_xpath("//*[match(text(),'hao123')]").click()






