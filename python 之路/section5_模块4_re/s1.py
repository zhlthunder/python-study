#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
# 参考：
# http://www.cnblogs.com/wupeiqi/articles/5501365.html

#re简介：
# 就其本质而言，这则表达式是一种小型的，高度专业化的编程语言；
# 它内嵌在python语言中，并通过re模块实现； 正则表达式被编译成一系列的字节码，然后
# 由用C编写的匹配引擎执行；

# 字符匹配 （普通字符  元字符）
# 普通字符匹配：大多数字符和字母都会和自身匹配

# import re
# print(re.findall('alex','yasudfafalexpeijf'))
# 输出：
# ['alex']
##findall 找到所有匹配到的字符串，并返回一个列表

##元字符匹配
#1）  .   匹配除换行符以外的任意一个字符，即只能匹配一个字符；
# import re
# print(re.findall('al.x','yasudfafalexpeijf'))
# print(re.findall('al.x','yasudfafalwxpeijf'))
# print(re.findall('al.x','yasudfafal\nxpeijf'))
# 输出：
# ['alex']
# ['alwx']
# []  ##无法匹配到换行符

#2）  ^  配置以什么开始；
# import re
# print(re.findall('^alex','yasudfafalexpeijf'))
# print(re.findall('^yas','yasudfafalexpeijf'))
# # 输出：
# []
# ['yas']

#3） $  匹配以什么结尾的
# import re
# print(re.findall('alex$','yasudfafalexpeijf'))
# print(re.findall('ijf$','yasudfafalexpeijf'))
# 输出：
# []
# ['ijf']

#4）*   重复元字符，即重复它前面的紧挨着的字符0及以上次
# import re
# print(re.findall('al.*x','yasaleudfafalexpeijf'))
# 输出：
# ['aleudfafalex']

# import re
# print(re.findall('al.*x','yaseudfafalxpeijf'))
# 输出：
# ['alx'] ##此处为匹配0次

#5） +   重复元字符，即重复它前面的紧挨着的字符1及以上次
# import re
# print(re.findall('al.*x','yaseudfafalxpeijf'))  ##匹配0次以上
# print(re.findall('al.+x','yaseudfafalxpeijf'))   #匹配1次以上
# 输出：
# ['alx']
# []

# import re
# print(re.findall('al.+x','yaseudfafalxpeijf'))
# print(re.findall('al.+x','yaseudfafalexpeijf'))
# print(re.findall('al.+x','yaseudfafaleeeexpeijf'))
# 输出：
# []
# ['alex']
# ['aleeeex']

#6） ？  重复元字符，即重复它前面的紧挨着的字符0~1次
# import re
# print(re.findall('al.?x','yaseudfafalxpeijf'))
# print(re.findall('al.?x','yaseudfafalexpeijf'))
# print(re.findall('al.?x','yaseudfafaleexpeijf'))
# 输出：
# ['alx']
# ['alex']
# []

#7）  {n}  重复元字符，即重复它前面的紧挨着的字符n次
# import re
# print(re.findall('al.{3}x','yaseudfafalexpeijf'))
# print(re.findall('al.{1,5}x','yaseudfafalexpeijf'))
# 输出：
# []
# ['alex']

# 说明：
# {3} 重复3次
# {1,3} 重复1~3次
# {,3} 重复0~3次
# {3,} 重复3次及以上

#8） [] 按特定的规则匹配一个字符
# import re
# print(re.findall('a[bc]d','abd'))
# print(re.findall('a[bc]d','acd'))
# print(re.findall('a[a-z]d','acd'))
# print(re.findall('a[a-z]d','acpd'))
# print(re.findall('a[a-z]+d','acpd')) ##此时的+就是对它前面的中括号进行重复
# 输出：
# ['abd']
# ['acd']
# ['acd']
# []
# ['acpd']

##，前面讲的元字符，如果是放在中括号里面，就不具有特殊的功能，就是一个普通字符
# import re
# print(re.findall('a[a*]d','aad'))
# print(re.findall('a[a*]d','a*d'))  #即在中括号中，* 不具有特殊的意义，只是代表他自己；
# 输出：
# ['aad']
# ['a*d']
##总结，所有的元字符，在中括号中都不具有特殊的意义，只代表字符自己；但有几个例外：
# 1>>   [a-z]  其中的 - 有特殊的意义，代表一个范围
#2>>  [^f]  其中的 ^ 有特殊的意义，表示 非
# import re
# print(re.findall('a[^f]d','aad'))
# print(re.findall('a[^f]d','afd'))
# 输出：
# ['aad']
# []
#3>>  [\d]  有特殊的功能，比如 \d表示数字
# import re
# print(re.findall('a[\d]d','aad'))
# print(re.findall('a[\d]d','a1d'))
# 输出：
# []
# ['a1d']

