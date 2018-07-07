#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import threading
import time

bar=threading.Barrier(4)

def run():
    print("线程%s-start"%(threading.current_thread().name))
    time.sleep(1)
    bar.wait()  ##这里的意思是，只有凑够4个线程，才会继续执行，所以执行结果中，只有4个线程结束了
    print("线程%s-stop"%(threading.current_thread().name))


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=run).start()

##输出：
# 线程Thread-1-start
# 线程Thread-2-start
# 线程Thread-3-start
# 线程Thread-4-start
# 线程Thread-5-start
# 线程Thread-3-stop
# 线程Thread-4-stop
# 线程Thread-2-stop
# 线程Thread-1-stop