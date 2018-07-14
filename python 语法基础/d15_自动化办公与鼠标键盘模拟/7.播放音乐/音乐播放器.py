#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import tkinter,os,sys,time
from music_play import Music
import threading


win=tkinter.Tk()
win.title("音乐播放")
win.geometry("600x400+200+50")

FILENAME=''

##显示歌曲列表
lb=tkinter.Listbox(win,selectmode=tkinter.BROWSE,width=30)
lb.pack(side=tkinter.LEFT,fill=tkinter.Y)
path=os.getcwd()
musiclist=os.listdir(path)
for item in musiclist:
    if '.mp3' in item:
        lb.insert(tkinter.END,item)
##设置初始值
lb.select_set(0)
cur=lb.get(lb.curselection())
FILENAME=os.path.join(os.getcwd(),cur)

##点击选择要播放的歌曲
def getitem(event):
    cur=lb.get(lb.curselection())
    print(cur)
    global FILENAME
    ##完整的文件路径：
    FILENAME=os.path.join(os.getcwd(),cur)
    # print(FILENAME)

lb.bind('<Button-1>',getitem)


def play_sub(filename):
    global obj
    obj=Music(filename)
    obj.play()

##播放音乐
def play():
    print(FILENAME)
    ##创建一个子进程用于播放音乐
    global t
    t=threading.Thread(target=play_sub,args=(FILENAME,))
    t.setDaemon(True)
    t.start()



play=tkinter.Button(win,text="播  放",command=play)
play.pack(anchor='nw',padx=80,pady=20)

def pause():
    obj.pause()

pause=tkinter.Button(win,text="暂  停",command=pause)
pause.pack(anchor='nw',padx=80,pady=20)

def stop():
    obj.stop()

stop=tkinter.Button(win,text="停  止",command=stop)
stop.pack(anchor='nw',padx=80,pady=10)

def next():
    # print("next")
    obj.stop()##停止当前的曲目播放
    cc=lb.curselection()
    lb.select_clear(cc[0])
    if cc[0]+1==lb.size():
        index=0
    else:
        index=cc[0]+1
    cur=lb.get(index)
    lb.select_set(index)
    print(cur)
    FILENAME=os.path.join(os.getcwd(),cur)
    t=threading.Thread(target=play_sub,args=(FILENAME,))
    t.setDaemon(True)
    t.start()

next=tkinter.Button(win,text="下一曲",command=next)
next.pack(anchor='nw',padx=80,pady=20)

exit=tkinter.Button(win,text="退  出",command=win.quit)
exit.pack(anchor='nw',padx=80,pady=20)


win.mainloop()


# path=r'C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 语法基础\d15_自动化办公与鼠标键盘模拟\7.播放音乐\我喜欢上你时的内心活动.mp3'
# obj=Music(path)
# obj.play()


##布局相关，请承诺参考： https://www.cnblogs.com/zhangpengshou/p/3626137.html