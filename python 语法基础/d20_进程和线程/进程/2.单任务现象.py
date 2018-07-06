#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
from time import sleep

def run():
    while True:
        print("sunck is a nice girl")
        sleep(1.2)

if __name__ == '__main__':
    while True:
        print("sunck is a good man")
        sleep(1)
    run()  ##这个任务永远也执行不到，只有上面的while循环结束才可以执行这个任务，所以当前就是单任务模式；
