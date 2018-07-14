#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# import win32com
# from win32com.client import Dispatch, constants
# ppt = win32com.client.Dispatch('PowerPoint.Application')
# ppt.Visible = 1
# path=r'C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 语法基础\d15_自动化办公与鼠标键盘模拟\5.读取ppt文件\aa.pptx'
# pptSel = ppt.Presentations.Open(path)
# win32com.client.gencache.EnsureDispatch('PowerPoint.Application')
#
# #get the ppt's pages
# slide_count = pptSel.Slides.Count
# for i in range(1,slide_count + 1):
#   shape_count = pptSel.Slides(i).Shapes.Count
#   print(shape_count)
#   for j in range(1,shape_count + 1):
#     if pptSel.Slides(i).Shapes(j).HasTextFrame:
#       s = pptSel.Slides(i).Shapes(j).TextFrame.TextRange.Text
#       print (s.encode('utf-8')+ "\n")
#
# ppt.Quit()

import win32com
from win32com.client import Dispatch, constants
ppt = win32com.client.Dispatch('PowerPoint.Application')
ppt.Visible = 1
pptSel = ppt.Presentations.Open("aa.pptx")
win32com.client.gencache.EnsureDispatch('PowerPoint.Application')
f = open("aa.txt","w")
slide_count = pptSel.Slides.Count
for i in range(1,slide_count + 1):
  shape_count = pptSel.Slides(i).Shapes.Count
  print(shape_count)
  for j in range(1,shape_count + 1):
    if pptSel.Slides(i).Shapes(j).HasTextFrame:
      s = pptSel.Slides(i).Shapes(j).TextFrame.TextRange.Text
      f.write(s.encode('utf-8') + "\n")
f.close()
ppt.Quit()


##待排错。。。。