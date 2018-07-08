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

label.bind("<B1-Motion>",func)
#<B1-Motion>  在控件上按住鼠标，并移动鼠标时触发这个事件， 1：表示鼠标左键  2：中键， 3：右键

win.mainloop()