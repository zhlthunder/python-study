#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import os,time
from multiprocessing  import Process,Pool

def copyFile(rPath,wPath):
    fr=open(rPath,"rb")
    fw=open(wPath,"wb")
    context=fr.read()
    fw.write(context)
    fr.close()
    fw.close()

path=r"C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 基础\进程和线程\file"
topath=r"C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 基础\进程和线程\tofile"

if __name__ == '__main__':
    start=time.time()
    ##读取path下所有的文件：
    fileslist=os.listdir(path)
    pp=Pool()
    for filename in fileslist:
        pp.apply_async(copyFile,args=(os.path.join(path,filename),os.path.join(topath,filename)))
    pp.close()
    pp.join()
    end=time.time()
    print("总耗时---%.2f"%(end-start))


# 输出：
# 总耗时---0.46  ##当拷贝大容量文件时，多线程就会节约时间了，请注意；