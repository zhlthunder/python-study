#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
#by python2.7
#可以接收多个链接，但只有一个客户端停止后。另一个客户端才可以进来进行通信；
#重要：虽然是while循环，但是是单线程，无法完成并发，即只能排队执行；
import socket,time
HOST="127.0.0.1"
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
    dd="hello world"
    s.sendall(dd)
    data=s.recv(1024)
    time.sleep(2)
    print("received",repr(data))
s.close()
