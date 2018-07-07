#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

##菜单条，就是菜单栏的横条
menubar=tkinter.Menu(win)
win.config(menu=menubar)


def func():
    print("zhl is a good man")

##创建一个菜单选项，比如 菜单栏中的file选项；
menu1=tkinter.Menu(menubar,tearoff=False)
##给菜单选项添加内容，就是file菜单的下拉子菜单
for item in ["python","c","c++","swift","c-sharp","java","php","shell","bat","退出"]:
    if item=="退出":
        menu1.add_separator()  ##添加分割线
        menu1.add_command(label=item,command=win.quit)
    else:
        menu1.add_command(label=item,command=func)

##向菜单条上添加菜单选项， 就是将file安装到菜单条上
menubar.add_cascade(label="语言",menu=menu1)


menu2=tkinter.Menu(menubar,tearoff=False)
menu2.add_command(label="red")
menu2.add_command(label="green")
menubar.add_cascade(label="颜色",menu=menu2)


win.mainloop()