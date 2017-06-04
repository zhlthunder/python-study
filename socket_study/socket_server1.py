#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
#by python2.7
##只支持客户端和服务器端的单次连接
import socket
HOST='127.0.0.1'
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()
print("connected by",addr)
while 1:
    data=conn.recv(1024)
    if not data:break
    conn.sendall(data)
conn.close()