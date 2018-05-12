#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##和 orm操作数据库_1.py 功能完整一样，可以忽略此脚本

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import *

#1.创建连接池
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/zhl", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

##2.从连接池中获取数据库连接
session = Session()


##3.执行ORM操作
obj1 = Users(name="thunder",email="zhlasfdsaf@163.com")
session.add(obj1)
session.commit()

##4.关闭数据库连接（实际上是将连接放回连接池，并没有关闭）
session.close()
