#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from .base import Base
class message(Base):
    def __init__(self,msg):
        ##短信相关的初始化代码
        self.msg=msg

    def send(self):
        print("send message"+self.msg)