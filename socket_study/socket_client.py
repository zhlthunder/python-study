#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
import socket
HOST="127.0.0.1"
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

dd="hello world"
s.sendall(dd)
data=s.recv(1024)
s.close()
print("received",repr(data))