#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from .base import Base
class Email(Base):
    def __init__(self):
        ##邮箱相关的初始化代码
        pass


    def send(self,msg):
        print("send email: "+msg)
