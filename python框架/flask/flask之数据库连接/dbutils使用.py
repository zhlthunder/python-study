#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#refer : http://www.cnblogs.com/wupeiqi/articles/8184686.html
##通过源码安装dbutils
# DBUtils是Python的一个用于实现数据库连接池的模块。
#
# 此连接池有两种连接模式：
#
# 模式一：为每个线程创建一个连接，线程即使调用了close方法，也不会关闭，只是把连接重新放到连接池，供自己线程再次使用。当线程终止时，连接自动关闭。
#//这种模式不好， 首先，连接的利用率较低，且当任务较多时，连接也会很多。  （这种模式，内部是采用threading.local实现的，即为每个线程保存数据）

# 模式二：创建一批连接到连接池，供所有线程共享使用。 @@重要，以后写代码，用这种连接方式
# PS：由于pymysql、MySQLdb等threadsafety值为1，所以该模式连接池中的线程会被所有线程共享。

#模式1应用：
import pymysql
from DBUtils.PersistentDB import PersistentDB

POOL = PersistentDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."],即事先执行的一些sql命令
    ping=0,  ##一般写 4或7
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    closeable=False,
    # 如果为False时， conn.close() 实际上被忽略，供下次使用，在线程关闭时，才会自动关闭链接。如果为True时， conn.close()则关闭链接，那么再次调用pool.connection时就会报错，因为已经真的关闭了连接（pool.steady_connection()可以获取一个新的链接）
    threadlocal=None,  # 本线程独享值得对象，用于保存链接对象，如果链接对象被重置
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='mydb',
    charset='utf8'
)

def func():
    conn = POOL.connection(shareable=False)
    cursor = conn.cursor()
    cursor.execute('select * from host')
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()

func()