#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#打开文件   f=open("db",'r')

f=open('db1','r')  #只读
f=open('db1','w')  #只写，先清空然后再写
f=open('db1','x')  #是python3新加入的功能，如果文件存在时就报错，如果文件不存在，就创建文件并写内容；
f=open('db1','a')  #追加内容


#操作文件    f.read   f.write ...
#关闭文件   f.close   或 with open('db') as f  来自动关闭文件



