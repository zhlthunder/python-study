#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

"""
两个线程同时工作，一个存钱，一个取钱
可能会导致数据异常

解决的思路：是加锁
"""


import threading

num=0
lock=threading.Lock()

def run(n):
    global num
    for i in range(1000000):

        ##加锁的方法1
        lock.acquire()
        ##如果临界区的代码执行异常时，会导致无法解锁，会进入死锁状态，所以我们一般需要使用异常处理的方式，来确保一定会执行解锁的操作
        #确保了这段代码只能由一个线程从头到尾的完整执行
        #阻止了多线程的并发执行，包含锁的某段代码实际上只能以单线程的模式执行，所以执行效率降低
        try:
            num+=n
            num-=n
        finally:
            lock.release()

        ##加锁的方法2，与上面代码功能相同； with lock 可以自动上锁与解锁；
        # with lock:
        #     num+=n
        #     num-=n


if __name__ == '__main__':
    t1=threading.Thread(target=run,args=(6,))
    t2=threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("num=",num)


##线程需要有锁，否则会导致数据混乱；
#由于可以存在多个锁，不同线程持有不同的锁，并试图获取其它的锁，这样可能会造成死锁，导致多个线程 挂起；这样的话，只能靠操作系统强制终止；
