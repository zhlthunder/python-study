#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
import tkinter
from tkinter import ttk
import os


class TreeWindow(tkinter.Frame):
    def __init__(self,master,path,otherwin):
        frame=tkinter.Frame(master)
        frame.grid(row=0,column=0)

        self.otherwin=otherwin
        self.tree=ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT,fill=tkinter.Y)

        root=self.tree.insert("","end",text=self.getLastPath(path),open=True,values=(path))
        self.loadTree(root,path)


        ##滚动条
        self.sy=tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)


        ##绑定事件
        self.tree.bind("<<TreeviewSelect>>",self.func)

    def func(self,event):
        self.v=event.widget.selection()
        for sv in self.v:
            file=self.tree.item(sv)["text"]
            self.otherwin.ev.set(file)
            # print(file)
            apath=self.tree.item(sv)["values"][0]
            print(apath)




    def getLastPath(self,path):
        pathlist=os.path.split(path)
        return pathlist[-1]

    def loadTree(self,parent,parentpath):
        for filename in os.listdir(parentpath):
            abspath=os.path.join(parentpath,filename)
            #插入树枝
            treey=self.tree.insert(parent,"end",text=self.getLastPath(abspath),values=(abspath))
            ##判断是否是目录：
            if os.path.isdir(abspath):
                self.loadTree(treey,abspath)
