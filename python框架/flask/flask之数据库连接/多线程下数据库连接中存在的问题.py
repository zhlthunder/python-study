#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


#单线程模式下执行下面的代码不会有任何问题
import pymysql
CONN = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='123456',
                       database='mydb',
                       charset='utf8')

cursor = CONN.cursor()
cursor.execute('select * from host')
result = cursor.fetchall()
cursor.close()

print(result)

"""
说明：单进程单线程的模式下，上面的代码执行时不会有问题，因为同一时间只有一个线程在操作数据库
但当应用到多线程的模式时，可能就会有问题，比如看下下面的例子
"""

##第一个问题：
##当在flask的视图函数中按下面的方式组织代码时，每个客户请求进来时，比如后台是多线程的，
##每个用户请求到来时，都要建立一次数据库连接， 这样当用户量增加时，数据的连接就会线性增加，即数据库的压力增大，所以这种方法应用受限
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    import pymysql
    CONN = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='123456',
                           database='mydb',
                           charset='utf8')

    cursor = CONN.cursor()
    cursor.execute('select * from host')
    result = cursor.fetchall()
    cursor.close()

    print(result)

if __name__ == '__main__':
    app.run()

##第二个问题：
##只建立一次连接如果呢？
#这样就会出现查询到的数据不是我们需要的，即数据库游标操作的代码会因为多线程操作时发生混乱
from flask import Flask
app = Flask(__name__)
import pymysql
CONN = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='123456',
                           database='mydb',
                           charset='utf8')

@app.route('/')
def index():
    cursor = CONN.cursor()
    cursor.execute('select * from host')
    result = cursor.fetchall()
    cursor.close()

    print(result)

if __name__ == '__main__':
    app.run()

##首先想到的一个解决办法是为游标操作的代码加锁, 这种方法可以实现，但无法实现并发

from flask import Flask
import  threading
app = Flask(__name__)
import pymysql
CONN = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='123456',
                           database='mydb',
                           charset='utf8')

@app.route('/')
def index():
    with threading.Lock():
        cursor = CONN.cursor()
        cursor.execute('select * from host')
        result = cursor.fetchall()
        cursor.close()

        print(result)

if __name__ == '__main__':
    app.run()

"""
##为了要解决上面的问题而进行的讨论

1.不能为每个用户创建一个链接；
2.创建一定数量的连接池，如果有人来，就从连接池中拿取一个连接处理用户请求。

使用dbuitls来创建连接池
"""
