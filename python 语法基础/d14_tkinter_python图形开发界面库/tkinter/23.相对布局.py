#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

label1=tkinter.Label(win,text="good",bg="blue")
label2=tkinter.Label(win,text="nice",bg="red")


##相对布局，窗体改变对控件有影响
label1.pack(fill=tkinter.Y,side=tkinter.LEFT)
label2.pack(fill=tkinter.X,side=tkinter.TOP)




win.mainloop()