#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8081))
server.listen(5)
print("服务器端启动成功，等待客户端连接")


def run(conn,addr):
    print("%s---%s连接成功"%(str(conn),addr))
    while True:
        data=conn.recv(1024)
        print("客户端说："+data.decode("utf-8"))
        senddata="this is server"
        conn.send(senddata.encode("utf-8"))

while True:
    conn,addr=server.accept()
    t=threading.Thread(target=run,args=(conn,addr))
    t.start()
