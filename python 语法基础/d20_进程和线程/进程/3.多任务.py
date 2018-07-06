#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:

"""
multiprocessing 是一个跨平台的多进程模块，提供了一个Process类来代表一个进程对象；
"""

from multiprocessing import Process
from time import sleep
import os

##子进程需要执行的代码
def run(arg):
    while True:
        #os.getpid() 获取当前进程id号
        #os.getppid() 获取当前进程的父进程
        print("sunck is a %s girl---%s--%s"%(arg,os.getpid(),os.getppid()))
        sleep(1.2)

if __name__ == '__main__':
    print("主进程--%s"%(os.getpid()))
    #创建子进程
    #target说明进程执行的任务
    p=Process(target=run,args=("nice",),)
    p.start()

    while True:
        print("sunck is a good man")
        sleep(1)
