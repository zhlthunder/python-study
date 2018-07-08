#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")



def func(event):
    print("char=",event.char)
    print("keycode=",event.keycode)

##直接给整个窗口设置键盘事件；
win.bind("<Key>",func)


win.mainloop()