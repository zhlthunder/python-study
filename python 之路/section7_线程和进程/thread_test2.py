#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# Python GIL(Global Interpreter Lock)　
# 上面的核心意思就是，无论你启多少个线程，你有多少个cpu, Python在执行的时候会淡定的在同一时刻只允许一个线程运行，
# 首先需要明确的一点是GIL并不是Python的特性，它是在实现Python解析器(CPython)时所引入的一个概念。就好比C++是一套语言（语法）标准，但是可以用不同的编译器来编译成可执行代码。有名的编译器例如GCC，INTEL C++，Visual C++等。Python也一样，同样一段代码可以通过CPython，PyPy，Psyco等不同的Python执行环境来执行。像其中的JPython就没有GIL。然而因为CPython是大部分环境下默认的Python执行环境。所以在很多人的概念里CPython就是Python，
# 也就想当然的把GIL归结为Python语言的缺陷。所以这里要先明确一点：GIL并不是Python的特性，Python完全可以不依赖于GIL
#


# Python threading模块

# 线程有2种调用方式，如下：
#
# 直接调用

# import threading
# import time
#
# def sayhi(num):
#     print("running on number:%s"%num)
#     time.sleep(3)
#
# if __name__ == '__main__':
#
#     t1 = threading.Thread(target=sayhi,args=(1,)) #生成一个线程实例
#     t2 = threading.Thread(target=sayhi,args=(2,)) #生成另一个线程实例
#
#     t1.start() #启动线程
#     t2.start() #启动另一个线程
#
#     print(t1.getName()) #获取线程名
#     print(t2.getName())



# 继承式调用
# import threading
# import time
#
#
# class MyThread(threading.Thread):
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num = num
#
#     def run(self):#定义每个线程要运行的函数
#
#         print("running on number:%s" %self.num)
#
#         time.sleep(3)
#
# if __name__ == '__main__':
#
#     t1 = MyThread(1)
#     t2 = MyThread(2)
#     t1.start()
#     t2.start()



# Join & Daemon
#守护进程
# import time
# import threading
# def run(n):
#
#     print('[%s]------running----\n' % n)
#     time.sleep(2)
#     print('--done--')
#
# def main():
#     for i in range(5):
#         t = threading.Thread(target=run,args=[i,])
#         t.start()
#         t.join(1)
#         print('starting thread', t.getName())
#
#
# m = threading.Thread(target=main,args=[])
# m.setDaemon(True) #将main线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,
# # m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
# m.start()
# m.join(timeout=2)  ##子进程执行不完
# # m.join()  ##所有的子线程可以执行完
# print("---main thread done----")

# 使用 m.join()时的输出：
# [0]------running----
#
# ('starting thread', 'Thread-2')
# [1]------running----
#
# --done--
# ('starting thread', 'Thread-3')
# [2]------running----
#
# --done--
# ('starting thread', 'Thread-4')
# [3]------running----
#
# --done--
# ('starting thread', 'Thread-5')
# [4]------running----
#
# --done--
# ('starting thread', 'Thread-6')
# ---main thread done----

# 使用m.join(timeout=2)时的输出，待继续对比确认：
# [0]------running----
#
# ('starting thread', 'Thread-2')
# [1]------running----
#
# ---main thread done----(
# 'starting thread', --done--'Thread-
# 3')
# [2]------running----



# 线程锁(互斥锁Mutex)

# import time
# import threading
#
# def addNum():
#     global num #在每个线程中都获取这个全局变量
#     print('--get num:',num )
#     time.sleep(1)
#     num  -=1 #对此公共变量进行-1操作
#
# num = 100  #设定一个共享变量
# thread_list = []
# for i in range(100):
#     t = threading.Thread(target=addNum)
#     t.start()
#     thread_list.append(t)
#
# for t in thread_list: #等待所有线程执行完毕
#     t.join()
#
#
# print('final num:', num )
# *注：不要在3.x上运行，不知为什么，3.x上的结果总是正确的，可能是自动加了锁


# 加锁版本

