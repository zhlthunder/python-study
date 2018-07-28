#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter,socket,threading

CK=None
USER=None
CURSELECT=None
ip='127.0.0.1'
port=9999

win=tkinter.Tk()
win.title("client")
win.geometry("400x500+200+0")



tkinter.Label(win,text="username").grid(row=0,column=0)
euser=tkinter.Variable()
entry3=tkinter.Entry(win,textvariable=euser).grid(row=0,column=1)


def getmsg():
    while True:
        ret=CK.recv(1024)
        if 'users' in ret:
            #信息来自服务器端
            print(ret)
            print(type(ret))
            userlist=eval(ret.split(":")[1])
            # print(userlist)
            listbox.delete(0,tkinter.END)
            for user in userlist:
                if user!=USER:
                    listbox.insert(tkinter.END,user+'\n')
        else:
            ret = ret + '\n'
            text.insert(tkinter.INSERT, ret.decode("utf-8"))

def connect_server():
    global USER

    user=euser.get()
    USER=user
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(user.encode("utf-8"))##发送用户账号信息
    print("登陆成功")
    text.insert(tkinter.INSERT,"登陆成功。。\n".decode("utf-8"))
    global CK
    CK=s ##供这个用户全局使用的套接字
    ##创建一个线程，用于和其它好友发送的数据
    tc=threading.Thread(target=getmsg)
    tc.start()


button1=tkinter.Button(win,command=connect_server,text="登陆").grid(row=0,column=2)


##接收在线用户窗口
tkinter.Label(win,text="在线好友:").grid(row=1,column=0)
listbox=tkinter.Listbox(win,height=15,width=10)
listbox.grid(row=2,column=0)

##接收信息的窗口
tkinter.Label(win,text="聊天信息:").grid(row=1,column=1)
text=tkinter.Text(win,width=30)
text.grid(row=2,column=1)

def sendmsg():
    #获取当前选中的用户的信息
    uu=listbox.get(listbox.curselection())
    listbox.select_set(listbox.curselection())
    # print(uu)
    ##获取输入框中的内容
    content=entry4.get()
    sendstr=uu+":"+content
    # print(sendstr)
    CK.send(sendstr.encode("utf-8"))

tkinter.Label(win,text="输入:").grid(row=3,column=0)
entry4=tkinter.Entry(win)
entry4.grid(row=3,column=1)



button2=tkinter.Button(win,command=sendmsg,text="发送").grid(row=4,column=2)

win.mainloop()