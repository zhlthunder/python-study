#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from selenium import webdriver
import time
driver=webdriver.Chrome()


# 一、frame和iframe区别
# Frame与Iframe两者可以实现的功能基本相同，不过Iframe比Frame具有更多的灵活性。 frame是整个页面的框架，iframe是内嵌的网页元素，也可以说是内嵌的框架
# Iframe标记又叫浮动帧标记，可以用它将一个HTML文档嵌入在一个HTML中显示。它和Frame标记的最大区别是在网页中嵌入 的<Iframe></Iframe>所包含的内容与整个页面是一个整体，
# 而<Frame>< /Frame>所包含的内容是一个独立的个体，是可以独立显示的。另外，应用Iframe还可以在同一个页面中多次显示同一内容，而不必重复这段内 容的代码。

#  三、切换iframe
# 1.由于登录按钮是在iframe上，所以第一步需要把定位器切换到iframe上
# 2.用switch_to_frame方法切换，此处有id属性，可以直接用id定位切换

# driver.get("http://mail.163.com/")
# driver.implicitly_wait(30) ##重要，这里的时间如果太短，会导致frame还没有加载完成，会提示找不要frame的报错信息
# ##切换iframe
# driver.switch_to_frame("x-URS-iframe")
# driver.find_element_by_name("email").send_keys("123")
# driver.find_element_by_name("password").send_keys("456")


# 四、如果iframe没有id怎么办？
# 1.这里iframe的切换是默认支持id和name的方法的，当然实际情况中会遇到没有id属性和name属性为空的情况，这时候就需要先定位iframe元素对象
# 2.定位元素还是之前的八种方法同样适用，这里我可以通过tag先定位到，也能达到同样效果
driver.get("http://mail.163.com/")
driver.implicitly_wait(30) ##重要，这里的时间如果太短，会导致frame还没有加载完成，会提示找不要frame的报错信息
#切换iframe
iframe=driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(iframe)
driver.find_element_by_name("email").send_keys("123")
driver.find_element_by_name("password").send_keys("456")

# 五、释放iframe
# 1.当iframe上的操作完后，想重新回到主页面上操作元素，这时候，就可以用switch_to_default_content()方法返回到主页面
# driver.get("http://mail.163.com/")
# driver.implicitly_wait(30) ##重要，这里的时间如果太短，会导致frame还没有加载完成，会提示找不要frame的报错信息
# ##切换iframe
# driver.switch_to_frame("x-URS-iframe")
# driver.find_element_by_name("email").send_keys("123")
# driver.find_element_by_name("password").send_keys("456")
# ##释放iframe,重新回到主页面上
# driver.switch_to_default_content()


# 六、如何判断元素是否在iframe上？
# 1.定位到元素后，切换到firepath界面
# 2.看firebug工具左上角，如果显示Top Window说明没有iframe
# 3.如果显示iframe#xxx这样的，说明在iframe上，#后面就是它的id




# 七、如何解决switch_to_frame上的横线呢？
# 1.先找到官放的文档介绍
# 2.python的脚本上面划一横线，是说这个语法已经过时了（也可以继续用，只是有部分人有强迫症）。
# 上面文档介绍说官方已经不推荐上面的写法了，用这个写法就好了driver.switch_to.frame()


# 参考代码：
# coding:utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://mail.163.com/")
driver.implicitly_wait(30)
# 切换iframe
# iframe = driver.find_element_by_tag_name("iframe")
# driver.switch_to_frame(iframe)
# driver.switch_to_frame("x-URS-iframe")
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys("123")
driver.find_element_by_name("password").send_keys("456")
# 释放iframe，重新回到主页面上
driver.switch_to.default_content()