# import time
# import threading
#
# def addNum():
#     global num #在每个线程中都获取这个全局变量
#     print('--get num:',num )
#     time.sleep(1)
#     lock.acquire() #修改数据前加锁
#     num  -=1 #对此公共变量进行-1操作
#     lock.release() #修改后释放
#
# num = 100  #设定一个共享变量
# thread_list = []
# lock = threading.Lock() #生成全局锁
# for i in range(100):
#     t = threading.Thread(target=addNum)
#     t.start()
#     thread_list.append(t)
#
# for t in thread_list: #等待所有线程执行完毕
#     t.join()
#
# print('final num:', num )



# RLock（递归锁）
# 说白了就是在一个大锁中还要再包含子锁

# import threading,time
#
# def run1():
#     print("grab the first part data")
#     lock.acquire()
#     global num
#     num +=1
#     lock.release()
#     return num
# def run2():
#     print("grab the second part data")
#     lock.acquire()
#     global  num2
#     num2+=1
#     lock.release()
#     return num2
# def run3():
#     lock.acquire()
#     res = run1()
#     print('--------between run1 and run2-----')
#     res2 = run2()
#     lock.release()
#     print(res,res2)
#
#
# if __name__ == '__main__':
#
#     num,num2 = 0,0
#     lock = threading.RLock()
#     for i in range(10):
#         t = threading.Thread(target=run3)
#         t.start()
#
# while threading.active_count() != 1:
#     print(threading.active_count())
# else:
#     print('----all threads done---')
#     print(num,num2)


# Semaphore(信号量)
#
# 互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 ，
# 比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去。

# import threading,time
#
# def run(n):
#     semaphore.acquire()
#     time.sleep(1)
#     print("run the thread: %s\n" %n)
#     semaphore.release()
#
# if __name__ == '__main__':
#
#     num= 0
#     semaphore  = threading.BoundedSemaphore(5) #最多允许5个线程同时运行
#     for i in range(20):
#         t = threading.Thread(target=run,args=(i,))
#         t.start()
#
# while threading.active_count() != 1:
#     pass #print threading.active_count()
# else:
#     print('----all threads done---')
#     print(num)


# Timer
#
# This class represents an action that should be run only after a certain amount of time has passed
#
# Timers are started, as with threads, by calling their start() method. The timer can be stopped (before its action has begun) by calling thecancel() method. The interval the timer will
# wait before executing its action may not be exactly the same as the interval specified by the user.
# Timer:  隔一定时间调用一个函数,如果想实现每隔一段时间就调用一个函数的话，
# 就要在Timer调用的函数中，再次设置Timer。Timer是Thread的一个派生类

# sample 1:
# import timer,threading
# def hello():
#     print("hello, world")
#
# t = threading.Timer(30.0, hello)
# t.start()  # after 30 seconds, "hello, world" will be printed

#smaple 2:  执行一次
# import threading
# import time
#
# def hello(name):
#     print "hello %s\n" % name
#

# if __name__ == "__main__":
#     timer = threading.Timer(2.0, hello, ["Hawk"])
#     timer.start()


#smaple 3: 递归调用
# import threading
# import time
#
# def hello(name):
#     print "hello %s\n" % name
#
#     global timer
#     timer = threading.Timer(2.0, hello, ["Hawk"])
#     timer.start()
#
# if __name__ == "__main__":
#     timer = threading.Timer(2.0, hello, ["Hawk"])
#     timer.start()


# Events
#
# An event is a simple synchronization object;
#
# the event represents an internal flag, and threads
# can wait for the flag to be set, or set or clear the flag themselves.
#
# event = threading.Event()
#
# # a client thread can wait for the flag to be set
# event.wait()

# a server thread can set or reset it
# event.set()
# event.clear()
# If the flag is set, the wait method doesn’t do anything.
# If the flag is cleared, wait will block until it becomes set again.
# Any number of threads may wait for the same event.
#
# 通过Event来实现两个或多个线程间的交互，下面是一个红绿灯的例子，即起动一个线程做交通指挥灯，
# 生成几个线程做车辆，车辆行驶按红灯停，绿灯行的规则。

