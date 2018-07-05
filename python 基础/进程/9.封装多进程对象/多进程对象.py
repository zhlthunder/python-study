#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from zhlprocess import zhlProcess
from multiprocessing import Process

if __name__ == '__main__':
    print("启动父进程")
    #创建子进程并执行，这样做的好处是，可以把子进程的模块从主进程中分离出来，代码更清晰了。
    p=zhlProcess("test")
    p.start()
    p.join()

    print("结束父进程")