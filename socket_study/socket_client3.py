#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
#by python2.7
#可以接收多个链接，但只有一个客户端停止后。另一个客户端才可以进来进行通信；
#重要：虽然是while循环，但是是单线程，无法完成并发，即只能排队执行；
#服务器端执行客户端发送过来的命令；
import socket,time
HOST="127.0.0.1"
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
    cmd=raw_input("please input your command:").strip()
    if len(cmd)==0:continue
    s.sendall(cmd)
    ##如何数据大于1024，需要调整数据的大小，最大改成8096
    data=s.recv(1024)
    print data
s.close()
