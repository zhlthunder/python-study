#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")



def update():
    val=r.get()##获取选择时对应的值
    print(val)

##绑定变量，单选框绑定一个变量
##一组单选框需要绑定同一个变量，绑定同一变量的所有单选框是一组单选框
r=tkinter.IntVar() ##此时只可以获取整形的value
# r=tkinter.StringVar() ##此时可以获取字符串型的value

##text是显示的信息
##value 是选择时对应的值
radio1=tkinter.Radiobutton(win,text="one",value=1,variable=r,command=update)
radio1.pack()

radio2=tkinter.Radiobutton(win,text="two",value=2,variable=r,command=update)
radio2.pack()

radio3=tkinter.Radiobutton(win,text="three",value=3,variable=r,command=update)
radio3.pack()


win.mainloop()