#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:

"""
multiprocessing 是一个跨平台的多进程模块，提供了一个Process类来代表一个进程对象；
"""

from multiprocessing import Process
from time import sleep
import os


# def run():
#     print("启动子进程")
#     sleep(3)
#     print("子进程结束")
#
# if __name__ == '__main__':
#     print("父进程启动")
#     p=Process(target=run)
#     p.start()
#      #父进程的结束不能影响子进程，
#     print("父进程结束")

# 输出：
# 父进程启动
# 父进程结束
# 启动子进程
# 子进程结束




from multiprocessing import Process
from time import sleep
import os


def run():
    print("启动子进程")
    sleep(3)
    print("子进程结束")

if __name__ == '__main__':
    print("父进程启动")
    p=Process(target=run)
    p.start()
    # 让父进程等待子进程结束再执行父进程
    p.join()
    print("父进程结束")

# 输出：
# 父进程启动
# 启动子进程
# 子进程结束
# 父进程结束