# import threading,time
# import random
# def light():
#     if not event.isSet():
#         event.set() #wait就不阻塞 #绿灯状态
#     count = 0
#     while True:
#         if count < 10:
#             print('\033[42;1m--green light on---\033[0m')
#         elif count <13:
#             print('\033[43;1m--yellow light on---\033[0m')
#         elif count <20:
#             if event.isSet():
#                 event.clear()
#             print('\033[41;1m--red light on---\033[0m')
#         else:
#             count = 0
#             event.set() #打开绿灯
#         time.sleep(1)
#         count +=1
# def car(n):
#     while 1:
#         time.sleep(random.randrange(10))
#         if  event.isSet(): #绿灯
#             print("car [%s] is running.." % n)
#         else:
#             print("car [%s] is waiting for the red light.." %n)
# if __name__ == '__main__':
#     event = threading.Event()
#     Light = threading.Thread(target=light)
#     Light.start()
#     for i in range(3):
#         t = threading.Thread(target=car,args=(i,))
#         t.start()


# 这里还有一个event使用的例子，员工进公司门要刷卡， 我们这里设置一个线程是“门”，
# 再设置几个线程为“员工”，员工看到门没打开，就刷卡，刷完卡，门开了，员工就可以通过。

#_*_coding:utf-8_*_
# __author__ = 'Alex Li'
# import threading
# import time
# import random
#
# def door():
#     door_open_time_counter = 0
#     while True:
#         if door_swiping_event.is_set():
#             print("\033[32;1mdoor opening....\033[0m")
#             door_open_time_counter +=1
#
#         else:
#             print("\033[31;1mdoor closed...., swipe to open.\033[0m")
#             door_open_time_counter = 0 #清空计时器
#             door_swiping_event.wait()
#
#
#         if door_open_time_counter > 3:#门开了已经3s了,该关了
#             door_swiping_event.clear()
#
#         time.sleep(0.5)
#
#
# def staff(n):
#
#     print("staff [%s] is comming..." % n )
#     while True:
#         if door_swiping_event.is_set():
#             print("\033[34;1mdoor is opened, passing.....\033[0m")
#             break
#         else:
#             print("staff [%s] sees door got closed, swipping the card....." % n)
#             print(door_swiping_event.set())
#             door_swiping_event.set()
#             print("after set ",door_swiping_event.set())
#         time.sleep(0.5)
# door_swiping_event  = threading.Event() #设置事件
#
#
# door_thread = threading.Thread(target=door)
# door_thread.start()
#
#
#
# for i in range(5):
#     p = threading.Thread(target=staff,args=(i,))
#     time.sleep(random.randrange(3))
#     p.start()



# queue队列

# queue is especially useful in threaded programming when information must be exchanged safely between multiple threads.
#
# class queue.Queue(maxsize=0) #先入先出
#
# class queue.LifoQueue(maxsize=0) #last in fisrt out
# class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列
#
#     Constructor for a priority queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.
#
#     The lowest valued entries are retrieved first (the lowest valued entry is the one returned by sorted(list(entries))[0]). A typical pattern for entries is a tuple in the form: (priority_number, data).
#
# exception queue.Empty
#
#     Exception raised when non-blocking get() (or get_nowait()) is called on a Queue object which is empty.
#
# exception queue.Full
#
#     Exception raised when non-blocking put() (or put_nowait()) is called on a Queue object which is full.
#
# Queue.qsize()
#
# Queue.empty() #return True if empty
#
# Queue.full() # return True if full
#
# Queue.put(item, block=True, timeout=None)
#
#     Put item into the queue. If optional args block is true and timeout is None (the default), block if necessary until a free slot is available. If timeout is a positive number, it blocks at most timeout seconds and raises the Full exception if no free slot was available within that time. Otherwise (block is false), put an item on the queue if a free slot is immediately available, else raise the Full exception (timeout is ignored in that case).
#
# Queue.put_nowait(item)
#
#     Equivalent to put(item, False).
#
# Queue.get(block=True, timeout=None)
#
#     Remove and return an item from the queue. If optional args block is true and
# timeout is None (the default), block if necessary until an item is available. If timeout is
# a positive number, it blocks at most timeout seconds and raises the Empty exception if no
# item was available within that time. Otherwise (block is false), return an item if one is
# immediately available, else raise the Empty exception (timeout is ignored in that case).
#
# Queue.get_nowait()
#
#     Equivalent to get(False).
#
# Two methods are offered to support tracking whether enqueued tasks have been
#  fully processed by daemon consumer threads.
#
# Queue.task_done()
#
#     Indicate that a formerly enqueued task is complete. Used by queue consumer
# threads. For each get() used to fetch a task, a subsequent call to task_done() tells
# he queue that the processing on the task is complete.
#
#     If a join() is currently blocking, it will resume when all items have been
# processed (meaning that a task_done() call was received for every item that had been put() into the queue).
#
#     Raises a ValueError if called more times than there were items placed in the queue.
#
# Queue.join() block直到queue被消费完毕

