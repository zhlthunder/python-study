#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#三元运算符
# var=1 if 2>1 else 2
# print(var)

##字符编码
"""
各国自己的编码格式：
ASCII
GBK
....

万国码： unicode  :涵盖了全球所有文字和二进制的对应关系
unidecode的两个作用：
1.支持全球所有的语言，每个国家都可以不用自己之前的旧的编码，用unicode就可以了
2.unide 包含了跟全球所有国家编码的映射关系；

unicode解决了字符和二进制的映射关系，但是有点浪费空间。
于是就产生了UTF (unicode transformation format),为了节约存储空间而产生的
utf-8: 使用1,2,3,4 个字节
utf-16 ：使用2,4个字节
utf-32:使用4个字节
总结：utf是为unicode设计的一种在存储和传输时节省空间的编码方案；

字符无论以什么编码在内存中显示字符，存到的硬盘上都是二进制；
要注意的是，存到硬盘上时以何种编码存的，再从硬盘上读出来时，就必要以何种编码读，要不然就乱码了。

编码的转换：
无论你以什么编码存储的数据，只要你的软件在把数据从硬盘读到内存里，转换成unicode来显示，就可以了。
由于所有的系统都默认支持unicode,所以你用gbk写的软件，加载到内存中，转换成Unicode，就可以正常显示了。
之所以可以从gbk转换成unicode,是因为上面说的第二点，unicode中包含了跟全球所有国家编码的映射关系。

unicode和 gbk转换表
http://www.unicode.org/charts/
"""

#py3
# -*- coding: utf-8 -*-
s="我是中文"
print(s)
print(type(s))
s2=s.encode('utf-8')
print(s2)
print(type(s2))


# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 基础\chapter3>python3 s1.py
# 我是中文

#说明：python3中可以正常显示中文的原因是， 将代码读入内存中后，py3解释器会自动把utf-8转换成unicode,所以可以正常显示了

#而如果是python2,将代码加载进入内存后，并不会自动转换成unicode,所以就会显示成乱码：
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 基础\chapter3>python2 s1.py
# 鎴戞槸涓枃

# 既然py2不可以自动转换，我们来手动转换试试看：
# s="我是中文"
# print(s)
# s2=s.decode('utf-8')
# print(s2)
# print(type(s2))
# 输出：
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 基础\chapter3>python2 s1.py
# 鎴戞槸涓枃
# 我是中文
# <type 'unicode'>

# s="我是中文"
# print(s)
# s2=s.decode('utf-8')
# print(s2)
# print(type(s2))
# s3=s2.encode('GBK')
# print(s3)
# print(type(s3))
# 输出：
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 基础\chapter3>python2 s1.py
# 鎴戞槸涓枃
# 我是中文
# <type 'unicode'>
# 鎴戞槸涓枃
# 我是中文
# <type 'unicode'>
# 我是中文
# <type 'str'>
#总结：即如果要显示中文,有两种方法：
# 1.将utf-8 解码成unicode,
# 2.将unicode再转换成gbk也可以正常显示中文

##重要： python2中，其它类型转换成unicode,为解码， 得到的类型是 unicode;
                   # unicode转换成其它类型，为编码，得到的类型是str


##python2  bytes类型
# 在交互模式下：
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study>python2
# Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> s="中文 "
# >>> print s
# 中文
# >>> s
# '\xd6\xd0\xce\xc4 '  ##bytes类型
# >>>

#在python2中，bytes==str, 即这两个类型是一样的。 python2有个专门的unicode类型，

##于是python3就出生了：
# 其中一个改进：将字符串变成了unicode,文件的默认编码格式变成了utf-8
#这意味着：只要用python3，无论你的程序是以哪种编码开发的，都可以在全球各国的电脑上正常显示。
# 同时，在py3中，把str和bytes做了明确的区分，str就是unicode格式的字符，bytes就是单纯的二进制了
#最重要的一点：py3中看到的字符，必须得是unicode编码的，其它的编码一律按bytes格式显示。

##关于字符类型的总结：重要
"""
py3中包括 str,bytes类型 ， str类型表示是unicode; bytes来统称其它的编码格式；
py2中包括 unicode,str类型，unicode类型表示就是unicode编码的；str(==bytes)来统称其它格式；
所以在py2中，unicode类型可以用type来判断，而关于str究竟是utf-8，还是gbk..，需要借助unicode编码映射表来查找或字节个数；

其它格式==》unicode 称为decode;  decode时需要指定编码格式
unicode==>其它格式 称为encode；  encode时需要指定编码格式；

"""