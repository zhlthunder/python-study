#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask
from db_helper import SQLHelper
app = Flask(__name__)

##为了避免连接部分的代码在每个视图函数中重复使用，可以在db_helper中定义一个类来完成对数据库的操作


@app.route('/')
def index():
    #读取操作
    ret=SQLHelper.fetch_all('select * from host')
    print(ret)

    #插入操作：
    # SQLHelper.sql_insert('insert into host(hostname,ip_addr,port) values(%s,%s,%s)',('host22','22.22.22.22',80))
    return 'Hello World!'


if __name__ == '__main__':
    app.run()