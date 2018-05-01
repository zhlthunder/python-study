#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from . import app

@app.route('/login')
def login():
    return 'Hello World!---login'
