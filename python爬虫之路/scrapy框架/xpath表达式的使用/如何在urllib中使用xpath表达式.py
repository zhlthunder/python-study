#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


##一般正则表达式和xpath表达式会混合使用，两种的区别是：
#xpath表达式：效率高
#正则表达式： 功能更强

#在urlib中，我们一样可以使用xpath来进行信息的提取，此时，你需要首先安装lxml模块，然后将网页数据通过lxml
# 下的etree转化为treedata的形式；
#q&a:安装完lxml却无法导入etree的问题

#重要：切记，python3.5及以上，在从lxml中导入etree时会提示“红色波浪线”，直接忽略，不影响正常使用
# 如果是强迫症，可以参考Q&A中的方法解决 （https://www.qnjslm.com/ITHelp/883.html）

import urllib.request
# from lxml import etree
from lxml import html  ##解决etree波浪线的问题

data=urllib.request.urlopen("http://www.baidu.com").read().decode("utf-8","ignore")
print(len(data))
# treedata=etree.HTML(data)
treedata=html.etree.HTML(data) ##解决etree波浪线的问题
title=treedata.xpath("//title/text()")
print(title)
print(type(title))
if(str(type(title))=="<class 'list'>"):
    pass
else: ##如果是迭代器的形式，就需用下面的方法把它转换成列表
    title=[i for i in title]

print(title)
print(type(title))


