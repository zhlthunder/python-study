#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


import tkinter


def showinfo():
    print(entry.get())


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")


entry=tkinter.Entry(win)
entry.pack()

button=tkinter.Button(win,text="按钮",command=showinfo)
button.pack()


win.mainloop()