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

##直接给整个窗口设置键盘事件； 只响应输入A 键时执行操作，其它键不响应；
win.bind("a",func)


win.mainloop()