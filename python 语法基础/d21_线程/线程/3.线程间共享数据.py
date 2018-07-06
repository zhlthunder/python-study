#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

"""
多线程和多进程最大的不同在于，
多进程中同一变量，各自有一份拷贝存储在每个进程的数据空间中，互不影响；
多线程中，所有变量都由所有线程共享；所以任何
"""

import threading

num=0

def run(n):
    global num
    for i in range(1000000):
        num+=n
        num-=n


if __name__ == '__main__':
    t1=threading.Thread(target=run,args=(6,))
    t2=threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("num=",num)


    #因为数据是共享的，所以输出的结果是不确定的。此时就要借助 threadinglocal了。
