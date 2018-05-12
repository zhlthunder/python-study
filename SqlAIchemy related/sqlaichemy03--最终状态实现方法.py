#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://root:123456@127.0.0.1:3306/mydb", max_overflow=5)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

# 寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
# Base.metadata.create_all(engine)  #创建所有表结构

##连接数据表，获取游标
Session = sessionmaker(bind=engine)
session = Session()


# ########## 增 ##########
# u = User(id=2, name='sb')
# session.add(u)
# session.add_all([
#     User(id=3, name='sb'),
#     User(id=4, name='sb')
# ])
# session.commit()

# ########## 删除 ##########
# session.query(User).filter(User.id > 2).delete()
# session.commit()

# ########## 修改 ##########
# session.query(User).filter(User.id > 2).update({User.name: 'jack'})
# session.commit()
# ########## 查 ##########
# ret = session.query(User).filter_by(name='sb').first()

# ret = session.query(User).filter_by(name='sb').all()
# print ret

# ret = session.query(User).filter(User.name.in_(['sb','bb'])).all()
# print ret

# ret = session.query(User.name.label('name_label')).all()  ##重命名 name --》 name_label
# print ret,type(ret)

# ret = session.query(User).order_by(User.id).all()
# print ret

# ret = session.query(User).order_by(User.id)[1:3]
# print ret
# session.commit()