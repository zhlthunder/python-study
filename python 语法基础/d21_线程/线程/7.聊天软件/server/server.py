#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter
import socket
import threading


win=tkinter.Tk()
win.title("qq服务器")
win.geometry("400x400+200+20")

users={}

def run(conn,addr):
    print("###############")

    # print("%s---%s连接成功"%(str(conn),addr))
    # while True:
    username=conn.recv(1024)
    users[username.decode("utf-8")]=conn ##保存这个用户的信息
    print(users)

    while True:
        rdata=conn.recv(1024)
        datastr=rdata.decode("utf-8")
        infolist=datastr.split(":")
        users[infolist[0]].send(username+("说:"+infolist[1]).encode("utf-8"))


##在这个子线程中跑服务器监控程序，如果直接放到主线程中，会导致界面卡死
def start():
    ipstr=eip.get()
    portstr=eport.get()
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ipstr,int(portstr)))
    server.listen(10)
    printstr="服务器启动成功"
    text.insert(tkinter.END,printstr)
    while True:
        conn,addr=server.accept()
        t=threading.Thread(target=run,args=(conn,addr))
        t.start()


def startserver():
    s=threading.Thread(target=start)
    s.start()





labelIP=tkinter.Label(win,text="IP").grid(row=0,column=0)
labelPORT=tkinter.Label(win,text="PORT").grid(row=1,column=0)
eip=tkinter.Variable()
eport=tkinter.Variable()
entryip=tkinter.Entry(win,textvariable=eip).grid(row=0,column=1)
entryport=tkinter.Entry(win,textvariable=eport).grid(row=1,column=1)
button=tkinter.Button(win,text="启动",command=startserver).grid(row=2,column=0)

text=tkinter.Text(win,width=30,height=10)
text.grid(row=3,column=0)


win.mainloop()