#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl




from flask import Flask,render_template
# from flask.ext.bootstrap import Bootstrap  #方式1
from flask_bootstrap import Bootstrap  #方式2

app=Flask(__name__)
bootstrap=Bootstrap(app)

@app.route('/index')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()