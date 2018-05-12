#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import threading

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.engine.result import ResultProxy
from models import Users

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/zhl", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

session = Session()

# 查询
# cursor = session.execute('select * from users')
# result = cursor.fetchall()
# print(result)

# 添加
# cursor = session.execute('insert into users(name) values(:value)',params={"value":'wupeiqi'})
# session.commit()
# print(cursor.lastrowid)

session.close()

