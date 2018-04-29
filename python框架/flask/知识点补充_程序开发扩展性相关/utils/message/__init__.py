#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import settings
import importlib

def send_msgs(msg):
    for path in settings.MSG_LIST:
        m,c=path.rsplit('.',maxsplit=1)
        md=importlib.import_module(m) ##导入模块
        cls=getattr(md,c)   ##找到类
        obj=cls()   ##实例化
        obj.send(msg)

##此处非常重要，根据字符串导入模块，然后使用反射获取类名