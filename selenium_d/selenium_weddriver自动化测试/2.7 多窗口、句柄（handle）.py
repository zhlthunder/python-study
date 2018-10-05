#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from selenium import webdriver
import time
driver=webdriver.Chrome()


# 前言
# 有些页面的链接打开后，会重新打开一个窗口，对于这种情况，想在新页面上操作，就得先切换窗口了。获取窗口的唯一标识用句柄表示，
# 所以只需要切换句柄，我们就能在多个页面上灵活自如的操作了。
# 一、认识多窗口
# 1.打开赶集网：http://bj.ganji.com/，点击招聘求职按钮会发现右边多了一个窗口标签
 # 2.我们用代码去执行点击的时候，发现界面上出现两个窗口，如下图这种情况就是多窗口了。即和手动点击不同
#  3.到这里估计有小伙伴纳闷了，手工点击是2个标签，怎么脚本点击就变成2个窗口了，这个在2.1里面讲过，脚本执行是不加载配置的，
# 手工点击是浏览器默认设置了新窗口打开方式为标签，这里用鼠标按住点二个标签，拖拽出来，也就变成2个窗口了，是一回事。

 # 二、获取当前窗口句柄
 #
 #    1.元素有属性，浏览器的窗口其实也有属性的，只是你看不到，浏览器窗口的属性用句柄（handle）来识别。
 #
 #    2.人为操作的话，可以通过眼睛看，识别不同的窗口点击切换。但是脚本没长眼睛，它不知道你要操作哪个窗口，这时候只能句柄来判断了。
 #
 #    3.获取当前页面的句柄：driver.current_window_handle

# driver.get("http://bj.ganji.com")
# driver.implicitly_wait(10)
# ##获取当前窗口句柄
# print(driver.current_window_handle)


# 三、获取所有句柄
#     1.定位赶集网招聘求职按钮，并点击
#     2.点击后，获取当前所有的句柄：window_handles
#

# driver.get("http://bj.ganji.com")
# driver.implicitly_wait(10)
# ##获取当前窗口句柄
# print(driver.current_window_handle)
# driver.find_element_by_link_text("北京招聘").click()
# print(driver.window_handles)

# 四、切换句柄
#
# 网上大部分教程都是些的第一种方法，小编这里新增一个更简单的方法，直接从获取所有的句柄list里面取值。
#
# 方法一（不推荐）：
#
#     1.循环判断是否与首页句柄相等
#
#     2.如果不等，说明是新页面的句柄
#
#     3.获取的新页面句柄后，可以切换到新打开的页面上
#
#     4.打印新页面的title,看是否切换成功
# 方法二：
#
#     1.直接获取all_h这个list数据里面第二个hand的值：all_h[1]

# driver.get("http://bj.ganji.com")
# driver.implicitly_wait(10)
# ##获取当前窗口句柄
# print(driver.current_window_handle)
# driver.find_element_by_link_text("北京招聘").click()
# all_handle=driver.window_handles
# driver.switch_to_window(all_handle[1])
# print(driver.title)


# 五、关闭新窗口，切回主页
#    1.close是关闭当前窗口，因为此时有两个窗口，用close可以关闭其中一个，quit是退出整个进程（如果当前有两个窗口，会一起关闭）。
#    2.切换到首页句柄：h
#    3.打印当前页面的title，看是否切换到首页了

driver.get("http://bj.ganji.com")
driver.implicitly_wait(10)
##获取当前窗口句柄
# print(driver.current_window_handle)
driver.find_element_by_link_text("北京招聘").click()
all_handle=driver.window_handles
driver.switch_to_window(all_handle[1])
time.sleep(3)
print(driver.title)
driver.switch_to_window(driver.window_handles[0])
print(driver.title)












