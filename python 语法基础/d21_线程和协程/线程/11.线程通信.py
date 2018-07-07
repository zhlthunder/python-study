#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import threading,time

def func():
    ##创建一个事件对象
    event=threading.Event()
    def run():
        for i in range(5):
            event.wait()##进程阻塞，等待事件的触发；
            event.clear() ##触发之后，再重置阻塞事件，这样每次都会阻塞，如果不重置，就只阻塞一次
            print("thunder is a good man!!%d"%i)
    t=threading.Thread(target=run).start()
    return event

e=func()

##触发事件,这个事件可以在任何一个地方触发，比如可以在别的子线程中触发，就可以实现线程之间的通信；
for i in range(5):
    e.set()  ##触发事件操作
    time.sleep(2)



