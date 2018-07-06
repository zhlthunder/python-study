#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from multiprocessing import Process,Queue
import os,time

def write(q):
    print("启动写子进程%s"%os.getpid())
    for item in ['A','B','C','D']:
        q.put(item)
        time.sleep(1)

    print("结束写子进程%s"%os.getpid())


def read(q):
    print("启动读子进程%s"%os.getpid())
    while True:
        val=q.get(True)
        print(val)
    print("结束读子进程%s"%os.getpid())


if __name__ == '__main__':
    #父进程创建队列，并传递给子进程
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate() ##因为读子进程是个死循环，所以需要在写子进程结束后，强制结束这个子进程；
