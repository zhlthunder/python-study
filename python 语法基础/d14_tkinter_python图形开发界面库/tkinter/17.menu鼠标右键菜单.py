#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

##菜单条
menubar=tkinter.Menu(win)

##创建一个菜单选项，比如 菜单栏中的file选项；
menu1=tkinter.Menu(menubar,tearoff=False)
##给菜单选项添加内容，就是file菜单的下拉子菜单
for item in ["python","c","c++","swift","c-sharp","java","php","shell","bat"]:
    menu1.add_command(label=item)

##把菜单装载到menubar中
menubar.add_cascade(label="语言",menu=menu1)

def showmenu(event):
    menubar.post(event.x_root,event.y_root)

win.bind('<Button-3>',showmenu)


win.mainloop()