#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import threading,time

cond=threading.Condition()  ##线程条件变量



# def run1():
#     for i in range(0,10,2):
#         print(threading.current_thread().name,i)
#         time.sleep(1)
#
#
# def run2():
#     for i in range(1,10,2):
#         print(threading.current_thread().name,i)
#         time.sleep(2)


def run1():
    with cond:
        for i in range(0,10,2):
            print(threading.current_thread().name,i)
            time.sleep(1)
            cond.wait() ##打印完0后，我阻塞
            cond.notify() ##通知另一个线程执行

def run2():
    with cond:
        for i in range(1,10,2):
            print(threading.current_thread().name,i)
            time.sleep(2)
            cond.notify()##打印完1后通知另一个线程执行
            cond.wait()  ##我阻塞

if __name__ == '__main__':
    threading.Thread(target=run1).start()
    threading.Thread(target=run2).start()