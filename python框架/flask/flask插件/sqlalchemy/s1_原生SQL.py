#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#pip3 install sqlalchemy


##实例1：
# import time
# import threading
# import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy.engine.base import Engine
#
# engine = create_engine(
#     "mysql+pymysql://root:123456@127.0.0.1:3306/mydb?charset=utf8",
#     max_overflow=0,  # 超过连接池大小外最多创建的连接
#     pool_size=5,  # 连接池大小
#     pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
#     pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
# )
#
# conn = engine.raw_connection()
# cursor = conn.cursor()
# cursor.execute(
#     "select * from user"
# )
# result = cursor.fetchall()
# print(result)
# cursor.close()
# conn.close()



##实例2：

import time
import threading
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

engine = create_engine(
    "mysql+pymysql://root:123456@127.0.0.1:3306/mydb?charset=utf8",
    max_overflow=2,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

def task(arg):
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute(
        # "select * from user"
        "select sleep(3)" ##延时命令  @@@@@@@重要，使用sleep可以验证多线程的执行情况，max_overflow=0时，同一时间有5个连接在执行；
    )                                           #max_overflow=2时，同一时间有7个连接在执行； 验证多线程时连接池的使用的情况，@@@@@@@@@@@@@@@@@@@@@@
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()


for i in range(20):
    t = threading.Thread(target=task, args=(i,))
    t.start()