# 9)  \
# 反斜杠后面跟元字符去除特殊功能；
# 反斜杠后面跟普通字符实现特殊功能；
# 引用序号对应的字组所匹配的字符串；

#
# \d 匹配任何十进制数；它相当于 [0-9]
# \D 匹配任何非数字字符；它相当于[^0-9]
# \s 匹配任何空白字符，它相当于[\t\n\r\f\v]
# \S 匹配任何非空白字符，它相当于[^\t\n\r\f\v]
# \w 匹配字母或数字或下划线或汉字，它相当于[a-zA-Z0-9]及其它
# \W 匹配任何非字母数字字符，它相当于[^a-zA-Z0-9]
# \b 匹配一个单词边界，也就是指单词和空格间的位置
#     匹配单词边界（包括开始和结束），这里的“单词”，是指连续的字母，数字和下划线组成的字符串。注意
#    \b的定义是\w和\W的交界，这是个零宽界定符（zero-width assertions）只用于匹配单词的词首和词尾.
#       单词被定义为一个字母数字序列，因此词尾就是用空白符或非字母数字符来标识的。


# import re
# print(re.findall('I','I am handIsom'))
# print(re.findall(r'I\b','I am handIsom'))
# print(re.findall(r'I\b','I&am handIsom'))
# 输出：
# ['I', 'I']
# ['I']  ##只匹配到 单词 I， 以空格来进行匹配
# ['I']   ##只匹配到 单词 I， 以特殊字符&来进行匹配


#re 函数
#1) match
# re.match(pattern,string,flags=0)
#flags 编译标志位，用于修改正则表达式的匹配方式，如：是否区分大小写，多行匹配等； 一般不用使用这个标志位

import re
# print(re.match('com','comwww.runcomoob')) #返回匹配到的结果的对象
# 输出：
# <_sre.SRE_Match object; span=(0, 3), match='com'>
# print(re.match('com','comwww.runcomoob').group())  #取出匹配到的结果
# 输出：
# com

# a=re.match('com','comwww.runcomoob')
# print(a.span())
# 输出：
# (0, 3)

# a=re.match('com','www.runcomoob')
# print(a.span())
# 没有配置到，a 为 none
# ==> 所以 match 只能从开始位置进行匹配，如果匹配不到就返回none,

#2） search
# import re
# a=re.search('com','www.com.runcomob')
# print(a.span())
# 输出：  # 即找到第一个匹配的就返回了
# (4, 7)

# ==》小结一下：match 只能从字符串的起始位置开始进行匹配； search: 不限于从第一个位置，但匹配到
#    第一个后就返回了； 而finall 则会返回全部匹配的元素；


##一旦匹配成功，就返回一个match object 对象，而match object对象有以下的方法：
# group()  返回被RE匹配到的字符串；
# start() 返回匹配开始的位置；
# end() 返回匹配结束的位置；
# span()  返回一个元祖包含匹配（开始，结束）的位置


# 3) findall()  返回一个列表
#4) finditer()  返回一个迭代器，其它用法和findall 相似

#5）sub() 匹配替换
#re.sub(pattern,repl,string,max=0)  pattern：要匹配的格式；repl:要替换的字符串；string:被查找和替换的字符串
  #max 为最大替换次数
# import re
# print(re.sub('g.t',"have","i get A, I got B,i gut C"))
# 输出：
# i have A, I have B,i have C

# import re
# print(re.sub('g.t',"have","i get A, I got B,i gut C",2)) #最多替换两个
# 输出：
# i have A, I have B,i gut C

#6）subn 返回替换后的字符串及替换的次数，其它和sub相同
# import re
# print(re.sub('g.t',"have","i get A, I got B,i gut C"))
# print(re.subn('g.t',"have","i get A, I got B,i gut C"))
# 输出：
# i have A, I have B,i have C
# ('i have A, I have B,i have C', 3)

