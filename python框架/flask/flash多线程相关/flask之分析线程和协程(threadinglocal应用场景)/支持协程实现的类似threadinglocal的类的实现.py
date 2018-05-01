#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##协程  gevent 安装：pip3 install gevent ，会安装 greenlet, gevent 两个模块
##pip安装指定版本的命令： pip3 install pyasn1==0.4.2

# import flask.globals
import  flask,threading
# from greenlet import getcurrent as get_ident  ##获取当前协程的ID，此处虽然导入时有波浪线，但可以正常使用，原因待确认
# from _thread import get_ident ##可以获取线程的唯一标识

try:
    from greenlet import getcurrent as get_ident  #先尝试导入协程相关的获取ID的模块， 即优先使用协程，如果没有安装协程的模块，就不支持协程
except ImportError:
    try:
        from thread import get_ident  ##如果上面的报错，表示不支持协程，再导入线程相关的获取ID的模块
    except ImportError:
        from _thread import get_ident


##下面的这个类就可以为每个线程开辟空间保存它的值了
class Local(object):
    def __init__(self):
        self.storage={}
        self.get_ident=get_ident

    def set(self,k,v):
        ident=self.get_ident()  #获取线程的唯一标识
        origin=self.storage.get(ident)
        if not origin: ##如果没有这个进程的信息，则为这个进程新创建一个字典
            origin={k:v}
        else:
            origin[k]=v  ##如果已经有这个进程对应的字典，则直接添加
        self.storage[ident]=origin

    def get(self,k):
        ident=self.get_ident()  #获取线程的唯一标识
        origin=self.storage.get(ident)
        if not origin:
            return None
        return origin.get(k,None)

local_values=Local()

def func(num):
    local_values.set('name',num)
    import time
    time.sleep(1)
    print(local_values.get('name'), threading.current_thread().name)


for i in range(20):
    th = threading.Thread(target=func, args=(i,), name='线程%s' % i)
    th.start()

# 输出： 结果和前面的threadinglocal的输出相同，即目前我们定义的类已经完成了和threadinglocal类似的功能了
# 1 线程1
# 0 线程0
# 2 线程2
# 3 线程3
# 4 线程4
# 7 线程7
# 6 线程6
# 5 线程5
# 9 线程9
# 8 线程8
# 10 线程10
# 13 线程13
# 11 线程11
# 12 线程12
# 15 线程15
# 14 线程14
# 16 线程16
# 17 线程17
# 18 线程18
# 19 线程19

