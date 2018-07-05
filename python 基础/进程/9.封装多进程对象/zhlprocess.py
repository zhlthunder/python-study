#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


from multiprocessing import Process
import os,time

class zhlProcess(Process):
    def __init__(self,name):
        Process.__init__(self) ##继承父类的__init__,也可以用super....
        # super(zhlProcess,self).__init__()
        self.name=name

    def run(self):##重构父类的run方法
        print("子进程启动--%s--%s"%(self.name,os.getpid()))
        ##在此实现子进程的功能
        time.sleep(2)
        print("子进程结束--%s--%s"%(self.name,os.getpid()))



