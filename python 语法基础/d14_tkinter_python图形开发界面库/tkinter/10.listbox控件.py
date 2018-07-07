#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

"""
列表框控件，可以包含一个或多个文本框
作用：可以在listbox控件的小窗口显示一个字符串；
"""

import tkinter


win=tkinter.Tk()
win.title("zhl")
win.geometry("400x400+200+0")

##1.创建一个listbox,
#功能1： 添加元素；
lb=tkinter.Listbox(win,selectmode=tkinter.BROWSE)
lb.pack()

for item in ["good","nice","handsom","high","aaa","bbb"]:
    ##按顺序依次向后添加
    lb.insert(tkinter.END,item)

##在开始位置添加
# lb.insert(tkinter.ACTIVE,"cool")
##在最后位置添加一串信息；
# lb.insert(tkinter.END,["very good","very nice"])

##功能2：删除元素，
#参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只删除第一个索引处的内容
# lb.delete(1,3) ##删除下标为1,2,3的元素,注意下标从0开始，切记！！！！
# lb.delete(1) ##只删除下标为1的元素

##功能3：选中元素
#参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只选中第一个索引处的内容
# lb.select_set(2,4)  #选中下标为2,3,4的元素
# lb.select_set(2)  ##选中下标为2的元素

##功能4：取消选中
#参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只取消选中第一个索引处的内容
# lb.select_set(2,5) ##先选中2-5
# lb.select_clear(2,4) ##再取消选中2-4，这样只有5是选中的；

##也支持只取消单个元素：
# lb.select_clear(3)


##功能5：获取列表中元素的个数
# print(lb.size())

##功能6：获取值
#参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只获取第一个索引处的内容
# print(lb.get(2,4))
# print(lb.get(2,))


#功能7：返回当前的索引项，不是item元素， 即打印当前选中的项的索引
lb.select_set(2,5) ##先选中2-5
print(lb.curselection()) ##打印的索引 2,3,4,5

##功能8：判断一个选项是否被选中
print(lb.select_includes(1))  ##判断当前 索引 1是否被选中

win.mainloop()