#7）split
# import re
# print(re.split('\d+','one1two2three3four4'))
# 输出：
# ['one', 'two', 'three', 'four', '']
# 注意，上面还有一个空格

#6） compile()
# re.compile(strpattern[,falg])
# 这个方法是pattern类的工厂方法，用于将字符串形式的正则表达式编译为
# pattern对象。第二个参数flag是匹配模式，取值可以使用按位或运算符'|'表示同时生效，比如re.I | re.M
# 可以把正则表达式编译成一个正则表达式对象，这样可以提高一定的效率。

# import re
# text="JGood is a handsome boy, he is cool,clever,and so on.."
# regex=re.compile(r'\w*oo\w*')  #查找所有包含'oo'的单词
# print(regex.findall(text))
# 输出：
# ['JGood', 'cool']


##原生表达式

# a=re.search(r'\\com','www.run\comoob')
# print(a.group())
# # 输出：
# # \com
# a=re.search('\\\\','www.run\comoob')  ##注意理解这里，需要\\\\ 才可以匹配到一个\
# print(a.group())
# # 输出：
##注意理解这里，需要\\\\ 才可以匹配到一个\
##为什么会这样呢？ 因为存在转义的问题；
#首先，python 是通过调用re来完成字符串匹配的。
 # 现在我们想匹配一个\ , 但在re中为了避免发生转义，需要用\\ 才可以匹配\,
 #而在python的语句中python解释器解释时，\ 也有转义的功能，所以如果想传递\\给re,就需要使用\\\\ 才可以实现，可见这种方法
 # 非常麻烦，于是就有了原生表达式这个东西

 # a=re.search('\\\\','www.run\comoob')
 # a=re.search(r'\\','www.run\comoob')  ##原生字符的表达方式
 #怎么理解呢？ 就是在python的代码中，直接用r""的形式告诉 python解释器，我要传递的就是两个\\的原生字符，不需要
 #转义，即re模块就拿到了 \\ 两个字符。
 # 即： \\\\  和 r'\\' 作用相似

##re中的\b 在python中也是特殊字符，所有下面的匹配时会报错
# print(re.search('\bam','Iww am w.run\con').group())  ##匹配不到，报错
# print(re.search(r'\bam','Iww am w.run\con').group())  ##使用原生字符，可以匹配到

##结论：以后进行正则匹配时，建议规定都使用 原生字符串，@@@重要

# 再举个例子：
# print(re.search('\bblow','blow').group()) #匹配不到
# print(re.search('\\bblow','blow').group()) #可以匹配到
# print(re.search(r'\bblow','blow').group()) #可以匹配到,使用的是原生字符

# a=re.search('\dblow','3blow')  #因为python 中没有 \d 的转义字符，所以可以匹配到
# print(a.group())

# ==》 总结： 建议使用原生字符的标准形式@@@@@@重要



##@@@@@正则表达式之分组
#分组的意思是，你该匹配就匹配，如果加了分组，就会去已经匹配到的内容中去取定义的分组
# 去已经提取到数据中再提取数据

#@1）match 支持分组
# 无分组
# import re
# origin="has dfuojqwlm88464"
# r = re.match("h\w+", origin)
# print(r.group())     # 获取匹配到的所有结果
# print(r.groups())    # 获取模型中匹配到的分组结果
# print(r.groupdict()) # 获取模型中匹配到的分组结果
# 输出：
# has
# ()
# {}


#有分组
# import re
# origin="has dfuojqwlm88464"
# r = re.match("h(\w+)", origin)  # 里面的（）对匹配没有任何影响，只是进行分组而已
# print(r.group())     # 获取匹配到的所有结果
# print(r.groups())    # 获取模型中匹配到的分组结果  #有分组的情况下，将匹配到的分组的内容放到groups中
# print(r.groupdict()) # 获取模型中匹配到的分组结果
# 输出：
# has
# ('as',)  ##匹配到的分组的部分，即从已经匹配到的结果中提取出分组的部分
# {}

#最基本的分组有两种方式，list形式 和 字典形式
#此处因为没有定义分组的名字，即没有定义key,所以取字典时取不到结果；


