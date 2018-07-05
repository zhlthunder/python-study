#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from multiprocessing import Process
from time import sleep

NUM=100

def run():
    print("子进程开始")
    global NUM   ##相当于定义了一个新的NUM=100
    NUM+=1
    print(NUM)
    print("子进程结束")

if __name__ == '__main__':
    print("父进程开始")
    p=Process(target=run)
    p.start()
    p.join()
    print("父进程结束--%d"%NUM)
    #在子进程中修改全局变量，对父进程中的全局变量没有影响；
    #因为在创建子进程时，对全局变量做了一个备份，父进程与子进程中的NUM 是完全不同的两个变量；

    ##注意，如果此处开启了多个子进程，他们内部的NUM也是没有关系的。
    # ==》父子进程或兄弟进程之间都无法共享这个变量；
