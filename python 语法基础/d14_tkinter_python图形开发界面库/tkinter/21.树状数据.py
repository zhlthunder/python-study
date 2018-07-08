#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter
from tkinter import ttk


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")


tree=ttk.Treeview(win)
tree.pack()


##添加一级树枝
treeF1=tree.insert("",0,"中国",text="china",values=("F1"))
treeF2=tree.insert("",1,"美国",text="USA",values=("F2"))
treeF3=tree.insert("",2,"英国",text="UK",values=("F3"))

##添加二级树枝
treeF1_1=tree.insert(treeF1,0,"黑龙江",text="黑龙江hei",values=("F1_1"))
treeF1_2=tree.insert(treeF1,1,"吉林",text="吉林JI",values=("F1_2"))
treeF1_2=tree.insert(treeF1,2,"辽宁",text="辽宁LIAO",values=("F1_3"))


treeF2_1=tree.insert(treeF2,0,"Laker",text="laker",values=("F2_1"))
treeF2_2=tree.insert(treeF2,1,"losangeles",text="losangeles",values=("F2_2"))
treeF2_2=tree.insert(treeF2,2,"shanandio",text="shanandio",values=("F2_3"))


treeF3_1=tree.insert(treeF3,0,"lendon",text="lendon",values=("F3_1"))
treeF3_2=tree.insert(treeF3,1,"weiershi",text="weiershi",values=("F3_2"))
treeF3_2=tree.insert(treeF3,2,"bali",text="bali",values=("F3_3"))


##三级树枝
treeF1_1_1=tree.insert(treeF1_1,0,"哈尔滨",text="哈尔滨")
treeF1_1_2=tree.insert(treeF1_1,1,"五常",text="五常")

win.mainloop()