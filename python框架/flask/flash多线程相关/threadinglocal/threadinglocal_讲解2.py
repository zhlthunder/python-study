#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#refer:https://blog.csdn.net/kikaylee/article/details/53232920
"""
当我们使用线程的时候，能使用线程的局部变量，就尽量不要用全局变量，因为使用全局变量涉及同步的问题
使用局部变量的时候，需要传递参数，比如有这样一个例子，程序需要处理客户申请，每来一个客户，就新开一
个线程进行处理，而客户有姓名、年龄、性别等属性（参数），如果都需要传递参数的话很繁琐。Python提供
了threading.local模块，方便我们实现线程局部变量的传递。直接看下面的例子:

"""

import threading

# Threading.local对象
ThreadLocalHelper = threading.local()
lock = threading.RLock()

class MyTheadEx(threading.Thread):
    def __init__(self, threadName, name, age, sex):
        super(MyTheadEx, self).__init__(name=threadName)
        self.__name = name
        self.__age = age
        self.__sex = sex

    def run(self):
        global ThreadLocalHelper
        ThreadLocalHelper.ThreadName = self.name
        ThreadLocalHelper.Name = self.__name
        ThreadLocalHelper.Age = self.__age
        ThreadLocalHelper.Sex = self.__sex
        MyTheadEx.ThreadPoc()

    # 线程处理函数
    @staticmethod
    def ThreadPoc():
        # lock.acquire()  ##经过验证，是否追加lock,得到的结果相关，待继续验证是否一定需要这个local
        try:
            print('Thread={id}'.format(id=ThreadLocalHelper.ThreadName))
            print('Name={name}'.format(name=ThreadLocalHelper.Name))
            print('Age={age}'.format(age=ThreadLocalHelper.Age))
            print('Sex={sex}'.format(sex=ThreadLocalHelper.Sex))
            print('----------')
        finally:
            # lock.release()
            pass

if __name__ == '__main__':
    Tom = {'Name': 'tom', 'Age': 20, 'Sex': 'man'}
    xiaohua = {'Name': 'xiaohua', 'Age': 18, 'Sex': 'woman'}
    Andy = {'Name': 'Andy', 'Age': 40, 'Sex': 'man'}
    T = (Tom, xiaohua, Andy)
    threads = []
    for i in range(len(T)):
        t = MyTheadEx(threadName='id_{0}'.format(i), name=T[i]['Name'], age=T[i]['Age'], sex=T[i]['Sex'])
        threads.append(t)
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()
    print('All Done!!!')

    ####经过验证，是否追加lock,得到的结果相关，待继续验证是否一定需要这个local