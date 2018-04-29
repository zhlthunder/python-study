#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##定义了一个基类，用来约束这个类的派生类，如果不定义send方法就会报错，实际上就是定义了一个编程接口
class Base(object):
    def send(self):
        raise NotImplementedError("....")