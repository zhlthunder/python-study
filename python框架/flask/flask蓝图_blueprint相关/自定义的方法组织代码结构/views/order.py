#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from . import app

@app.route('/order')
def order():
    return 'Hello World!---order'