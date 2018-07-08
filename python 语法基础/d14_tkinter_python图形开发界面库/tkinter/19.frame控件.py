#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")


"""
框架控件：
在屏幕上显示一个矩形区域，多作为容器控件

"""


fram=tkinter.Frame(win) ##创建一个长方形的区域1
fram.pack()

##left
frm_1=tkinter.Frame(fram)#在区域1内部创建一个区域2
tkinter.Label(frm_1,text="左上",bg="pink").pack(side=tkinter.TOP) ##在区域2上添加区域
tkinter.Label(frm_1,text="左下",bg="blue").pack(side=tkinter.TOP)##在区域2上添加区域
frm_1.pack(side=tkinter.LEFT)


##right
frm_2=tkinter.Frame(fram)#在区域1内部创建一个区域3
tkinter.Label(frm_2,text="右上",bg="red").pack(side=tkinter.TOP)#在区域3上添加区域
tkinter.Label(frm_2,text="右下",bg="yellow").pack(side=tkinter.TOP) #在区域3上添加区域
frm_2.pack(side=tkinter.RIGHT)

win.mainloop()