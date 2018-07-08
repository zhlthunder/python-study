#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

label=tkinter.Label(win,text="zhl is good man")
label.pack()

def func(event):
    print(event.x,event.y)

label.bind("<Enter>",func)
label.bind("<Leave>",func)

#<Enter> 当鼠标进入控件区域时触发一次事件
#<Leave> 当鼠标光标离开控件区域时触发一次事件


win.mainloop()