#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from selenium import webdriver
import time
driver=webdriver.Firefox()

# 前言
# 大部分人在使用selenium定位元素时，用的是xpath定位，因为xpath基本能解决定位的需求。css定位往往被忽略掉了，其实css定位也有它的价值，css定位更快，语法更简洁。
# 这一篇css的定位方法，主要是对比上一篇的xpath来的，基本上xpath能完成的，css也可以做到。两篇对比学习，更容易理解。
# 2.4.1 css:属性定位
# 1.css可以通过元素的id、class、标签这三个常规属性直接定位到
# 2.如下是百度输入框的的html代码：
# <input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd"/>
# 3.css用#号表示id属性,如：#kw
# 4.css用.表示class属性，如：.s_ipt
# 5.css直接用标签名称，无任何标示符，如：input
driver.get("https://www.baidu.com")
##css通过id属性定位
# driver.find_element_by_css_selector("#kw").send_keys("python")
##css通过class属性定位
# driver.find_element_by_css_selector(".s_ipt").send_keys("python")
##css通过标签属性来定位，这里运行会报错，因为不唯一，主要是了解一下用法
# driver.find_element_by_css_selector("input").send_keys("python")


# 2.4.2 css:其它属性
# 1.css除了可以通过标签、class、id这三个常规属性定位外，也可以通过其它属性定位
# 2.以下是定位其它属性的格式
driver.get("http://www.baidu.com")
##css通过name属性定位
# driver.find_element_by_css_selector("[name='wd']").send_keys("python")
##css通过autocomplete属性定位
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys("python")
##css通过type属性来定位,不唯一
# driver.find_element_by_css_selector("[type='text']").send_keys("python")


# 2.4.3 css:标签
# 1.css页可以通过标签与属性的组合来定位元素
# driver.get("https://www.baidu.com")
# ##css通过标签和class属性的组合定位
# driver.find_element_by_css_selector("input.s_ipt").send_keys("python")
##css通过标签和id属性的组合定位
# driver.find_element_by_css_selector("input#kw").send_keys("python")
##css通过标签和其它属性组合定位
# driver.find_element_by_css_selector("input[autocomplete='off']").send_keys("python")


# 2.4.4 css:层级关系
# 1.在前面一篇xpath中讲到层级关系定位，这里css也可以达到同样的效果
# 2.如xpath：
#
# //form[@id='form']/span/input和
# //form[@class='fm']/span/input也可以用css实现

# driver.get("https://www.baidu.com")
##css通过层级关系定位
# driver.find_element_by_css_selector("form#form>span>input").send_keys("python")
##css通过层级关系定位
# driver.find_element_by_css_selector("form.fm>span>input").send_keys("python")


# 2.4.5 css:索引
# 1.以下图为例，跟上一篇一样：
# 2.css也可以通过索引option：nth-child(1)来定位子元素，这点与xpath写法用很大差异，其实很好理解，直接翻译过来就是第几个小孩。
##选择第1个option
# driver.find_element_by_css_selector("select#nr>option:nth-child(1)").click()
# ##选择第2个option
# driver.find_element_by_css_selector("select#nr>option:nth-child(2)").click()
# ##选择第3个option
# driver.find_element_by_css_selector("select#nr>option:nth-child(3)").click()


# 2.4.6 css:逻辑运算
# 1.css同样也可以实现逻辑运算，同时匹配两个属性，这里跟xpath不一样，无需写and关键字

# driver.get("http://www.baidu.com")
# driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys("python")


# 2.4.7 css:模糊匹配
# 1.css的模糊匹配contains('xxx'),网上虽然用各种资料显示能用，但是小编亲自试验了下，一直报错。
# 2.在各种百度后找到了答案：you can't do this withCSS selectors, because there is no such thing as:contains() in CSS.
# It was a proposal that was abandoned years ago.
# 非常遗憾，这个语法已经被抛弃了，所以这里就不用管这个语法了。
# css语法远远不止上面提到的，还有更多更强大定位策略，有兴趣的可以继续深入研究。官方说法，css定位更快，语法更简洁，但是xpath更直观，更好理解一些。
#























