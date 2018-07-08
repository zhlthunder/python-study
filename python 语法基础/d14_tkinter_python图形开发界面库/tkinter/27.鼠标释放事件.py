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

label.bind("<ButtonRelease-1>",func)

#<ButtonRelease-1> 在控件上按住鼠标左键，在释放时触发
#<ButtonRelease-2> 在控件上按住鼠标中键，在释放时触发
#<ButtonRelease-3> 在控件上按住鼠标右键，在释放时触发

win.mainloop()