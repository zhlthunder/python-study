#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import socket
import sys

HOST,PORT="localhost",50007
data=" ".join(sys.argv[1:])

#create a socket(SOCK_STREAM means a TCP socket)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    #coonect to server and send data
    sock.connect((HOST,PORT))
    sock.sendall(data+"\n")

    #receive data from the server and shut down
    received=sock.recv(1024)

finally:
    sock.close()

print("sent: {}".format(data))
print("received: {}".format(received))