#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


def func():
    print("zhl is  good man")

win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")


##text:定义按钮上显示的命名
##command 定义点击按钮触发的函数
##height,width: 设置按钮的宽高
button1=tkinter.Button(win,text="按钮",command=func,width=5,height=5)
button1.pack()

button2=tkinter.Button(win,text="按钮",command=lambda:print("it is button2"),width=5,height=5)
button2.pack()


button3=tkinter.Button(win,text="退出",command=win.quit,width=5,height=5)
button3.pack()



win.mainloop()