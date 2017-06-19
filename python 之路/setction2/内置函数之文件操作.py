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




#操作文件    f.read   f.write ...
#关闭文件   f.close   或 with open('db') as f  来自动关闭文件



