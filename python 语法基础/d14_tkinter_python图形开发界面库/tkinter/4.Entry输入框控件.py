#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


"""
entry :是输入控件
也可以用于显示简单的文本内容
"""

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")



entry1=tkinter.Entry(win)
entry1.pack()

entry2=tkinter.Entry(win,show="*")##show：设置显示的字符,比如用于密码输入用
entry2.pack()


##绑定变量：
e=tkinter.Variable() ##定义变量对象
entry3=tkinter.Entry(win,textvariable=e) ##将变量绑定到输入框上
entry3.pack()

#e就代表输入框这个对象
#设置值
e.set("zhl is good man")

##获取输入框的值
print(e.get())  ##取值方法1
print(entry3.get()) ##取值方法2

win.mainloop()