#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import os,time
from multiprocessing  import Process

def copyFile(rPath,wPath):
    fr=open(rPath,"rb")
    fw=open(wPath,"wb")
    context=fr.read()
    fw.write(context)
    fr.close()
    fw.close()

path=r"C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 基础\进程和线程\file"
topath=r"C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 基础\进程和线程\tofile"

##读取path下所有的文件：
fileslist=os.listdir(path)
##启动for循环处理每一个文件
start=time.time()
for filename in fileslist:
    copyFile(os.path.join(path,filename),os.path.join(topath,filename))
end=time.time()
print("总耗时:%.2f"%(end-start))

##输出：
# 总耗时:0.01