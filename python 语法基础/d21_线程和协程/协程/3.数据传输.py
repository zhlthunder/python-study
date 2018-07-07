#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

def run():
    ##空变量，存储的作用，data始终为空
    data=""
    r=yield data   ##首先返回一个空字符，然后执行 m.send("a") ，会把“a”赋值给r;
    print(1,r,data)
    r=yield data
    print(2,r,data)
    r=yield data
    print(3,r,data)
    r=yield data


m=run()
##启动m
print(m.send(None))
print(m.send("a"))
print("---------------")
print(m.send("b"))
print("---------------")
print(m.send("c"))
print("---------------")
