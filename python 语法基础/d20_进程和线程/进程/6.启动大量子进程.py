#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from multiprocessing import Process,Pool
import os,time,random

def run(name):
    print("子进程%s开始--%s"%(name,os.getpid()))
    start=time.time()
    time.sleep(random.choice([1,2,3]))
    end=time.time()

    print("子进程%s结束--%s--耗时%.2f"%(name,os.getpid(),end-start))

if __name__ == '__main__':
    print("父进程启动")
    #创建多个进程
    #进程池 Pool
    #Pool(N)  N表示可以同时执行的进程数量，如果不写，默认大小 是CPU核心数
    pp=Pool()
    for i in range(5): ##此处的数字要大于进程数目
        #创建进程，放入进程池中统一管理
        pp.apply_async(run,args=(i,))
    #在调用join之前必须先调用close,调用close之后就不能再继续添加新的进程,但在close之前，还可以继续在循环之外添加进程到进程池中

    pp.close()
    #进程池对象调用的jOin,会等待进程池中所有的子进程结束完毕再去执行父进程；
    pp.join()

    print("父进程结束")

    ##输出：
# 父进程启动
# 子进程0开始--33196
# 子进程1开始--8576
# 子进程2开始--123284
# 子进程3开始--98072
# 子进程1结束--8576--耗时2.00
# 子进程4开始--8576 //此处注意，只有一个进程结束后，进程4才可以启动
# 子进程3结束--98072--耗时2.00
# 子进程0结束--33196--耗时3.00
# 子进程2结束--123284--耗时3.00
# 子进程4结束--8576--耗时3.00
# 父进程结束


##这个例子中，多个子进程完成的功能是一样的，只是为了测试需要
##实际的使用中，多个子进程执行的功能是不同的，就不要用循环，使用pp.apply_async() 依次增加就可以了
