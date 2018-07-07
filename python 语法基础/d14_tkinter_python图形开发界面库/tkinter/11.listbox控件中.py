#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

##绑定变量
lbv=tkinter.StringVar()



##与BROWSE 功能相似，但是不支持鼠标移动选中元素
#browse时， 长按鼠标左键，移动鼠标时移动选中的元素；
#SINGLE时， 长按鼠标左键，移动鼠标时不能移动选中的元素；
lb=tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)
lb.pack()

for item in ["good","nice","handsom","high","aaa","bbb"]:
    ##按顺序依次向后添加
    lb.insert(tkinter.END,item)

##返回当前列表中的所有元素
# print(lbv.get())

##重新设置所有的选项；
# lbv.set(("1","2","3"))

##绑定事件的第二种方法，之前的第一种方法是command=：
##注意，这个函数需要一个参数 event, 但调用时不需要传参数过来
def myprint(event):
    # print(lb.curselection()) ##获取双击的元素的下标
    print(lb.get(lb.curselection())) ##获取双击的元素

#Double-Button-1 意思是双击鼠标左键  ， 1表示鼠标左键；
lb.bind('<Double-Button-1>',myprint)



win.mainloop()