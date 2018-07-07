#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter

##创建主窗口
win=tkinter.Tk()

##设置标题
win.title("zhl")

##设置大小和位置：
# 大小：使用宽像素x高的像素， 中间的乘号使用小写的x字母              400x400
#位置：左上角为坐标原点，依次用距离左边和上边的距离表示；和大小之间用+连接；    +200+0 //距离左边200px,距离上边0px;
win.geometry("400x400+200+0")


##进入消息循环

win.mainloop()