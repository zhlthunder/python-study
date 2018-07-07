#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

##属性：MULTIPLE  执行多选，可以依次点击，选中多个元素
lb=tkinter.Listbox(win,selectmode=tkinter.MULTIPLE)
lb.pack()

for item in ["good","nice","handsom","high","aaa","bbb"]:
    lb.insert(tkinter.END,item)


win.mainloop()