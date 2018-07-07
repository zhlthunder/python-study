#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


def product(c):
    c.send(None)
    for i in [1,2,3,4,5]:
        print("生产者生产数据%d"%(i))
        r=c.send(i)
        print("消费者消费了数据:status--%s"%r)
    c.close()

def customer():
    data=""
    while True:
        n=yield data
        if not n:
            return
        print("消费者消费了%s"%n)
        data="200"



c=customer()
product(c)