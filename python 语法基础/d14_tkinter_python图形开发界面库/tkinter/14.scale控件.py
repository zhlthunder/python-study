#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")


"""
供用户通过拖拽指示器改变变量的值，可以水平，也可以竖直的，比如 音量控制的scale

"""
# orient=tkinter.HORIZONTAL 控制水平或竖直orient=tkinter.VERTICAL
##length: 水平时，表示宽度， 竖直时，表示高度；
##tickinterval 选择值将会为改制的倍数

scale1=tkinter.Scale(win,from_=0,to=100,orient=tkinter.HORIZONTAL,tickinterval=10,length=200)
scale1.pack()

##获取值
# print(scale1.get())

def shownum():
    print(scale1.get())
tkinter.Button(win,text="按钮",command=shownum).pack()

##设置值
scale1.set(20)


win.mainloop()