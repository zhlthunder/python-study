#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##说明：
# 和 socket_client4_multi.py可以进行正常的通信，但socket_client4_multi.py 只进行一次通信；
# 即socket_client4_multi.py 的功能太简单了，比socket_client3.py还简单；
#即这个server 如果和 socket_client3.py， 第一次可以成功，但第二次就报错，因为下面的MyTCPHandler 只进行了单次的请求处理，没有应对多次的请求

import SocketServer  ##只在python2.7中才用这个模块，切到pyhton3就会报错，待确认
#定义一个类来处理客户端的请求
class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    the requesthandler class for our server.
    it is instantiated once per connection to the server, and mustoverride the handle() method to implement communication
    to the client
    """
    def handle(self):  ##处理客户请求的函数，类似之前的while循环中的部分
        #self.request is the TCP socket connected to the client
        self.data=self.request.recv(1024).strip()
        print("{} wroted:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

if __name__=="__main__":
    HOST,PORT="localhost",50007
    #create the server,bingding to localhost on port 50007
    server=SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)

    #activate the server; this will keep running until you interrupt the program with ctrl+c
    server.serve_forever()

