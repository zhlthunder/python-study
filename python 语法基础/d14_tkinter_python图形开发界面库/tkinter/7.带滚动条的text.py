#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

"""
文本控件，用于显示多行文本
"""

import tkinter


win=tkinter.Tk()
win.title("zhl")
# win.geometry("400x400+200+0")  ##切记，配置滚动条时需要注释掉这行，否则滚动条无效

##创建滚动条
scroll=tkinter.Scrollbar()

text=tkinter.Text(win,width=40,height=4)

##side 表示放到窗口的哪一侧
##fill 表示填充整个Y轴
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)

##为text也配置side和fill参数
##这样整个窗口就是左侧是text,右侧是滚动条
text.pack(side=tkinter.LEFT,fill=tkinter.Y)

##关联text和scroll
scroll.config(command=text.yview)  ##这个的作用的，滚动条滚动时文本会跟着动；
text.config(yscrollcommand=scroll.set) ##这个的作用是，文本动时，滚动条也跟着动；


str='''Some of you already know, that it’s hard, it’s not easy, it’s hard changing your life. That in the process
of working on your dreams you are going to incur a lot of disappointment, a lot of failure, a lot of pain.
 There are moments that you are going to doubt yourself. You said, God why is this happening to me? I’m
 just trying to take care of my family, trying to give them a good life, I’m not trying to steal or rob
 from anybody. Why does this have to happen to me. For those of you that have experienced some hardships –
 don’t give up on your dream.
 of working on your dreams you are going to incur a lot of disappointment, a lot of failure, a lot of pain.
 There are moments that you are going to doubt yourself. You said, God why is this happening to me? I’m
 just trying to take care of my family, trying to give them a good life, I’m not trying to steal or rob
 from anybody. Why does this have to happen to me. For those of you that have experienced some hardships –
 don’t give up on your dream.
'''

##将内容插入text中
text.insert(tkinter.INSERT,str)

win.mainloop()