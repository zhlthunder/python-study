#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


##解决数据一致性问题的第二种方法， 线程本地化；


import threading

NUM=0  ##为全局变量

locall=threading.local()
 ##创建一个threading.local对象；可以让每个线程有独立的数据空间，避免数据混乱的问题；
 #每个线程对threading.local对象都可以读写，但是互补影响；

def func(n):
    #每个线程都有一个local.x ,是基于线程ID区分开的，可以看成是线程的局部变量，是每个线程独有的。
    locall.x=NUM  ##将全局变量赋值给局部变量；
    for i in range(1000000):
        locall.x+=n
        locall.x-=n
    print("线程%s--%d"%(threading.current_thread().name,locall.x))

if __name__ == '__main__':
    t1=threading.Thread(target=func,args=(6,))
    t2=threading.Thread(target=func,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()




##threadinglocal的作用：
#为每个线程绑定一个数据库连接 或 HTTP请求 或用户身份信息等；
#这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源；
