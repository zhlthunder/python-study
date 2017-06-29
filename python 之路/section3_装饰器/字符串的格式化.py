#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# @@@补充确认学习：
#截止目前共两种字符串格式化的方式：
# %方式  ：更老一些
# .format 方式  ##功能更强大


# 1、百分号方式
#
#     %[(name)][flags][width].[precision]typecode
#
#     (name)      可选，用于选择指定的key
#     flags          可选，可供选择的值有:
#         +       右对齐；正数前加正好，负数前加负号；
#         -        左对齐；正数前无符号，负数前加负号；
#         空格    右对齐；正数前加空格，负数前加负号；
#         0        右对齐；正数前无符号，负数前加负号；用0填充空白处
#     width         可选，占有宽度
#     .precision   可选，小数点后保留的位数
#     typecode    必选

# s="发发发 %s 顶顶顶顶顶 %d"%('alex',123)  #按顺序替换占位符
# print(s)
# # 输出：
# 发发发 alex 顶顶顶顶顶 123


# (name)   @@@
# s="发发发 %(name)s 顶顶顶顶顶 %(age)d" %{'name':'alex','age':123} #按key:value的方式提供值，即以字典的方式提供值去替换占位符
# print(s)
# 输出：
# 发发发 alex 顶顶顶顶顶 123

#[flags][width]  @@flag一定要配合宽度使用采用意义


# s="aaaa%+sbbbb"%('alex')
# print(s)
# #没有位宽，所有无差异
#
# s="aaaa%+10sbbbb"%('alex')
# print(s)
#
# s="aaaa%-10sbbbb"%('alex')
# print(s)
# 输出：
# aaaaalexbbbb
# aaaa      alexbbbb
# aaaaalex      bbbb

## flag 对于%d 的数字，会按一定的规律在数字的前面加上符号
# s="%-10s###%+d"%('alex',123)
# print(s)
# s="%-10s###%+d"%('alex',-123)
# print(s)
# s="%-10s###%-d"%('alex',123)
# print(s)
# s="%-10s###%-d"%('alex',-123)
# print(s)

# 输出：
# alex      ###+123
# alex      ###-123
# alex      ###123
# alex      ###-123

#     flags          可选，可供选择的值有:
#         +       右对齐；正数前加正好，负数前加负号；
#         -        左对齐；正数前无符号，负数前加负号；
#         空格    右对齐；正数前加空格，负数前加负号；
#         0        右对齐；正数前无符号，负数前加负号；用0填充空白处


##配置小数的精度，且支持
# s="##%s####%f"%('alex',1.223123)
# print(s)
# s="##%s####%.2f"%('alex',1.223123)
# print(s)
# 输出：
##alex####1.223123
##alex####1.22


# s="---%c----%o---%x"%(65,15,15)
# print(s)
# # 输出：
# # ---A----17---f
# #65直接转换成ASCII对应的字符A； 15转换成8进制的 17; 15 转换成16进制的f；


# s="--------%e---%E"%(100000000,20000000)
# print(s)
# 输出：
# --------1.000000e+08---2.000000E+07


##g 根据数字的大小，自动在e和f 之间进行切换；  切换的依据是，超过6位数用e的方式处理；
# s="--------%g"%(100000000)
# print(s)
# s="--------%g"%(1000)
# print(s)
# 输出：
# --------1e+08
# --------1000

###%的用法
# s1="alex %"
# print(s1)
# 输出：alex %

# s1="alex %s %%"%('SB')
# print(s1)
# 输出： alex SB %

# s1="alex %s %"%('SB')  ##这样写会报错
# print(s1)
#总结：当格式化时如果一个字符串中没有占位符的话，你写几个％就输出几个％，一旦有占位符的话，就必须写　％％表示 %； 切记；
# 类似转意的效果；


# 常用格式化就是如下几种方式：

# tpl = "i am %s" % "alex"
#
# tpl = "i am %s age %d" % ("alex", 18)
#
# tpl = "i am %(name)s age %(age)d" % {"name": "alex", "age": 18}
#
# tpl = "percent %.2f" % 99.97623
#
# tpl = "i am %(pp).2f" % {"pp": 123.425556, }
#
# tpl = "i am %.2f %%" % {"pp": 123.425556, }


###format方式：

# s1="#######{0}####{0}####{1}".format(123,'alex')
# print(s1)
# 输出：
# #######123####123####alex


