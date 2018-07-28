#!/usr/bin/env python
# -*- coding: utf-8 -*-



import socket,threading,time
userlist={}
ip='127.0.0.1'
port=9999

def client_process(conn,addr):
    username=conn.recv(1024)
    username=username.decode("utf-8")
    userlist[username]=conn
    print(userlist)
    while True:
        rdata=conn.recv(1024)
        datastr=rdata.decode("utf-8")
        print(datastr)
        ##接收到需要通讯的用户名及内容
        duser,dcontent=datastr.split(":")
        strtransfer=username+" say to:"+duser+dcontent
        userlist[duser.strip('\n')].send(strtransfer.encode("utf-8"))

def sendonline_user():
    users=userlist.keys()
    print(userlist)
    for conn in userlist.values():
        strr="users:"+str(users)
        conn.send(strr)


##启动监控连接的服务器线程
def startserver():
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind((ip, port))
    ss.listen(5)
    print("服务器启动完成，等待客户端连接")
    while True:
        conn,addr=ss.accept()
        tt=threading.Thread(target=client_process,args=(conn,addr))
        tt.start()
        ##但有一个新用户连接上线是，我就需要把当前上线的所有用户的信息发送所有的客户端
        time.sleep(0.3)
        sendonline_user()

startserver()
