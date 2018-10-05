#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
#
# 前言
#     selenium并不是万能的，有时候页面上操作无法实现的，这时候就需要借助JS来完成了。
# 常见场景：
# 当页面上的元素超过一屏后，想操作屏幕下方的元素，是不能直接定位到，会报元素不可见的。这时候需要借助滚动条来拖动屏幕，使被
# 操作的元素显示在当前的屏幕上。滚动条是无法直接用定位工具来定位的。selenium里面也没有直接的方法去控制滚动条，这时候只能借助Js了，
# 还好selenium提供了一个操作js的方法:execute_script()，可以直接执行js的脚本。

# 一、JavaScript简介
#
# 1.JavaScript是世界上最流行的脚本语言，因为你在电脑、手机、平板上浏览的所有的网页，以及无数基于HTML5的手机App，交互逻辑
# 都是由JavaScript驱动的。简单地说，JavaScript是一种运行在浏览器中的解释型的编程语言。那么问题来了，为什么我们要学JavaScript？
#
# 2.有些特殊的操作selenium2+python无法直接完成的，JS刚好是这方面的强项，所以算是一个很好的补充。对js不太熟悉的，可以网上找下教程，简单了解些即可。

# 二、控制滚动条高度
# 1.滚动条回到顶部：
#
# js="var q=document.documentElement.scrollTop=0"
# driver.execute_script(js)
#
# 2.滚动条拉到底部
#
# js="var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
#
# 3.这里可以修改scrollTop 的值，来定位右侧滚动条的位置，0是最上面，10000是最底部

# from selenium import  webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("http://news.baidu.com/")
# driver.implicitly_wait(10)
# ##注意，对于不同的网页，此处的10000不一定对应的是底部
# js="var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# time.sleep(3)
# ##定位到最上面
# js="var q=document.documentElement.scrollTop=0"
# driver.execute_script(js)

# 三、横向滚动条
# 1.有时候浏览器页面需要左右滚动（一般屏幕最大化后，左右滚动的情况已经很少见了）。
#
# 2.通过左边控制横向和纵向滚动条scrollTo(x, y)
# js = "window.scrollTo(100,400);"
# driver.execute_script(js)
#
# 3.第一个参数x是横向距离，第二个参数y是纵向距离

# 四、Chrome浏览器
# 1.以上方法在Firefox上是可以的，但是用Chrome浏览器，发现不管用。
# 谷歌浏览器就是这么任性，不听话，于是用以下方法解决谷歌浏览器滚动条的问题。
# 2.Chrome浏览器解决办法：
#
# js = "var q=document.body.scrollTop=0"
# driver.execute_script(js)


# 五、元素聚焦
# 1.虽然用上面的方法可以解决拖动滚动条的位置问题，但是有时候无法确定我需要操作的元素
# 在什么位置，有可能每次打开的页面不一样，元素所在的位置也不一样，怎么办呢？
# 2.这个时候我们可以先让页面直接跳到元素出现的位置，然后就可以操作了。同样需要借助JS去实现。
# 3.元素聚焦：
# target = driver.find_element_by_xxxx()
# driver.execute_script("arguments[0].scrollIntoView();", target)

# 六、获取浏览器名称:driver.name
# 1.为了解决不同浏览器操作方法不一样的问题，可以写个函数去做兼容。
# 2.先用driver.name获取浏览器名称，然后用if语句做个判断


#七 scrollTo函数
# 楼下有个小伙伴说这个scrollTo函数不存在兼容性问题，小编借花献佛了。
# --scrollHeight 获取对象的滚动高度。
# --scrollLeft 设置或获取位于对象左边界和窗口中目前可见内容的最左端之间的距离。
# --scrollTop 设置或获取位于对象最顶端和窗口中可见内容的最顶端之间的距离。
#
# --scrollWidth 获取对象的滚动宽度。
#
# scrollTo函数不存在兼容性问题，直接用这个函数就可以了

#滚动到底部
# js = "window.scrollTo(0,document.body.scrollHeight)"
# driver.execute_script(js)
# #滚动到顶部
# js = "window.scrollTo(0,0)"
# driver.execute_script(js)

# 参考代码：
# coding:utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
print(driver.name)
## 回到顶部
#def scroll_top():
#        if driver.name == "chrome":
#               js = "var q=document.body.scrollTop=0"
#        else:
#                js = "var q=document.documentElement.scrollTop=0"
#        return driver.execute_script(js)
# 拉到底部
#def scroll_foot():
#       if driver.name == "chrome":
#                js = "var q=document.body.scrollTop=10000"
#        else:
#                js = "var q=document.documentElement.scrollTop=10000"
#        return driver.execute_script(js)
#滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
#滚动到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)
# 聚焦元素  (用法待确认？？？？)
target = driver.find_element_by_xxxx()
driver.execute_script("arguments[0].scrollIntoView();", target)

# JS功能还是很强大的，它还可以处理富文本、内嵌滚动条的问题。