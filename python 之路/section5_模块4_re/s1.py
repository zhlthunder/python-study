#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

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

# 9)  \   重要的一点，前面提到的元字符，如果和\组合，就失去特殊的功能了；