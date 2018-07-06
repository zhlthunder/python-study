#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import threading,time



def run(num):
    print("启动子线程%s"%(threading.current_thread().name))

    ##实现线程的功能
    time.sleep(2)
    print("打印",num)
    time.sleep(2)
    print("结束子线程%s"%(threading.current_thread().name))



if __name__ == '__main__':
    #任何进程默认就会启动一个线程，称为主线程，主线程可以启动新的子线程；
    #current_thread() 返回当前线程的实例
    #  .name 放回当前线程的名称
    print("主线程启动%s"%(threading.current_thread().name))

    ##创建子线程
    # t=threading.Thread(target=run,name="runthread")  # name="runthread" 用于设定子线程的名字，如果不传，
    t=threading.Thread(target=run,args=(1,))  # name="runthread" 用于设定子线程的名字，如果不传，默认就是Thread-1。。。
    t.start()

    ##对于线程，一定要使用join,即让主线程（或进程）等待子线程结束后才退出，否则子线程运行所需的资源环境就没有了，这样是不允许的。
    t.join()

    print("主线程结束%s"%(threading.current_thread().name))

#     输出：
# 主线程启动MainThread
# 启动子线程Thread-1
# 打印
# 结束子线程Thread-1
# 主线程结束MainThread

