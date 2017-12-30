#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import re
#正则表达式模块 re

#type 1:普通字符作为原子
# str="taoyunjiaoyu"
# pat="yun"
# result=re.search(pat,str)
# print(result)
# 输出：
# <_sre.SRE_Match object; span=(3, 6), match='yun'>

##type2:非打印字符作为原子
#\n换行符
#\t 制表符
# str='''taoyunjiaoyu
# baidu
# '''
# pat='\n'
# ret=re.search(pat,str)
# print(ret)
# 输出：
# <_sre.SRE_Match object; span=(12, 13), match='\n'>

#type3:通用字符作为原子
'''
\w  字母 数字 下划线
\W 除 字母 数字 下划线 之外的字符
\d 十进制数
\D 除 十进制数 之外的字符
\s 空白字符
\S 除空白字符 之外的字符
'''

# str="taoyun876912jiaoyu"
# pat='\d\d'
# ret=re.search(pat,str)
# print(ret)
# 输出：<_sre.SRE_Match object; span=(6, 8), match='87'>

# pat='\d\d\d'
# ret=re.search(pat,str)
# print(ret)
# 输出：<_sre.SRE_Match object; span=(6, 9), match='876'>

# pat='\w\d\d\d'
# ret=re.search(pat,str)
# print(ret)
# 输出：<_sre.SRE_Match object; span=(5, 9), match='n876'>

# str="taoyun6877 54jiaoyu"
# pat='\d\d\s\d'
# ret=re.search(pat,str)
# print(ret)
# 输出： <_sre.SRE_Match object; span=(8, 12), match='77 5'>

#type4:原子表
#[xyz]  表示匹配其中任意一个
# [^xyz] 表示匹配非xyz的字符
# str="taoyunjiaoyu"
# pat="tao[xyz]un"
# ret=re.search(pat,str)
# print(ret)

# 输出：<_sre.SRE_Match object; span=(0, 6), match='taoyun'>

# [^xyz] 表示提取非xyz的字符
# str="taoyunjiaoyu"
# pat="tao[^xyz]un"
# ret=re.search(pat,str)
# print(ret)
# 输出： None


#type5 :元字符
#所谓元字符，就是正则表达式中的有特殊含义的字符
'''
. 匹配除换行符以外的任意一个字符
^ 匹配开始位置
$ 匹配结束位置
* 重复匹配它前面的原子 0次，1次或多次
？重复匹配它前面的原子 0次或1次
+ 重复匹配它前面的原子 1次或多次
{n} 重复匹配它前面的原子 n次
{n,} 重复匹配它前面的原子 n次及以上
{n,m}重复匹配它前面的原子 至少n次，至多m次
| 模式选择符  “或”
（） 模式单元
'''

# str="taoyun87654321jiaoyu"
# pat="tao.un"
# ret=re.search(pat,str)
# print(ret)
# 输出： <_sre.SRE_Match object; span=(0, 6), match='taoyun'>

# str="taoyun87654321jiaoyu"
# pat="^taoy.."
# ret=re.search(pat,str)
# print(ret)
# # 输出：<_sre.SRE_Match object; span=(0, 6), match='taoyun'>
# pat="jiao..$"
# ret=re.search(pat,str)
# print(ret)
# # 输出：<_sre.SRE_Match object; span=(14, 20), match='jiaoyu'>
# pat="tao*"   #重复o 0次；
# ret=re.search(pat,str)
# print(ret)
# # 输出：<_sre.SRE_Match object; span=(0, 3), match='tao'>
# pat="tao.*" # .表示任意字符，*就可以重复0到任意次
# ret=re.search(pat,str)
# print(ret)
# # 输出：<_sre.SRE_Match object; span=(0, 20), match='taoyun87654321jiaoyu'>
# pat="tao+"  #此处注意理解， 0+要一起看，表示o重复了1次，即满足+的规则；
# ret=re.search(pat,str)
# print(ret)
# # 输出： <_sre.SRE_Match object; span=(0, 3), match='tao'>


