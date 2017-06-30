#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# callable() #表示是否可以被调用
#@@@@@@@@@@@@@@@@@@@@@@
# def f1():
#     pass
# print(callable(f1))
#
# f2=123
# print(callable(f2))
# 输出：
# True
# False
#@@@@@@@@@@@@@@@@@@@@@@@


# chr() 从ASCII码转换为字符，即数字转换为字母；
# ord()  从字符转换为ASCII码，即字母转换为数字；
# r=chr(65)
# print(r)
# 输出：A
# n=ord("a")
# print(n)
# 输出：97

# @@随机验证码生成器
# import random
# i=random.randrange(1,5)  #生成1-5的随机数字； （大于等于1，小于5）
# print(i)

#在ASCII码表中， 65~90 对应的是A~Z;
# import random
# i=random.randrange(65,91)
# c=chr(i)
# print(c)

# 实例1：@@生成6个字母的随机验证码
# li=[]
# import random
# for i in range(6):
#     i=random.randrange(65,91)
#     c=chr(i)
#     li.append(c)
# str="".join(li)
# print(str)

#实例2：在第二和第四位会出现数字；
# li=[]
# import random
# for i in range(6):
#     if i==2 or i==4:
#         temp=random.randrange(0,10)
#         c=str(temp) #将数字转换成字符串，否则无法执行join方法；
#         li.append(c)
#     else:
#         temp=random.randrange(65,91)
#         c=chr(temp)
#         li.append(c)
#
# str="".join(li) #补充，执行join命令时，元素必须都是字符串才可以，如果有数据，就会报错；
# print(str)

#实例3：任意位都可能是数字或字母，即这种方式的随机性就很高了；
#这是常用的生存随机验证码的完整的代码；
# li=[]
# import random
# for i in range(6):
#     k=random.randrange(0,5)
#     if k==2 or k==4:
#         temp=random.randrange(0,10)
#         c=str(temp) #将数字转换成字符串，否则无法执行join方法；
#         li.append(c)
#     else:
#         temp=random.randrange(65,91)
#         c=chr(temp)
#         li.append(c)
#
# str="".join(li) #补充，执行join命令时，元素必须都是字符串才可以，如果有数据，就会报错；
# print(str)

#@
# compile()  #用来编译代码的，将字符串编译成字节码；
# eval()
# exec()  #执行字节码；

# 当我们执行python s1.py时的过程如下：
# 1.读取文件内容到内存中；类似open函数一样，拿到的是字符串；
# 2.python内部把字符串编译成 特殊的代码（字节码）
# 3.执行字节码

#@@@
# s="print(123)" #这只是一个字符串，不是代码，如果要变成代码，需要编译；
# r=compile(s,"<string>","exec")  #将字符串编译成字节码，编译模式分为 single , eval,exec
# exec(r)  #执行字节码
# 输出：
# 123

#@@compile:还支持你给它传一个文件名，即由它自己来打开文件，并把文件内容加载到内存，然后编译；
#编译模式介绍：single:把代码编译成单行的python程序； eval:会把代码编译成表达式；exec:会按照python默认的方式进行编译；

# # eval("") 接受一个字符串，把字符串当做表达式来执行；
# s="8*8"
# ret=eval(s) #接受一个字符串的表达式，然后运算并获得结果；
# print(ret)
# 输出:
# 64

#总结：
# compile() 将字符串编译成python代码；
# exec()  执行python 字节码；但没有返回值；
# eval()  执行表达式字符串的运算，可以获得结果；

# s="8*8"
# ret=exec(s) #即无法获得结果；
# print(ret)
# 输出：
# None
#总结：exec() 和eval()都是用来执行pyhton代码的，
# 但exec() 的功能比 eval（）要强大得多；
# 即exec()的功能描述如下：
# 1.它可以接收python的字节码（比如使用compile()获得的代码），那就直接执行python字节码；
# 2.如果它接收的是字符串，它就会先把字符串转换成python字节码，然后再执行；

#exec()用法1：接收python字节码，然后执行；
# s="print(123)"
# r=compile(s,"<string>","exec")
# exec(r)
# 输出：123

#exec()用法2：接收字符串，然后执行；
# s="print(123)"
# exec(s)
# 输出：123
#exec()唯一的不足是没有返回值；

#@最终总结：
# compile() 用于把字符串编译成python字节码；
# exec() 用于执行python代码 （接收两种方式的Python代码：1.编译生成的字节码；2.字符串），但没有返回值；
# eval() 用于执行python代码（只接收表达式样式的字符串，且可以获得返回值）

