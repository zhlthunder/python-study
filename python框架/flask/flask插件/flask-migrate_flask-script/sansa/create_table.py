#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##离线脚本，用于创建表或删除表


from sansa import create_app
from sansa import db

app = create_app()

with app.app_context(): #必须加载当前app的上下文，即把flask app相关的所有信息都加载到Local（）中
    db.create_all()
    # db.drop_all()