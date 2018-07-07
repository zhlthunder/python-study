#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


import threading
import time

sem=threading.Semaphore(2) ##并发线程数

def run():
    #不使用信号量时：
    # for i in range(10):
    #     print("线程%s--%d"%(threading.current_thread().name,i))
    #     time.sleep(1)

    #使用信号量时,此时只允许2个线程同时工作；
    with sem:
        for i in range(10):
            print("线程%s--%d"%(threading.current_thread().name,i))
            time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=run).start()