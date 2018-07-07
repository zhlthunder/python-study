#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8081))

while True:
    data=input("请输入要发送的数据：")
    client.send(data.encode("utf-8"))
    info=client.recv(1024)
    print("服务器说："+info.decode("utf-8"))