# s1="#######{name:s}######{age:d}".format(name='alex',age=123)
# print(s1)
# 输出：
# #######alex######123

# 冒号前面有name,就按照有name的方式赋值，如果没有，就按照顺序赋值；
# s2="-----{:9^20s}------".format('alex')  #9位填充字符；^ 这个符号为居中； 20 表示宽度； s表示字符串方式
# print(s2)
# 输出：
# -----99999999alex99999999------


# s2="-----{:9^20s}@@@@@{:+d}".format('alex',123)
# print(s2)
# s2="-----{:9^20s}@@@@@{:+d}".format('alex',-123)
# print(s2)
# s2="-----{:9^20s}@@@@@{:-d}".format('alex',123)
# print(s2)
# s2="-----{:9^20s}@@@@@{:-d}".format('alex',-123)
# print(s2)
# 输出：
# -----99999999alex99999999@@@@@+123
# -----99999999alex99999999@@@@@-123
# -----99999999alex99999999@@@@@123
# -----99999999alex99999999@@@@@-123




# s1="---------{:b}".format(15)
# print(s1)
# s1="---------{:#b}".format(15)
# print(s1)
# s1="---------{:#o}".format(15)
# print(s1)
# s1="---------{:o}".format(15)
# print(s1)
# s1="---------{:x}".format(15)
# print(s1)
# s1="---------{:#x}".format(15)
# print(s1)
#
# 输出：
# ---------1111
# ---------0b1111
# ---------0o17
# ---------17
# ---------f
# ---------0xf


# s3="aaaaaaa{:%}".format(0.2345)  #直接转换成百分数
# print(s3)
# 输出：
# aaaaaaa23.450000%


##总结：
# 1.format 支持 填充任意字符；
# 2.format支持居中；
# 3.format 支持二进制；
#4. % 有特殊的功能，自动转换成百分号


# 常用格式化：
#  tpl = "i am {}, age {}, {}".format("seven", 18, 'alex')  #只有一个空的{}，表示不论类型，所有的都可以按照顺序进行替换；
#
# tpl = "i am {}, age {}, {}".format(*["seven", 18, 'alex']) ##如果以列表的方式进行传递，必须要加*，就可以按照顺序逐个进行替换；
#
# tpl = "i am {0}, age {1}, really {0}".format("seven", 18) ##指定索引的情况下，按照索引进行替换
#
# tpl = "i am {0}, age {1}, really {0}".format(*["seven", 18]) ##列表方式
#
# tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18) ##指定名字的方式
#
# tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18}) ##用字典的方式
#
# tpl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33]) ##索引中嵌套索引，复用的方式
#
# tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1) ##指定占位符的类型
#
# tpl = "i am {:s}, age {:d}".format(*["seven", 18])
#
# tpl = "i am {name:s}, age {age:d}".format(name="seven", age=18)
#
# tpl = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})
#
# tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2) ##不同进制的转换
#
# tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
#
# tpl = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
#
# tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)

# 更多格式化操作：https://docs.python.org/3/library/string.html









#没有仔细阅读，是直接copy的，需要抽空再看看
# remark:字符串格式化
# http://www.cnblogs.com/wupeiqi/articles/5484747.html

#%s %d 称为占位符

# s="测试字符串格式化%s %d"% ('alex',123)
# print(s)
# 输出：
# 测试字符串格式化alex 123

# dic={'name':'alex','age':123}
# s="测试字符串格式化 {name} {age}".format(**dic)
# print(s)

# 输出：
# 测试字符串格式化 alex 123

