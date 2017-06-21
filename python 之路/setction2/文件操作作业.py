#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 需求：

# 老板现在给你任务，公司有haproxy配置文件，希望通过python程序可以对ha配置文件进行增删改，不再是以往的打开文件进行直接操作了。

def record(args):
    with open("haproxy",'r+') as f:
        for line in f:
            if line.strip()=="backend "+args:
                print(f.readline())


def main():
    print(
    """
     operation method:
    1、获取ha记录
    2、增加ha记录
    3、删除ha记录
    """)
    num=input("please select your operation method:")
    if num=='1':
        read = input('请输入backend：')
        record(read)
# 如果用户输入的 1：
#     read = raw_input('请输入backend：')     如输入：www.oldboy.org
#     讲配置文件 backend www.oldboy.org 节点下的所有记录获取到，并输入到终端
main()