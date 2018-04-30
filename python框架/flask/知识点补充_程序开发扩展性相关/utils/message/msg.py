#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from .base import Base
class message(Base):
    def __init__(self):
        ##短信相关的初始化代码
        pass

    def send(self,msg):
        print("send message: "+msg)