# 生产者消费者模型

# 在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡
# 生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。
#
# 为什么要使用生产者和消费者模式
#
# 在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，
# 如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，
# 如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。
#
# 什么是生产者消费者模式
#
# 生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来
# 进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，
# 阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。

# 下面来学习一个最基本的生产者消费者模型的例子
# 这个是python自带的库，不需要安装。
# 直接在代码中敲入 import Queue 就可以了。注意第一个字母大写（在python 2的版本中）。
# Python2.x 是import Queue   注意Q是大写。  而到了Python3.x  变成了queue。
# 因为有中文，下面的这个例子用python3

# import threading
# import queue
#
# def producer():
#     for i in range(10):
#         q.put("骨头 %s" % i )
#
#     print("开始等待所有的骨头被取走...")
#     q.join()
#     print("所有的骨头被取完了...")
#
#
# def consumer(n):
#
#     while q.qsize() >0:
#
#         print("%s 取到" %n ,q.get())
#         q.task_done() #告知这个任务执行完了
#
# q = queue.Queue()
#
#
#
# p = threading.Thread(target=producer,)
# p.start()
#
# c1 = consumer("李闯")

# 下面的这个例子用python3
# import time,random
# import queue,threading
# q = queue.Queue()
# def Producer(name):
#   count = 0
#   while count <20:
#     time.sleep(random.randrange(3))
#     q.put(count)
#     print('Producer %s has produced %s baozi..' %(name, count))
#     count +=1
# def Consumer(name):
#   count = 0
#   while count <20:
#     time.sleep(random.randrange(4))
#     if not q.empty():
#         data = q.get()
#         print(data)
#         print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
#     else:
#         print("-----no baozi anymore----")
#     count +=1
# p1 = threading.Thread(target=Producer, args=('A',))
# c1 = threading.Thread(target=Consumer, args=('B',))
# p1.start()
# c1.start()

# 多进程multiprocessing
#
# multiprocessing is a package that supports spawning processes using an API similar to the threading module.
# The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global
# Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the
# programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows.
#
# from multiprocessing import Process
# import time
# def f(name):
#     time.sleep(2)
#     print('hello', name)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()

# To show the individual process IDs involved, here is an expanded example:

# from multiprocessing import Process
# import os
#
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#     print("\n\n")
#
# def f(name):
#     info('\033[31;1mfunction f\033[0m')
#     print('hello', name)
#
# if __name__ == '__main__':
#     info('\033[32;1mmain process line\033[0m')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()


# 进程间通讯　
# 不同进程间内存是不共享的，要想实现两个进程间的数据交换，可以用以下方法：
#
# Queues
#
# 使用方法跟threading里的queue差不多

from multiprocessing import Process, Queue

# def f(q):
#     q.put([42, None, 'hello'])
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())    # prints "[42, None, 'hello']"
#     p.join()

# Pipes

# The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex
# (two-way). For example:

# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())   # prints "[42, None, 'hello']"
#     p.join()