##分组
# import re
# origin="has dfuojqwlm88464"
# r = re.match("h(?P<name>\w+)", origin)  # 里面的?P<name>对匹配没有任何影响，只是把分区取了个名字，叫key
# print(r.group())     # 获取匹配到的所有结果
# print(r.groups())    # 获取模型中匹配到的分组结果  #有分组的情况下，将匹配到的分组的内容放到groups中
# print(r.groupdict()) # 获取模型中匹配到的分组结果

# 输出：
# has
# ('as',)
# {'name': 'as'}

##所以对于分组来说，本质上就是取已经分组的内容中再去获取一点东西；


##2)search  支持分组， 除了搜索方式为全部字符串搜索外，其它和match相同
#无分组
# import re
# origin="ttpaboy a good guy"
# r = re.search("a\w+", origin)
# print(r.group())     # 获取匹配到的所有结果
# print(r.groups())    # 获取模型中匹配到的分组结果
# print(r.groupdict()) # 获取模型中匹配到的分组结果
# 输出：
# aboy
# ()
# {}

#有分组：
# import re
# origin="ttpaboy a good guy"
# r = re.search("a(?P<key1>\w+)", origin)
# print(r.group())     # 获取匹配到的所有结果
# print(r.groups())    # 获取模型中匹配到的分组结果
# print(r.groupdict()) # 获取模型中匹配到的分组结果
# 输出：
# aboy
# ('boy',)
# {'key1': 'boy'}


#3） findall 支持分组
#无分组
# import re
# origin="has dfuojqhal wlm88464"
# r = re.findall("h\w+", origin)
# print(r)
# 输出：
# ['has', 'hal']

#有分组：
# import re
# origin="has dfuojqhal wlm88464"
# r = re.findall("(h\w+)", origin)
# print(r)
# 输出：  和上面没有分组是返回的相同；
# ['has', 'hal']

#有分组：
# import re
# origin="has dfuojqhal wlm88464"
# r = re.findall("h(\w+)", origin) #匹配的时候使用h(\w+)去整体匹配，返回时只返回分组（）中的部分
# print(r)
# 输出：
# ['as', 'al']

##有分组--多个分组的情况， 切记，整体匹配时和分组无关；
# import re
# origin="hasaabc dfuojqhalaabc wlm88464"
# r = re.findall("h(\w+)a(ab)c", origin)
# print(r)
# 输出：
# [('as', 'ab'), ('al', 'ab')]


#4） sub  都是整体匹配，并且整体替换，所以与分组无关；

#5）split

# 无分组
# origin = "hello alex bcd alex lge alex acd 19"
# r = re.split("alex", origin, 1)
# print(r)
# 输出：
# ['hello ', ' bcd alex lge alex acd 19']  #输出中没有分隔符 alex

# #有分组：
# origin = "hello alex bcd alex lge alex acd 19"
# r = re.split("(alex)", origin, 1)
# print(r)
# 输出：
# ['hello ', 'alex', ' bcd alex lge alex acd 19']  #输出中有分隔符 alex

#有分组：
# origin = "hello alex bcd alex lge alex acd 19"
# r = re.split("al(ex)", origin, 1)
# print(r)
# 输出：
# ['hello ', 'ex', ' bcd alex lge alex acd 19']


#有分组：@@重要，注意理解双层括号的情况
# origin = "hello alex bcd alex lge alex acd 19"
# r = re.split("(al(ex))", origin, 1)
# print(r)
# 输出：
# ['hello ', 'alex', 'ex', ' bcd alex lge alex acd 19']
#注意理解它的本质，就是取匹配到的结果中去取值，有几层括号就取几次值，从外向内匹配，逐个取值；

# origin = "hello alex bcd alex lge alex acd 19"
# r = re.split("(al(e(x)))", origin, 1)
# print(r)
# 输出：
# ['hello ', 'alex', 'ex', 'x', ' bcd alex lge alex acd 19']

#@@@@@@再次强调，python中正则的分组，就是取已经匹配到的结果中去取值；


# @@@从网站上抄录过来的

# python中re模块提供了正则表达式相关操作
# 字符：
#
# 　　. 匹配除换行符以外的任意字符
# 　　\w 匹配字母或数字或下划线或汉字
# 　　\s 匹配任意的空白符
# 　　\d 匹配数字
# 　　\b 匹配单词的开始或结束
# 　　^ 匹配字符串的开始
# 　　$ 匹配字符串的结束

