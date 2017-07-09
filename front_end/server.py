#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##http 请求本质上就是一种socket请求；
##且http 通信传递的是字符串

# import socket
# def handle_request(client):
#     buf=client.recv(1024)
#     client.send("HTTP/1.1 200 OK\r\n\r\n")
#     # client.send("zhuhonglei")
#     # client.send("<h1>zhuhonglei<h1>")
#     client.send("<h1 style='color:red;'>zhuhonglei<h1>")
#     #总结：即服务器端返回的永远都是字符串，根据字符串不同的格式，浏览器会去分析字符串，按照特定的语法进行解析并显示
#     ##所以，学习html,学习的就是它的语法规则及对应关系
#
# def main():
#     sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     sock.bind(('localhost',8003))
#     sock.listen(5)
#
#     while True:
#         connection,address=sock.accept()
#         handle_request(connection)
#
# if __name__=='__main__':
#     if __name__ == '__main__':
#         main()


##采用读取文件的方式进行，这是所有的web 服务器实现的鼻祖，即最根本的原理都是这样的。
import socket
def handle_request(client):
    buf=client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    with open('index.html','r') as f:
        data=f.read()
        client.sendall(data)

def main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8003))
    sock.listen(5)

    while True:
        connection,address=sock.accept()
        handle_request(connection)

if __name__=='__main__':
    if __name__ == '__main__':
        main()