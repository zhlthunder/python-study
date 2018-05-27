#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    return "hello zhlllllll"

if __name__ == '__main__':
    app.run()