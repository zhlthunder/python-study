#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter
import socket
import threading

win=tkinter.Tk()
win.title("qq服务器")
win.geometry("400x400+200+20")


ck=None


def getinfo():
    while True:
        data=ck.recv(1024)
        text.insert(tkinter.INSERT,data.decode("utf-8"))

def  connectserver():
    global ck
    ipstr=eip.get()
    portstr=eport.get()
    userstr=euser.get()
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((ipstr,int(portstr)))
    client.send(userstr.encode("utf-8"))  ##将我的用户名发送给服务端；
    ck=client  ##这个套接字是全局需要使用的

    ##创建一个线程，等待接收数据
    t=threading.Thread(target=getinfo)
    t.start()


def sendmail():
    friend=efriend.get()  ##给谁发
    sendstr=esend.get() ##要发送的内容
    sendstr=friend+":"+sendstr  ##整合要发送的数据
    ck.send(sendstr.encode("utf-8"))



labeluser=tkinter.Label(win,text="username").grid(row=0,column=0)
euser=tkinter.Variable()
entryuser=tkinter.Entry(win,textvariable=euser).grid(row=0,column=1)

labelip=tkinter.Label(win,text="ip").grid(row=1,column=0)
eip=tkinter.Variable()
entryip=tkinter.Entry(win,textvariable=eip).grid(row=1,column=1)

labelport=tkinter.Label(win,text="port").grid(row=2,column=0)
eport=tkinter.Variable()
entryport=tkinter.Entry(win,textvariable=eport).grid(row=2,column=1)

button=tkinter.Button(win,text="连接",command=connectserver).grid(row=3,column=0)


text=tkinter.Text(win,width=30,height=5)
text.grid(row=4,column=0)


esend=tkinter.Variable()
entrysend=tkinter.Entry(win,textvariable=esend).grid(row=5,column=0)

efriend=tkinter.Variable()
entryfriend=tkinter.Entry(win,textvariable=efriend).grid(row=6,column=0)
button2=tkinter.Button(win,text="发送",command=sendmail).grid(row=6,column=1)
win.mainloop()