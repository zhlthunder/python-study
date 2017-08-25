#!/usr/bin/env python
#coding:utf-8
  
import socket

  #2 处理请求的部分
def handle_request(client):  #这个就是处理请求的入口， client中封装了客户端请求的信息；
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("Hello, Seven")
  
def main():  #1.自定义实现的socket的功能；
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8000))
    # 最多有5个排队
    sock.listen(5)
  
    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()
  
if __name__ == '__main__':
    main()