#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

"""
使用队列实现生产者和消费者
"""

import  threading,queue
import time,random

##生产者
def producer(i,q):
    while True:
        num=random.randint(0,1000)
        q.put(num)
        print("生产者%d---生产了%d数据放入了队列"%(i,num))
        time.sleep(3)
    #任务结束
    q.task_done()


##消费者
def consumer(i,q):
    while True:
        item=q.get()
        if item is None:
            break
        print("消费者%d--消费了%d数据"%(i,item))
        time.sleep(4)
    ##任务结束
    q.task_done()

if __name__ == '__main__':
    #消息队列
    q=queue.Queue()

    #启动生产者
    for i in range(4):
        threading.Thread(target=producer,args=(i,q)).start()


    ##启动消费者
    for  i in range(3):
        threading.Thread(target=consumer,args=(i,q)).start()