#备注：exec 和compile 在python的web 框架的模板引擎中会用到；


#@@@
# dir()  用于快速查看某个对象提供的功能
# print(dir(dict))
# 输出：
# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
#  '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

#查看某个对象的详细功能的帮助信息；但IDE编程时一般都不需要使用；
# help(list)


#@@
# divmod()
# r=divmod(97,10)
# print(r)
# 输出：
# (9, 7)

#@@
# enumerate() 枚举类型
# 如果对一个列表，既要遍历索引又要遍历元素时，首先可以这样写：
# list1 = ["这", "是", "一个", "测试"]
# for i in range (len(list1)):
#     print(i ,list1[i])
# 输出：
# 0 这
# 1 是
# 2 一个
# 3 测试

# 上述方法有些累赘，利用enumerate()会更加直接和优美：
# list1 = ["这", "是", "一个", "测试"]
# for index, item in enumerate(list1):
#     print(index, item)
# 输出：
# 0 这
# 1 是
# 2 一个
# 3 测试

# enumerate还可以接收第二个参数，用于指定索引起始值，如：
# list1 = ["这", "是", "一个", "测试"]
# for index, item in enumerate(list1, 1):
#     print(index, item)
# 输出：
# 1 这
# 2 是
# 3 一个
# 4 测试

# 补充
#
# 如果要统计文件的行数，可以这样写：
# count = len(open("db1", 'r').readlines())
# print(count)
# 输出：
# 12

# 这种方法简单，但是可能比较慢，当文件比较大时甚至不能工作。
#
# 可以利用enumerate()：
# count = 0
# for index, line in enumerate(open("db1",'r')):
#     count += 1
# print(count)
# # 输出:
# 12

##@@
# isinstance() 判断对象是否是某个类的实例
# s="alex" #对象是类的实例
# print(isinstance(s,str))
# 输出：
# True



#@@
# filter()
# map()

#需求，列表筛选，自定义函数的实现：
# def f1(args):
#     result=[]
#     for item in args:
#         if item>22:
#             result.append(item)
#     return result
# li=[11,22,33,44,55]
# ret=f1(li)
# print(ret)
# 输出：
# [33, 44, 55]


##使用filter 实现上面的需求
# li=[11,22,33,44,55]
# ret=filter(None,li)
# print(list(ret))
# 输出：
# [11, 22, 33, 44, 55]

#@@
# def f2(a):
#     if a>22:
#         return True
# li=[11,22,33,44,55]
# #在filter内部，会循环第二个参数（for item in li）,对每个循环到的元素执行第一个参数（f2）,如果执行结果为真时，
# #会对应的元素筛选出来组成一个list并返回；
# ret=filter(f2,li)
# print(list(ret))
# 输出：
# [33, 44, 55]

##filter功能的类似解释：
# result=[]
# for item in 第二个参数：
#     r=第一个参数（item）
#     if r:
#         result.append(item)
# return result
#再解释：filter会循环第二个参数，让每个元素执行函数，如果函数返回值为true，表示元素合法，并生成一个子list并返回；

#@
# f1=lambda a:a>30   #lambda表达式内部会自动将执行结果返回，即不是返回None
# ret=f1(90)
# print(ret)
# 输出：
# True

# li=[11,22,33,44,55]
# ret=filter(lambda x:x>33,li) #此处是lambda函数和 filter的结合，让编程更简单；
# #本身，lambda表达式就是用来实现简单功能的，此处把lambda函数体作为filter的第一个参数，让编程变得更简单；
# print(list(ret))
# 输出：
# [44, 55]

#总结： filter 用于做筛选的；

#@@需求，把列表的每个元素都加100
# li=[11,22,33,44,55]
# def f1(args):
#     result=[]
#     for item in args:
#         result.append(item+100)
#     return result
#
# ret=f1(li)
# print(ret)
# 输出：
# [111, 122, 133, 144, 155]

#此时引出map函数，来完成上门的功能；
# li=[11,22,33,44,55]
# def f1(args):
#     return args+100
#
# ret=map(f1,li)
# print(list(ret))
# 输出：
# [111, 122, 133, 144, 155]

#实现此功能的函数进一步简化：
# li=[11,22,33,44,55]
# ret=map(lambda x:x+100,li)
# print(list(ret))
# 输出：
# [111, 122, 133, 144, 155]

#总结：map 函数，是循环第二个参数，对每个元素放到第一个参数中去执行，并将每个元素执行后得到的返回值组成一个list并返回；