# str="taoyunnnjiaoyu"
# pat="yun{2}"
# ret=re.search(pat,str)
# print(ret)
# 输出： <_sre.SRE_Match object; span=(3, 7), match='yunn'>
# 注意，此处得到的是 yunn 而不是 yunnn, 即n{2}要一起看
# pat="yun{2,}"
# ret=re.search(pat,str)
# print(ret)
# 输出：<_sre.SRE_Match object; span=(3, 8), match='yunnn'>


##模式修正符
# 所谓的模式修正符，即可以在不改变正则表达式的情况下，通过模式修正符改变正则表达式的含义，从而实现一些匹配结果的调整等功能；
'''
I 匹配时忽略大小写  **重点
M 多行匹配  **重点
L 本地化识别匹配
U unicode
S 让.匹配包括换行符  **重点
'''
# str="Python"
# pat="pyt"
# ret=re.search(pat,str)
# print(ret)
# 输出：None
# ret=re.search(pat,str,re.I)  #使用方法： re.模式修正符
# print(ret)
# 输出：<_sre.SRE_Match object; span=(0, 3), match='Pyt'>


##贪婪模式和懒惰模式
# 贪婪模式的核心点就是 尽可能多的匹配 ,比较模糊
# 懒惰模式的核心点就是 尽可能少的匹配，比较精准
# str="Pythony"
# pat="P.*y"  ##贪婪模式
# ret=re.search(pat,str)
# print(ret)
# 输出：
# <_sre.SRE_Match object; span=(0, 7), match='Pythony'>
# 说明：
# P.*y ： 可以匹配成 Py 或Pythony，但因为默认是贪婪模式，所以会尽可能多的去匹配

# pat2="P.*?y" ##懒惰模式，把（.*?）当成一个整体来看，表示.*按懒惰模式进行匹配，所以只匹配成Py
# ret=re.search(pat2,str)
# print(ret)
# 输出：<_sre.SRE_Match object; span=(0, 2), match='Py'>
# 注意区分：
# ？有两种用法，1）表示懒惰模式 2）表示 重复匹配它前面的原子 0次或1次
##如何区分，如果？前面的是一个原子，则为方法2， 如果？前已经是一个匹配规则了，比如.*,表示方法1


##正则表达式函数：
# 正则表达式函数有 re.match() 函数，re.search() 函数， 全局匹配函数，re.sub()函数。
# match()  ,只能从开始位置进行匹配
# str="pythonasdfasy"
# pat="p.*?y"
# ret=re.match(pat,str)
# print(ret)
# # 输出： <_sre.SRE_Match object; span=(0, 2), match='py'>
# pat="f.*?y"
# ret=re.match(pat,str)
# print(ret)
# 输出：None
#总结： match() 必须是字符串的开始位置进行匹配的。

#全局匹配函数
# str="pythopnyaaapty"
# pat="p.*?y"
# ret1=re.match(pat,str)  ##只匹配一组就结束了
# print(ret1)
# ret2=re.search(pat,str)  ##只匹配一组就结束了
# print(ret2)
# ret3=re.compile(pat).findall(str)  ##全局匹配
# # 全局匹配格式：re.compile(正则表达式).findall(数据)
# print(ret3)
# 输出：
# <_sre.SRE_Match object; span=(0, 2), match='py'>
# <_sre.SRE_Match object; span=(0, 2), match='py'>
# ['py', 'pny', 'pty']

##常见的正则实例
# 比如如何匹配.com .cn网站，匹配电话号码等
# str="<a href=http://www.baidu.com,ftp://www.google.cn>百度首页</a>"
# pat="[a-zA-Z]+://[^\s]*[.com|.cn]"
# ret=re.compile(pat).findall(str)
# print(ret)
# 输出：['http://www.baidu.com,ftp://www.google.cn']

#匹配电话号码
# str="asdfsafdasfdasfd021-123456788888asdfsfd0772-12345677777"
# pat="\d{3}-\d{8}|\d{4}-\d{7}"
# ret=re.compile(pat).findall(str)
# print(ret)
# 输出：['021-12345678', '0772-1234567']





