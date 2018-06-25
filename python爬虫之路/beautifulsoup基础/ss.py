#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from bs4 import BeautifulSoup as bs
import urllib.request
data=urllib.request.urlopen("http://edu.iqianyue.com").read().decode("utf-8","ignore")
bs1=bs(data)

# print(data)
##格式化输出：
# print(bs1.prettify())   ##注意对比此处的格式的变化

#获取标签： bs对象.标签名
print(bs1.title)
#输出：<title>韬云教育</title>

#获取标签里面的文字： bs对象.标签名.string
print(bs1.title.string)
#输出：韬云教育

##获取标签名：bs对象.标签名.name
print(bs1.title.name)

##获取属性列表： bs对象.标签名.attrs
print(bs1.a.attrs)
# 输出：
# {'href': '#', 'class': ['navbar-brand']}

##获取某个属性对应的值：bs对象.标签名[属性名] 或bs对象.标签名.get(属性名)
print(bs1.a["class"]) ##方法1
print(bs1.a.get("class")) ##方法2
# 输出：
# ['navbar-brand']
# ['navbar-brand']

##提取所有某个节点的内容：bs对象.find_all（标签名）  bs对象.find_all（[标签名1,标签名2，。。。】）
print(bs1.find_all('a'))
bs1.find_all(['a','ul'])
print("-----------------------")
# 输出：返回全部的a标签：
# [<a class="navbar-brand" href="#">
# <img src="static/images/logo.png" style="height: 50px;margin-top:-15px;"/>
# </a>, <a href="static/../index">韬云教育</a>, <a href="static/../index_index_course">课程中心</a>, <a href="static/../index_index_teacher">专家师资</a>, <a href="/live/index.php">教学直播间</a>, <a class="dropdown-toggle" data-toggle="dropdown" href="#">
# 					联系我们
# 					<b class="caret"></b>
# </a>, <a href="static/../index_index_company">公司资质</a>, <a href="static/../index_index_about">联系我们</a>, <a href="static/../index_user_register">注册</a>, <a href="static/../index_user_login">登录</a>]


##提取所有子节点：bs对象.标签.contents  bs对象.标签.children
k1=bs1.ul.contents  ##得到的是一个列表
k2=bs1.ul.children  ##得到的是一个生成器
allulc=[i for i in k2] #再通过这种方式转换成列表
print(k1)
# 输出 全部的子标签（就是ul标签内部的所有的标签）
# ['\n', <li class="active"><a href="static/../index">韬云教育</a></li>, <li><a href="static/../index_index_course">课程中心</a></li>, <li><a href="static/../index_index_teacher">专家师资</a></li>, <li><a href="/live/index.php">教学直播间</a></li>, '\n', <li class="dropdown">
# <a class="dropdown-toggle" data-toggle="dropdown" href="#">
# 					联系我们
# 					<b class="caret"></b>
# </a>
# <ul class="dropdown-menu">
# <li><a href="static/../index_index_company">公司资质</a></li><li class="divider"></li><li><a href="static/../index_index_about">联系我们</a></li>
# </ul>
# </li>, '\n']


##更多的信息请参考：官方地址： http://beautifulsoup.readthedocs.io/zh_CN/latest/