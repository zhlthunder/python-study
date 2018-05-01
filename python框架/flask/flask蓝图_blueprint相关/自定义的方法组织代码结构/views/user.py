#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from . import app

@app.route('/user')
def user():
    return 'Hello World!---user'