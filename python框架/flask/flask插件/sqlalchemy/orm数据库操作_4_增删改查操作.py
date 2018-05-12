#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 基于scoped_session实现线程安全

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from models import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.sql import text


#1.创建连接池
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/zhl", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

##2.从连接池中获取数据库连接
session = scoped_session(Session)

##3.执行ORM操作
#####################增加#####################
# session.add(Users(name="jack3",email="jack3@163.com"))   ##单个增加
#
# session.add_all([                                           ##批量增加
#     Users(name="jack4",email="jack4@163.com"),
#     Users(name="jack5",email="jack5@163.com"),
# ])   ##单个增加
# session.commit()

################### 查#####################
# user_list=session.query(Users).all()
# user_list=session.query(Users).filter(Users.id>4)
# for row in user_list:
#     print(row.id)
#     print(row.name)
#     print(row.email)
#     print(row.ctime)

# r2 = session.query(Users.name, Users.age).all()
# print(r2)

# r2 = session.query(Users.name.label("xx"), Users.age).all()  ##Users.name.label("xx") 相当于把name字段重命名为xx
# print(r2)
# for item in r2:
#     print(item.xx)
#     # print(item.name)  #打印时提示：'result' object has no attribute 'name'，因为已经重命名为xx
#     print(item.age)

#使用filter时，括号里面是表达式，为字段名
#使用filter_by时，括号里面是参数
# r3 = session.query(Users).filter(Users.name == "tony").all()
# print(r3)
# for i in r3:
#     print(i.email)

##和上面的例子完成到的功能完全一样
# r4 = session.query(Users).filter_by(name='tony').all()
# print(r4)
# for i in r4:
#     print(i.email)


# r5 = session.query(Users).filter_by(name='alex').first()  ##取第一个值

# r6 = session.query(Users).filter(text("id<:value and name=:name")).params(value=2, name='tony').order_by(Users.id).all()
# print(r6)
# for i in r6:
#     print(i.name)

# r7 = session.query(Users).from_statement(text("SELECT * FROM users where name=:name")).params(name='jack_sb').all()
# print(r7)
# for i in r7:
#     print(i.name)

##################删除########################
# session.query(Users).filter(Users.id>4).delete()
# session.commit()

##################改########################
# session.query(Users).filter(Users.id==1).update({'name':'tony'})
# session.commit()
# session.query(Users).filter(Users.id >1).update({Users.name: Users.name + "_sb"}, synchronize_session=False)  ##对于字符串的修改用这个：jack==>jack_sb
# session.commit()
# session.query(Users).filter(Users.id > 2).update({"age": Users.age + 2}, synchronize_session="evaluate")  #如果是数字，用这个格式
# session.commit()
##4.关闭数据库连接（实际上是将连接放回连接池，并没有关闭）
session.close()

##备注：如果进行insert操作后，没有commit的情况下，ID正常增长，虽然数据中的数据没有写入