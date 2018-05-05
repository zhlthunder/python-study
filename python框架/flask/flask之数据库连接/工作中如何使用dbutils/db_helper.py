#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


import pymysql
from DBUtils.PooledDB import PooledDB
POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制, 闲置的多余连接可以关闭
    maxshared=3,  #重要，源码中这个参数是无效的，设成多少都一样，所以可以忽略这个参数
                  #  链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所以值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
                    #比如连接池中只有5个连接，那么第6个人来的时候就要等待了
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='mydb',
    charset='utf8'
)


##因为我们调用这个类时，没有定义__init__，只是用了它内部的方法
#可以采用@staticmethod，这样就不用self参数了，
#此时调用的时候，可以不用进行实例化，可以执行使用SQLHelper.fetch_all来调用类的方法， 切记，非常重要！！！！！
class SQLHelper(object):

    @staticmethod
    def fetch_all(sql):
        conn = POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()  ##这个关闭不是真的关闭连接，而是把连接释放到连接池中，供其它连接使用
        return result

    @staticmethod
    def fetch_one(sql,args=None):
        conn = POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql,args)
        result = cursor.fetchone()
        conn.close()  ##这个关闭不是真的关闭连接，而是把连接释放到连接池中，供其它连接使用
        return result

    @staticmethod
    def sql_insert(sql,args):
        conn = POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql,args)
        conn.commit()  ##改写数据库时必须要添加的
        conn.close()  ##这个关闭不是真的关闭连接，而是把连接释放到连接池中，供其它连接使用


#关于这个类，另外一种定义方法如下，使用实例化的方法进行定义：
##但使用这种方式时，每次调用的时候都要实例化
"""
class SQLHelper(object):

    def __init__(self):
        self.conn = POOL.connection()
        self.cursor = self.conn.cursor()
    def close(self):
        self.cursor.close()
        self.conn.close()

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.close()  ##这个关闭不是真的关闭连接，而是把连接释放到连接池中，供其它连接使用
        return result

"""