# 次数：
#
#
#
# 　　* 重复零次或更多次
# 　　+ 重复一次或更多次
# 　　? 重复零次或一次
# 　　{n} 重复n次
# 　　{n,} 重复n次或更多次
# 　　{n,m} 重复n到m次


# match
# # match，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None
#
#
#  match(pattern, string, flags=0)
#  # pattern： 正则模型
#  # string ： 要匹配的字符串
#  # falgs  ： 匹配模式
#      X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
#      I  IGNORECASE  Perform case-insensitive matching.
#      M  MULTILINE   "^" matches the beginning of lines (after a newline)
#                     as well as the string.
#                     "$" matches the end of lines (before a newline) as well
#                     as the end of the string.
#      S  DOTALL      "." matches any character at all, including the newline.
#
#      A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
#                     match the corresponding ASCII character categories
#                     (rather than the whole Unicode categories, which is the
#                     default).
#                     For bytes patterns, this flag is the only available
#                     behaviour and needn't be specified.
#
#      L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
#      U  UNICODE     For compatibility only. Ignored for string patterns (it
#                     is the default), and forbidden for bytes patterns.


# # 无分组
#         r = re.match("h\w+", origin)
#         print(r.group())     # 获取匹配到的所有结果
#         print(r.groups())    # 获取模型中匹配到的分组结果
#         print(r.groupdict()) # 获取模型中匹配到的分组结果
#
#         # 有分组
#
#         # 为何要有分组？提取匹配成功的指定内容（先匹配成功全部正则，再匹配成功的局部内容提取出来）
#
#         r = re.match("h(\w+).*(?P<name>\d)$", origin)
#         print(r.group())     # 获取匹配到的所有结果
#         print(r.groups())    # 获取模型中匹配到的分组结果
#         print(r.groupdict()) # 获取模型中匹配到的分组中所有执行了key的组


# search
# # search,浏览整个字符串去匹配第一个，未匹配成功返回None
# # search(pattern, string, flags=0)

# # 无分组
#
#         r = re.search("a\w+", origin)
#         print(r.group())     # 获取匹配到的所有结果
#         print(r.groups())    # 获取模型中匹配到的分组结果
#         print(r.groupdict()) # 获取模型中匹配到的分组结果
#
#         # 有分组
#
#         r = re.search("a(\w+).*(?P<name>\d)$", origin)
#         print(r.group())     # 获取匹配到的所有结果
#         print(r.groups())    # 获取模型中匹配到的分组结果
#         print(r.groupdict()) # 获取模型中匹配到的分组中所有执行了key的组

# findall
# findall，获取非重复的匹配列表；如果有一个组则以列表形式返回，且每一个匹配均是字符串；如果模型中有多个组，则以列表形式返回，且每一个匹配均是元祖；
# 空的匹配也会包含在结果中
#findall(pattern, string, flags=0)

# # 无分组
#         r = re.findall("a\w+",origin)
#         print(r)
#
#         # 有分组
#         origin = "hello alex bcd abcd lge acd 19"
#         r = re.findall("a((\w*)c)(d)", origin)
#         print(r)
#
# Demo


# sub

# sub，替换匹配成功的指定位置字符串

# sub(pattern, repl, string, count=0, flags=0)
# pattern： 正则模型
# repl   ： 要替换的字符串或可执行对象
# string ： 要匹配的字符串
# count  ： 指定匹配个数
# flags  ： 匹配模式

        # 与分组无关

        # origin = "hello alex bcd alex lge alex acd 19"
        # r = re.sub("a\w+", "999", origin, 2)
        # print(r)


# split
# # split，根据正则匹配分割字符串
#
# split(pattern, string, maxsplit=0, flags=0)
# # pattern： 正则模型
# # string ： 要匹配的字符串
# # maxsplit：指定分割个数
# # flags  ： 匹配模式

# # 无分组
#         origin = "hello alex bcd alex lge alex acd 19"
#         r = re.split("alex", origin, 1)
#         print(r)
#
#         # 有分组
#
#         origin = "hello alex bcd alex lge alex acd 19"
#         r1 = re.split("(alex)", origin, 1)
#         print(r1)
#         r2 = re.split("(al(ex))", origin, 1)
#         print(r2)
#
# Demo
#
# 常用正则表达式：
# IP：
# ^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$
# 手机号：
# ^1[3|4|5|8][0-9]\d{8}$
# 邮箱：
# [a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+
#
# 常用正则表达式