# 字符串格式化
# Python的字符串格式化有两种方式: 百分号方式、format方式
#
# 百分号的方式相对来说比较老，而format方式则是比较先进的方式，企图替换古老的方式，目前两者并存。[PEP-3101]
#
# This PEP proposes a new system for built-in string formatting operations, intended as a replacement for the existing '%' string formatting operator.
#
# 1、百分号方式
#
#     %[(name)][flags][width].[precision]typecode
#
#     (name)      可选，用于选择指定的key
#     flags          可选，可供选择的值有:
#         +       右对齐；正数前加正好，负数前加负号；
#         -        左对齐；正数前无符号，负数前加负号；
#         空格    右对齐；正数前加空格，负数前加负号；
#         0        右对齐；正数前无符号，负数前加负号；用0填充空白处
#     width         可选，占有宽度
#     .precision   可选，小数点后保留的位数
#     typecode    必选
#         s，获取传入对象的__str__方法的返回值，并将其格式化到指定位置
#         r，获取传入对象的__repr__方法的返回值，并将其格式化到指定位置
#         c，整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；字符：将字符添加到指定位置
#         o，将整数转换成 八  进制表示，并将其格式化到指定位置
#         x，将整数转换成十六进制表示，并将其格式化到指定位置
#         d，将整数、浮点数转换成 十 进制表示，并将其格式化到指定位置
#         e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
#         E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
#         f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
#         F，同上
#         g，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
#         G，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是E；）
#         %，当字符串中存在格式化标志时，需要用 %%表示一个百分号
#
# 注：Python中百分号格式化是不存在自动将整数转换成二进制表示的方式
#
# 常用格式化：

# tpl = "i am %s" % "alex"
#
# tpl = "i am %s age %d" % ("alex", 18)
#
# tpl = "i am %(name)s age %(age)d" % {"name": "alex", "age": 18}
#
# tpl = "percent %.2f" % 99.97623
#
# tpl = "i am %(pp).2f" % {"pp": 123.425556, }
#
# tpl = "i am %.2f %%" % {"pp": 123.425556, }


# 2、Format方式
#
#     [[fill]align][sign][#][0][width][,][.precision][type]
#
#     fill           【可选】空白处填充的字符
#     align        【可选】对齐方式（需配合width使用）
#         <，内容左对齐
#         >，内容右对齐(默认)
#         ＝，内容右对齐，将符号放置在填充字符的左侧，且只对数字类型有效。 即使：符号+填充物+数字
#         ^，内容居中
#     sign         【可选】有无符号数字
#         +，正号加正，负号加负；
#          -，正号不变，负号加负；
#         空格 ，正号空格，负号加负；
#     #            【可选】对于二进制、八进制、十六进制，如果加上#，会显示 0b/0o/0x，否则不显示
#     ，            【可选】为数字添加分隔符，如：1,000,000
#     width       【可选】格式化位所占宽度
#     .precision 【可选】小数位保留精度
#     type         【可选】格式化类型
#         传入” 字符串类型 “的参数
#             s，格式化字符串类型数据
#             空白，未指定类型，则默认是None，同s
#         传入“ 整数类型 ”的参数
#             b，将10进制整数自动转换成2进制表示然后格式化
#             c，将10进制整数自动转换为其对应的unicode字符
#             d，十进制整数
#             o，将10进制整数自动转换成8进制表示然后格式化；
#             x，将10进制整数自动转换成16进制表示然后格式化（小写x）
#             X，将10进制整数自动转换成16进制表示然后格式化（大写X）
#         传入“ 浮点型或小数类型 ”的参数
#             e， 转换为科学计数法（小写e）表示，然后格式化；
#             E， 转换为科学计数法（大写E）表示，然后格式化;
#             f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
#             F， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
#             g， 自动在e和f中切换
#             G， 自动在E和F中切换
#             %，显示百分比（默认显示小数点后6位）


 # 常用格式化：
#  tpl = "i am {}, age {}, {}".format("seven", 18, 'alex')  #只有一个空的{}，表示不论类型，所有的都可以按照顺序进行替换；
#
# tpl = "i am {}, age {}, {}".format(*["seven", 18, 'alex']) ##如果以列表的方式进行传递，必须要加*，就可以按照顺序逐个进行替换；
#
# tpl = "i am {0}, age {1}, really {0}".format("seven", 18) ##指定索引的情况下，按照索引进行替换
#
# tpl = "i am {0}, age {1}, really {0}".format(*["seven", 18]) ##列表方式
#
# tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18) ##指定名字的方式
#
# tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18}) ##用字典的方式
#
# tpl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33]) ##索引中嵌套索引，复用的方式
#
# tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1) ##指定占位符的类型
#
# tpl = "i am {:s}, age {:d}".format(*["seven", 18])
#
# tpl = "i am {name:s}, age {age:d}".format(name="seven", age=18)
#
# tpl = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})
#
# tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2) ##不同进制的转换
#
# tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
#
# tpl = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
#
# tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)

# 更多格式化操作：https://docs.python.org/3/library/string.html