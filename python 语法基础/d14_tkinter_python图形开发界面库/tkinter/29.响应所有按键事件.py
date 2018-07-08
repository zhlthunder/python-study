#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

label=tkinter.Label(win,text="zhl is good man")
##设置焦点
label.focus_set()  ##切记，必须设置焦点后才可以响应键盘事件
label.pack()

def func(event):
    print("char=",event.char)
    print("keycode=",event.keycode)


label.bind("<Key>",func)

#<Key>  响应所有的按键，当单击一个键时触发事件

win.mainloop()