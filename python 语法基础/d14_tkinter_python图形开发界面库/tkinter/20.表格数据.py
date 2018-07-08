#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter
from tkinter import ttk

win=tkinter.Tk()
win.title("zhl")
win.geometry("600x400+200+0")


##表格
tree=ttk.Treeview(win)
tree.pack()
##定义列
tree["columns"]=("姓名","年龄","身高","体重")
#设置列,列还不显示
##设置列宽度
tree.column("姓名",width=100)
tree.column("年龄",width=100)
tree.column("身高",width=100)
tree.column("体重",width=100)

##设置列的列名
tree.heading("姓名",text="姓名--name")
tree.heading("年龄",text="年龄--age")
tree.heading("身高",text="身高--height")
tree.heading("体重",text="体重--weight")

##要求上面三处：  定义列，设置列，设置列的列名， 的名称要一一对应，否则会报错；


#添加数据
tree.insert("",0,text="line1",values=("luyanxu","23","170cm","80kg"))
tree.insert("",1,text="line2",values=("jack","33","175cm","90kg"))
tree.insert("",3,text="line3",values=("tom","43","165cm","60kg"))

win.mainloop()