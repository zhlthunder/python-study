#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 基于scoped_session实现线程安全

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from models import *

#1.创建连接池
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/zhl", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

##2.从连接池中获取数据库连接
session = scoped_session(Session) ##对比orm数据库操作_2.py只修改这一个


##3.执行ORM操作
obj1 = Users(name="jack",email="jack@163.com")
session.add(obj1)
session.commit()

##4.关闭数据库连接（实际上是将连接放回连接池，并没有关闭）
session.close()
