#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


def update():
    message=""
    if hobby1.get()==True:
        message+="money\n"
    if hobby2.get()==True:
        message+="power\n"
    if hobby3.get()==True:
        message+="person\n"
    text.delete(0.0,tkinter.END)  ##清空text中的所有的内容  从第0行到最后一行
    text.insert(tkinter.INSERT,message) ##选中后，将内容显示到text上

win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

hobby1=tkinter.BooleanVar()
hobby2=tkinter.BooleanVar()
hobby3=tkinter.BooleanVar()

check1=tkinter.Checkbutton(win,text="money",variable=hobby1,command=update)
check1.pack()
check2=tkinter.Checkbutton(win,text="power",variable=hobby2,command=update)
check2.pack()
check3=tkinter.Checkbutton(win,text="person",variable=hobby3,command=update)
check3.pack()


text=tkinter.Text(win,width=50,height=5)
text.pack()

win.mainloop()