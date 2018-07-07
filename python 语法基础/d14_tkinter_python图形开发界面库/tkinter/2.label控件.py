#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")


"""
label:标签控件，可以显示文本
"""
#参数说明：
##win:主窗口对象名
#text：显示文本内容
#bg: 背景色
#fg：字体颜色
#font 字体及size
#width: 设置宽度百分比， 以窗口全屏的像素来参考的。
#height:设置高度百分比，以窗口全屏的像素来参考的，但验证时有问题，待继续确认详细的功能
#wraplength 指定text文本中，多宽进行换行；
#justify 对齐方式
#anchor: 位置， n  e  s   w  c  // n--north  e--east  s--south  w--west c--center, 也可以组合 ne se sw nw
label=tkinter.Label(win,
                    text="thunder",
                    bg="green",
                    fg="red",
                    font=("黑体",15),
                    width=50,
                    height=4,
                    wraplength=100,
                    justify="left",
                    anchor="w",
                    )

##将label显示在窗口中，
label.pack()

win.mainloop()