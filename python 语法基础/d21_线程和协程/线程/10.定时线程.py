#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import threading


def run():
    print("sunck is a good man")


##根据设置的延时时间，延后执行线程；
t=threading.Timer(5,run)
t.start()
t.join()
print("父线程结束")