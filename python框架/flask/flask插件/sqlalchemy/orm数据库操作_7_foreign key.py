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
from models import Users, Hobby, Person

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/zhl", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)
session = Session()
# 添加

# session.add_all([
#     Hobby(caption='basketball'),
#     Hobby(caption='pingpang'),
#     Person(name='zhangsan', hobby_id=1),
#     Person(name='lisi', hobby_id=2),
# ])

# person = Person(name='张九', hobby=Hobby(caption='姑娘')) ##创建一个person ,一个hobby,并建立两者的关联
# session.add(person)

# hb = Hobby(caption='人妖')  ##创建一条hobby记录
# hb.pers = [Person(name='文飞'), Person(name='博雅')]  ##创建两条person记录，它们的foreign key自动关联到新创建的hobby上
# session.add(hb)

# session.commit()


# 使用relationship正向查询

# v = session.query(Person).first()
# print(v.name)
# print(v.hobby.caption)


# 使用relationship反向查询

v = session.query(Hobby).first()
print(v.caption)
print(v.pers)


session.close()
