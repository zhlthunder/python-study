#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter
import os
from treeWindows import TreeWindow
from infoWindow import InfoWindow

win=tkinter.Tk()
win.title("sunnk")
win.geometry("600x400+200+50")

path=r'C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study'
infowin=InfoWindow(win)
treeWin=TreeWindow(win,path,infowin)


win.mainloop()