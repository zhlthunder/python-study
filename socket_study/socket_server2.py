#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
#by python2.7
#可以接收多个链接，但只有一个客户端停止后。另一个客户端才可以进来进行通信；
#重要：虽然是while循环，但是是单线程，无法完成并发，即只能排队执行；
import socket
HOST='127.0.0.1'
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while 1:
    conn,addr=s.accept()

    while 1:
        print("connected by",addr)
        data=conn.recv(1024)
        if not data:break
        conn.sendall(data)
    conn.close()