#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#打开文件   f=open("db",'r')

#以下的格式，默认由python来完成字符串向bytes的转换；
# f=open('db1','r')  #只读
# f=open('db1','w')  #只写，先清空然后再写
# f=open('db1','x')  #是python3新加入的功能，如果文件存在时就报错，如果文件不存在，就创建文件并写内容；
# f=open('db1','a')  #追加内容

# def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True): # known special case of open
# f=open('db1','r')
# data=f.read()
# print(data,type(data))
# f.close()

# 输出：
# admin|123
# tom|123 <class 'str'>  #python 自动把二进制转换成字符串；

#备注，如果打开文件时出现乱码，那就是字符编码不匹配导致的，推荐都适用utf-8的格式来保存和读取；
# f=open('db1','r',encoding="utf-8")  # 这是标准格式；
# data=f.read()
# print(data,type(data))
# f.close()


#只要打开方式中有b,就表示直接以二进制的方式来读取，且此时如果写的话，也是以字节的形式来写的。
# f=open('db1','rb')
# data=f.read()
# print(data,type(data))
# f.close()
# 输出：
# b'admin|123\r\ntom|123' <class 'bytes'>

#有b的时候只能写字节；
# f=open("db1",'ab')
# f.write("hello")  #执行时报错 TypeError: a bytes-like object is required, not 'str'
# f.close()


# f=open("db1",'ab')
# f.write(bytes("hello",encoding="utf-8"))  #手动将字符串转换成字节
# f.close()

#打开方式中没有b,python自动将字符串转换成字节；
# f=open("db1",'a')
# f.write("hello")
# f.close()

##总结：
#1.读的时候，如果有 b，读到的是字节；如果没有b,读到的是字符串； 对于写是一样的。



#复合读写模式 “+”
# r+  可读可写
# w+  可读可写
# x+  可读可写
# a+  可读可写

# f=open("db1",'r+',encoding="utf-8")
# data=f.read()
# print(data)
# f.write("777")  #在文件的末尾加上了 “7777”
# f.close()
#说明，文件有个文件指针，读取全部后，文件指针移动到文件的最后了，此时写入时，会从最后开始写入；


# f=open("db1",'r+',encoding="utf-8")
# data=f.read(1)  #说明，即使只读取一个字符，然后进行写入时，也会默认将文件指针移动到最后进行写入，这是python的默认设置，切记；
# print(data)
# f.write("777")
# f.close()

# 输出： a
# db1:
# admin|123
# tom|123777777

#主动调整文件指针的位置；
# f=open("db1",'r+',encoding="utf-8")
# data=f.read(1)
# print(data)
# f.seek(1)
# f.write("777")
# f.close()

# 输出：a
# db1：
# a777n|123  # 由于使用了seek(1)将指针移动到第一个字符的后面，此时写入777会覆盖“dmi”,即python默认执行覆盖的操作；
# tom|123777777

#无论使用什么样的打开方式，seek始终以字节的方式来进行定位，如果文件中有中文字符，就可能因为被拆分而出现乱码；
#使用utf-8写入时是乱码，待确认？
# f=open("db1",'r+',encoding="GBK")
# # data=f.read()
# # print(data)
# # f.seek(1)
# f.write("李杰")
# f.close()


#使用f.tell 获取当前指针位置的命令；
# f=open("db1",'r+',encoding="utf-8")
#如果模式无b,则read的时候是按照字符读取，
# data=f.read(1)
# print(data)
#tell是当前指针所在的位置（永远以字节为单位，与打开方式无关；）
# print(f.tell())
#调整当前指针位置到你指定的地方（永远以字节为单位，与打开方式无关；）
# f.seek(f.tell())
#当前指针位置开始向后覆盖写入；
# f.write("8888")
# f.close()
#
# 输出：
# a
# 1

#@@总结：ｒ＋是使用最多的一种模式，可能也是唯一一种使用的模式，原因介绍：
# a+ :支持读写了，但无论是否使用seek指定指针的位置，只要一写，就总是从最后开始追加；
# w+ :支持读写了，也还是要先清空，再写入；

#==》使用r+ 时，就可以使用seek调整指针位置，然后想在哪写就在哪写，但其它的几个选项都无法满足这个目的，所以只有
# r+可以满足指定位置的写入，也是唯一一个被经常使用的模式；

#r+b  以字节进行读写；

#操作文件    f.read   f.write ...
# read()  #无参数读全部； 有参数，就和打开方式有关：
#                                          打开方式有b,按字节；
#                                          打开方式无b,按字符；

#tell()  获取当前指针位置； 和打开方式无关，永远以字节为单位；
#seek(#)  跳转到指定的位置； 和打开方式无关，永远以字节为单位；
#write()  写数据，和打开方式有关：
#                                          打开方式有b,按字节写
#                                          打开方式无b,按字符写；

#close() 关闭；
#fileno  文件描述符；
#flush() 强制刷新；

#flush介绍：
# f=open("db1",'a')
# f.write("123")
# f.flush()  #强制刷新
# 如果执行f.close() 会自动进行刷新；
# 如果此时没有执行f.close(),比如此时的代码为等待用户输入，如果想让数据被写入文件中，需要执行:f.flush()
# input("请输入：")

#readable() 判断是否可读
# f=open("db",'w')
# print(f.readable())
# 输出：
# False

#seekable() 是否可以移动指针

#readline仅读取一行
# f=open("db1",'r')
# f.readline() #读取第一行
# f.readline() #读取第二行
# f.readline() #读取第三行
# 。。。

#writable() 是否可以写

# #truncate 用于截断数据，指针位置后的内容清空
# f=open("db1",'r+',encoding="utf-8")
# f.seek(3)
# f.truncate() #指针位置后的内容清空
# f.close()
# 执行后： db1 中的内容如下：
# adm

#for循环文件对象（文件句柄） f=open(###)
# f=open("db1",'r+',encoding="utf-8")
# for line in f:
#     print(line)  #循环打印文件中的每一行


#关闭文件   f.close   或 with open('db') as f  来自动关闭文件

# with open("db1") as f:
#     pass#代码块
#
# # 从python2.7开始支持，使用with open 同时打开多个文件；
# with open("db1") as f1, open("db2") as f2:
#     pass

#使用举例：
# 比如把一个文件的前10行写到另外一个文件中；

# with open("db1",'r',encoding="utf-8") as f1, open("db2",'w',encoding="utf-8") as f2:
#     times=0
#     for line in f1:
#         f2.write(line)
#         times+=1
#         if times==10:
#             break

#使用实例2：文件中指定内容的替换操作；
# with open("db1",'r',encoding="utf-8") as f1, open("db3",'w',encoding="utf-8") as f2:
#     for line in f1:
#         new_str=line.replace("alex","steven")
#         f2.write(new_str)
#



