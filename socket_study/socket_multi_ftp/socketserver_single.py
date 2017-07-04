#!/usr/bin/python



import socket

HOST="localhost"
PORT=9999
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind((HOST,PORT))
ss.listen(5)

while True:
     conn,addr=ss.accept()
     print "connected by :",addr
     while True:
         data=conn.recv(1024).strip()
         if not data:break
         conn.sendall(data.upper())
