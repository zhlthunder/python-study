#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#修改背景图片
#regedit==>HEKY_CURRENT_USER==>Control Panel==>Desktop==>WallPaper

import win32api
import win32con
import win32gui

def setWallPaper(path):
    #打开注册表,设置数据
    reg_key=win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)

    ##设置图片的拉伸: 0 居中， 6 适应， 10 填充
    win32api.RegSetValueEx(reg_key,"WallpaperStyle",0,win32con.REG_SZ,"2")



    ##设置图片  #SPIF_SENDWININICHANGE 立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)


path=r'C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 语法基础\d15_自动化办公与鼠标键盘模拟\8.修改背景图片\timg.jpg'
setWallPaper(path)