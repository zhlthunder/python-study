#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

#<Button-1> 鼠标左键
#<Button-3> 鼠标右键
#<Button-2> 鼠标中键
#<Double-Button-1> 鼠标左键双击
#<Double-Button-3> 鼠标右键双击
#<Double-Button-2> 鼠标中键双击

#<Triple-Button-1> 鼠标左键三击
#<Triple-Button-3> 鼠标右键三击
#<Triple-Button-2> 鼠标中键三击

def func(event):
    print(event.x,event.y)  ##相对于小控件的坐标位置

button1=tkinter.Button(win,text="leftmouse_click")
#bind 给控件绑定事件，（触发事件的操作，执行的函数）
button1.bind("<Button-1>",func)
button1.pack()

button2=tkinter.Button(win,text="middlemouse_click")
button2.bind("<Button-2>",func)
button2.pack()

button3=tkinter.Button(win,text="rightmouse_click")
button3.bind("<Button-3>",func)
button3.pack()


button4=tkinter.Button(win,text="dd")
button4.bind("<Double-Button-1>",func)
button4.pack()


win.mainloop()

##定义事件有两种方法：
#1.command=  有的空间控件支持，有的控件不支持；
#2.bind 可以对所有的控件适用