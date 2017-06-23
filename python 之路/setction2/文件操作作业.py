#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 需求：
# 老板现在给你任务，公司有haproxy配置文件，希望通过python程序可以对ha配置文件进行增删改，不再是以往的打开文件进行直接操作了。

#思路：
#1.建议一行一行地读，防止因为文件过大导致的卡顿；

# 实现思路及实例：
# http://www.cnblogs.com/wupeiqi/articles/5539371.html

#查询记录
def fetch(backend):
    result=[]
    with open("ha.conf","r",encoding="utf-8") as f:
        flag=False
        for line in f:
            if line.strip().startswith("backend") and line.strip()=="backend "+backend:
                flag=True
                continue
            if flag and line.strip().startswith("backend"):
                flag=False
                break
            if flag and line.strip():
                result.append(line.strip())

    return result

# ret=fetch("www.oldboy.org")
# print(ret)


#添加记录
#有三种类型：1--没有backend 和记录； 2--没有记录； 3--记录和backend都有
#实现思路1：先检查记录是否存在；
def add(backend,record):
    record_list=fetch(backend)
    if not record_list:#backend 不存在
        #思路是把目前的配置文件完全复制到另外一个新的文件中，然后在最后添加上backend和 record
        with open("ha.conf","r") as old, open("new.conf","w") as new:
            for line in old:
                new.write(line)
            new.write("\nbackend "+backend+"\n")
            new.write(" "*8+record+"\n")
    else: #backend存在
        #记录存在和记录不存在两种情况；
        if record in record_list:
            #record已经存在
            import shutil
            shutil.copy("ha.conf","new.conf") #直接把文件拷贝一份就可以了

        else:
            #backend存在，record不存在；
            record_list.append(record) #
            with open("ha.conf","r") as old,open("new.conf","w") as new:
                flag=False
                for line in old:
                    #定位到输入的backend处
                    if line.strip().startswith("backend") and line.strip()=="backend "+backend:
                        flag=True #设置标准位
                        new.write(line) #把当前bakcend 行写入新文件
                        for new_line in record_list: #将增加玩记录的所有记录都写入新文件中
                            new.write(" "*8+new_line+"\n")
                    if flag and line.strip().startswith("backend"): #如何循环到下一个backend时执行
                        flag=False #取消标志位
                        new.write(line) #写入当前backend行
                        continue #进入下一行的循环
                    if not flag and line.strip():
                        new.write(line)
                    #备注，两个backend之间的所有行不满足上面三个if的条件，所以都不执行；


# bk="test.oldboy.org"
# rd="server 100.1.7.29 100.1.7.9 weight 20 maxconn 3000"
# add(bk,rd)
bk="www.oldboy.org"
rd="server 100.1.7.139 100.1.7.9 weight 20 maxconn 3000"
add(bk,rd)







#补充json的知识
#使用loads，可以把字符串转换成python的基本数据类型；
# s="[11,22,33,44]"
# print(type(s))
# import json
# a=json.loads(s)
# print(type(a))
# print(a)
#
# 输出：
# <class 'str'>
# <class 'list'>
# [11, 22, 33, 44]

# remark:
# http://www.cnblogs.com/wupeiqi/articles/4950799.html
#作业介绍：
# import json
# inp_str = "[11,22,33,44]"
# inp_list = json.loads(inp_str) # 根据字符串书写格式，将字符串自动转换成 列表类型
# print(inp_list)
#
#
# inp_str = ' {"k1":123, "k2": "wupeiqi"} '  # 正确的输入     切记，字符串内部的列表或字典内的字符串必须用双引号 ！！！
# #inp_str = " {'k1':123, 'k2': 'wupeiqi'}"   # 错误的输入
# inp_dict = json.loads(inp_str) # 根据字符串书写格式，将字符串自动转换成 字典类型
# print(inp_dict)
#
# 输出：
# [11, 22, 33, 44]
# {'k1': 123, 'k2': 'wupeiqi'}

# r=input("请输入:")
# print(type(r),r)
# import json
# dic=json.loads(r)

