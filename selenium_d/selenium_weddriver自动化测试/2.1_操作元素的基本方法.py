#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
from selenium import webdriver
import time
driver=webdriver.Firefox()

# 2.1.1 打开网页
#
# 1.从selenium里面导入webdriver模块
# 2.打开Firefox浏览器（Ie和Chrome对应下面的）
# 3.打开百度网址


# driver=webdriver.Firefox() ##火狐浏览器
# driver=webdriver.Ie() ##for ie
# driver=webdriver.Chrome() # for chrome
# driver.get("http://www.baidu.com")


# 2.1.2 设置休眠
#
# 1.由于打开百度网址后，页面加载需要几秒钟，所以最好等到页面加载完成后再继续下一步操作
# 2.导入time模块，time模块是Python自带的，所以无需下载
# 3.设置等待时间，单位是秒（s）,时间值可以是小数也可以是整数

# driver.get("http://www.baidu.com")
#显示等待
# time.sleep(5)
##隐式等待（智能等待），即最多等待多久
# driver.implicitly_wait(10)
# print("页面加载完毕")

# 2.1.3 页面刷新
#
# 1.有时候页面操作后，数据可能没及时同步，需要重新刷新
# 2.这里可以模拟刷新页面操作，相当于浏览器输入框后面的刷新按钮
# driver.get("http://www.baidu.com")
# time.sleep(5)
# #等待5s后刷新一下页面
# driver.refresh()

# 2.1.4 页面切换
#
# 1.当在一个浏览器打开两个页面后，想返回上一页面，相当于浏览器左上角的左箭头按钮。
#
# 2.返回到上一页面后，也可以切换到下一页，相当于浏览器左上角的右箭头按钮。

# driver.get("http://www.baidu.com")
# time.sleep(5)
# driver.get("http://www.hordehome.com")
# time.sleep(5)
# ##返回上一页
# driver.back()
# time.sleep(3)
# ##切换到下一页面
# driver.forward()

# 2.1.5 设置窗口大小
#
# 1.可以设置浏览器窗口大小，如设置窗口大小为手机分辨率540*960
# 2.也可以最大化窗口
# driver.get("http://www.baidu.com")
# time.sleep(3)
# ##设置窗口大小540*960
# driver.set_window_size(540,960)
# time.sleep(3)
# ##浏览器窗口最大化
# driver.maximize_window()

#  2.1.6 截屏
#
# 1. 打开网站之后，也可以对屏幕截屏
# 2.截屏后设置指定的保存路径+文件名称+后缀

# driver.get("http://www.baidu.com")
# time.sleep(3)
# driver.get_screenshot_as_file("./screenshot.png")


# 2.1.7 退出
#
# 1.退出有两种方式，一种是close;另外一种是quit。
# 2.close用于关闭当前窗口，当打开的窗口较多时，就可以用close关闭部分窗口。
# 3.quit用于结束进程，关闭所有的窗口。
# 4.最后结束测试，要用quit。quit可以回收c盘的临时文件。

# driver.get("http://www.baidu.com")
# time.sleep(3)
# # driver.close()##关闭当前窗口
# driver.quit() #退出浏览器进程，关闭所有窗口


# 2.1.8 加载浏览器配置
#
# 启动浏览器后，发现右上角安装的插件不见了，这是因为webdriver启动浏览器时候，
# 是开的一个虚拟线程，跟手工点开是有区别的，selenium的一切操作都是模拟人工（不完全等于人工操作）。

# 加载Firefox配置
#
#    有小伙伴在用脚本启动浏览器时候发现原来下载的插件不见了，无法用firebug在打开的页面上继续定位页面元素，
# 调试起来不方便 。加载浏览器配置，需要用FirefoxProfile(profile_directory)这个类来加载，profile_directory既为浏览器配置文件的路径地址。

# 设置的方法是配置：FirefoxProfile 类；，它的解释如下:
# 这个类初始化时，需要用到：profile_directory
# profile_directory=None，如果没有路径，默认为None，启动的是一个新的，有的话就加载指定的路径。
# Firefox的配置文件地址如何找到呢？
# 打开Firefox点右上角设置>？（帮助）>故障排除信息>显示文件夹
#得到的配置路径为：C:\Users\lin\AppData\Roaming\Mozilla\Firefox\Profiles\5ickf9vm.default-1478654411172

# 启动配置文件
# 1.由于文件路径存在字符：\ ，反斜杠在代码里是转义字符，这个有点代码基础的应该都知道。
# 不懂什么叫转义字符的，自己翻书补下基础吧！
# 2.遇到转义字符，为了不让转义，有两种处理方式：
# 第一种：\ (前面再加一个反斜杠)
#
# 第二种:r”\"（字符串前面加r，使用字符串原型)


# 配置文件地址
profile_directory = r'C:\Users\lin\AppData\Roaming\Mozilla\Firefox\Profiles\5ickf9vm.default-1478654411172'
# 加载配置配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
driver = webdriver.Firefox(profile)
driver.get('http://www.baidu.com')
# 其实很简单，在调用浏览器的前面，多加2行代码而已，主要是要弄清楚原理。