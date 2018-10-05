#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 前言
#     日历控件是web网站上经常会遇到的一个场景，有些输入框是可以直接输入日期的，有些不能，以我们经常抢票的12306网站为例，详细讲解如何解决日历控件为readonly属性的问题。
#     基本思路：先用js去掉readonly属性，然后直接输入日期文本内容
# 一、日历控件
#     1.打开12306的车票查询界面，在出发日期输入框无法直接输入时间
#     2.常规思路是点开日历控件弹出框，从日历控件上点日期，这样操作比较烦躁，并且我们测试的重点不在日历控件上，只是想输入个时间，做下一步的操作
#     3.用firebug查看输入框的属性：readonly="readonly"，如下：


 # 二、去掉readonly属性
 #
 #    1.很明显这种元素的属性是readonly，输入框是无法直接输入的，这时候需要先去掉元素的readonly属性，然后就可以输入啦。
 #
 #    2.点左下角firebug的“编辑按钮”，找到对应元素，直接删除readonly="readonly"，然后回车。
 #
 #    3.在页面出发日位置输入：yoyoketang 试试，嘿嘿，有没有发现可以输入成功。当然这里只是为了验证可以输入内容，测试时候还是输入测试的日期。


 # 三、用js去掉readonly属性
 #    1.用js去掉元素属性基本思路：先定位到元素，然后用removeAttribute("readonly")方法删除属性。
 #    2.出发日元素id为：train_date，对应js代码为：'document.getElementById("train_date").removeAttribute("readonly");'
from selenium import  webdriver
driver=webdriver.Chrome()
driver.get("https://kyfw.12306.cn/otn/index/init")
driver.implicitly_wait(30)
##去掉元素怒的readonly 属性
js='document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)

# 四、输入日期
#     1.输入日期前，一定要先清空文本，要不然无法输入成功的。
#     2.这里输入日期后，会自动弹出日历控件，随便点下其它位置就好了，接下来会用js方法传入日期，就不会弹啦！

# driver.find_element_by_id("train_date").clear()
# driver.find_element_by_id("train_date").send_keys("2018-10-15")


# 五、js方法输入日期
#    1.这里也可以用js方法输入日期，其实很简单，直接改掉输入框元素的value值就可以啦。
#用js的方法输入日期：
js_value='document.getElementById("train_date").value="2018-10-01"'
driver.execute_script(js_value)

# 代码参考：
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("https://kyfw.12306.cn/otn/index/init")
# # 去掉元素的readonly属性
# js = 'document.getElementById("train_date").removeAttribute("readonly");'
# driver.execute_script(js)
# # 用js方法输入日期
# js_value = 'document.getElementById("train_date").value="2016-12-25"'
# driver.execute_script(js_value)
# # # 清空文本后输入值
# # driver.find_element_by_id("train_date").clear()
# # driver.find_element_by_id("train_date").send_keys("2016-12-25")





