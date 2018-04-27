#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.update(DEBUG=True)  # 参数形式配置

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

##日志输出
app.logger.debug('A value for debugging')
# app.logger.warning('A warning occurred (%d apples)', 42)
# app.logger.error('An error occurred')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)

