#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

"""
文本控件，用于显示多行文本
"""

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")


text=tkinter.Text(win,width=40,height=4)
#height:表示显示的行数
text.pack()

str='''Some of you already know, that it’s hard, it’s not easy, it’s hard changing your life. That in the process
of working on your dreams you are going to incur a lot of disappointment, a lot of failure, a lot of pain.
 There are moments that you are going to doubt yourself. You said, God why is this happening to me? I’m
 just trying to take care of my family, trying to give them a good life, I’m not trying to steal or rob
 from anybody. Why does this have to happen to me. For those of you that have experienced some hardships –
 don’t give up on your dream.
'''

##将内容插入text中
text.insert(tkinter.INSERT,str)

win.mainloop()