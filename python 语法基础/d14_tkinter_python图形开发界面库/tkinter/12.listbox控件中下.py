#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
# win.geometry("400x400+200+0")  如果要有滚动条，就必须要注释掉这行


##EXTENDED模式：可以使listbox支持shift和control按键，即可以支持同时选中多个选项
lb=tkinter.Listbox(win,selectmode=tkinter.EXTENDED)


for item in ["good","nice","handsom","high1","aaa","bbb","nice","handsom","high3","aaa3","bbb3","nice3","handsom3","high3","aaa3","bbb3"]:
    ##按顺序依次向后添加
    lb.insert(tkinter.END,item)

##按住shift 可以实现连选
##按住control ,可以实现多选

##滚动条
sc=tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
##额外给属性赋值
sc['command']=lb.yview

win.mainloop()