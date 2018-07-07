#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

"""
数据范围控件
"""

##绑定变量
v=tkinter.StringVar()

def update():
    print(v.get())

#increment 设置步长
#values 最好不要和from_ 和 to同时使用
#command  ##只要值改变，就会执行对应的事件函数；
sp=tkinter.Spinbox(win,from_=0,to=100,increment=5,textvariable=v,command=update)
# sp=tkinter.Spinbox(win,values=(0,2,4,6,8))  #即指定取值范围
sp.pack()

##设置值 ,注意需要绑定变量才可以取值和设置值；
# v.set(20)

##取值
# print(v.get())


win.mainloop()