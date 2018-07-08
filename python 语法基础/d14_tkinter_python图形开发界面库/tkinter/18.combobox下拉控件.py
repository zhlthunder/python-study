#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter
from tkinter import ttk




win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

#绑定变量：  切记，变量绑定一定要放在win的定义下面，否则会报错
cv=tkinter.StringVar()

com=ttk.Combobox(win,textvariable=cv)
com.pack()
##设置下拉数据
com["value"]=("helongjiang","jilin","haerbin","jiangsu","nanjing","guangdong")

##设置默认值
com.current(0) ##即设置默认值的下标，对应的就是上面元祖中的第一个元素




##绑定事件 (当改变box中的值时，会执行这个事件)
def func(event):
    # print("zhl is good man")
    # print(com.get())  ##获取当前的选择的值，也可以使用绑定变量的方式
    print(cv.get()) ##通过绑定变量获取当前选择的值

com.bind("<<ComboboxSelected>>",func)

win.mainloop()