# filter 和 map的本质区别：
#filter: 当函数的返回值为true时，将元素添加到结果中；
#map: 将函数的返回值添加到结果中


#@@@
# frozenset #不可变的集合

#@
# globals() #代表所有的全局变量
# # locals()  #代表所有的局部变量
#
# NAME="alex"
# def show():
#     a=123
#     c=234
#     print(globals())
#     print(locals())
# show()
#
# 输出：
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00FEB370>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/python 之路/setction2/内置函数2.py', '__cached__': None, 'NAME': 'alex', 'show': <function show at 0x00FAD540>}
# {'c': 234, 'a': 123}


#@
# hash()  #将字符串转换成哈希值
# s="hhh"
# print(hash(s))
# 输出：
# 1804062631

#hash() 实际上是python内部使用的一种功能，几乎所有的语言也都是这么干的，不会直接存储字符串（比如字典的key），而是先将
# 字符串转换为一个哈希值然后再存储，几乎所有的语言都是这么做的，这样做的好处是：
#1.方便存储，即不论你给我的字符有多长，转换后的长度都是一样的； 2.转换后存储时，查找会很快；即通过转换后值做了一个索引；
#hash一般用于字典的key的保存；


# s="李杰"
# print(len(s))  #在python2.7里输出为6，即默认是按照字节计数的，在python3里输出为2，即默认是按字符来计数的；


# s="李杰"
# b=bytes(s,encoding="utf-8")
# print(len(b))
# 输出：6

#总结：
# python2.7 只能按照字节来计数；
# python3 中既可以按照字节来计数，也可以按照字符来计数；

# #python3:
# for item in "李杰":
#     print(item)
#
# 输出：
# 李
# 杰

# #python2.7
# for item in "李杰":
#     print item
#  #输出6个乱码，即以字节为单位输出的
# 输出：
# �
# �
# �
# �
# �
# �

#
# max()
# min()
# sum()

# ret1=max([11,22,33,1])
# ret2=min([11,22,33,1])
# ret3=sum([11,22,33,1])
# print(ret1)
# print(ret2)
# print(ret3)
# 输出：
# 33
# 1
# 67

# memoryview 是一个类#和内存地址相关的一个类，用不到

# object  也是一个类，是python中所有类的父类

# pow() 求次方的
# print(2**10)
# ret=pow(2,10)
# print(ret)
# 输出：
# 1024
# 1024

# property()  特性，面向对象时用到

# range()
# for i in range(3):
#     print(i)
# 输出：
# 0
# 1
# 2

#repr
# class Foo:
#     def __repr__(self):
#         return "123"
# ret=repr(Foo()) #repr会自动执行它后面的对象所属类的 __repr__方法， 如果这个类定义了__repr__方法就直接执行，如果么有定义就会报错；
# print(ret)
# # 输出：
# # 123

# ret=repr("alex")  # 自动执行字符串类的__repr__方法，如果跟上的对象所属的类没有这个方法，就会报错；
# print(ret)
# 输出：
# 'alex'
#
# str 中的定义：
#   def __repr__(self, *args, **kwargs): # real signature unknown
#         """ Return repr(self). """
#         pass


#reverse
# li=[11,22,33,44]
# print(li.reverse())
# print(li)
# 输出:
# None
# [44, 33, 22, 11]

# li=[11,22,33,44]
# print(list(reversed(li)))
# 输出：
# [44, 33, 22, 11]

# print(round(1.8))
# print(round(1.4))
# 输出：
# 2
# 1

# slice #用于切片，和下面的功能相似
# s="sssssssss"
# print(s[0:2:2])
# 输出：
# s


# li=[11,2,12,3]
# print(li.sort())
# print(li)
# 输出：
# None
# [2, 3, 11, 12]

#sorted()
# li=[11,2,12,3]
# print(sorted(li))
# print(li)
# 输出：
# [2, 3, 11, 12]
# [11, 2, 12, 3]

##zip()

# l1=["alex",11,22]
# l2=["is",11,22]
# l3=["super",11,22]
# l4=["guy",11,22]
#
# ret=zip(l1,l2,l3,l4)
# print(list(ret))

# 输出：
# [('alex', 'is', 'super', 'guy'), (11, 11, 11, 11), (22, 22, 22, 22)]

# l1=["hhh",1,2]
# l2=["hhh",1]
# ret=zip(l1,l2)
# print(list(ret))
# 输出：
# [('hhh', 'hhh'), (1, 1)]


