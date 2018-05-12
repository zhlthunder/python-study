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

######条件类#######################
#使用filter时，括号里面接收的是表达式
#使用filter_by时，括号里面接收的是参数
# r3 = session.query(Users).filter(Users.name == "tony").all()
# print(r3)
# for i in r3:
#     print(i.email)

# ret = session.query(Users).filter(Users.id > 1, Users.name == 'jack3_sb').all()  ##两个条件是and关系
# ret = session.query(Users).filter(Users.id.between(1, 3), Users.name == 'jack2_sb').all()
# ret = session.query(Users).filter(Users.id.in_([1,3,4])).all()
# ret = session.query(Users).filter(~Users.id.in_([1,3,4])).all()  #取非
# ret = session.query(Users).filter(Users.id.in_(session.query(Users.id).filter_by(age=18))).all()

from sqlalchemy import and_, or_
# ret = session.query(Users).filter(and_(Users.id > 3, Users.name == 'jack2_sb')).all()
# ret = session.query(Users).filter(or_(Users.id < 2, Users.name == 'jack2_sb')).all()
# ret = session.query(Users).filter(
#     or_(
#         Users.id < 2,
#         and_(Users.name == 'jack3_sb', Users.id > 3),
#         Users.extra != ""
#     )).all()


###### 通配符
# ret = session.query(Users).filter(Users.name.like('j%')).all()  #  %代表任意多个字符
# ret = session.query(Users).filter(~Users.name.like('j%')).all()  #取非

# 限制
# ret = session.query(Users)[1:2]  #[1,2), 不包括2，请注意

# 排序
# ret = session.query(Users).order_by(Users.name.desc()).all()  ##从大到小
# ret = session.query(Users).order_by(Users.name.asc()).all()  #从小到大
# ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()  ##优先按照name从大到下排，如果重名再按照id从小到大排


# 分组
from sqlalchemy.sql import func

# ret = session.query(Users).group_by(Users.name).all()  ##分组
# ret = session.query(
#     func.max(Users.id),
#     func.sum(Users.id),
#     func.min(Users.id)).group_by(Users.name).all()  ##先分组，分组之后每一个组中再取最大id,最小id， id之和
#
# ret = session.query(
#     func.max(Users.id),
#     func.sum(Users.id),
#     func.min(Users.id)).group_by(Users.name).having(func.min(Users.id) >2).all() #对group_by的条件再做筛选使用having

# print(ret)
# for i in ret:
#     print(i.name)


# 连表
# ret = session.query(Users, Favor).filter(Users.id == Favor.nid).all()
# ret = session.query(Person).join(Favor).all()  ##inner join
# ret = session.query(Person).join(Favor, isouter=True).all()  ##person left join favor, 如果要实现right jion,只有变更一下顺序
# #上面的连表没有on参数，即在sqlalchemy中，执行jion是，如果有foreign key默认用foreign key的字段进行关联
                                                     # 如果没有foreign key，就不执行关

##重要，查看sqlalchemy语句对应的原生sql语句的方法如下： 不加 all(), 然后pirint(ret)
# ret = session.query(Person).join(Hobby, isouter=True)
# print(ret)
# 打印信息如下：
# SELECT person.nid AS person_nid, person.name AS person_name, person.hobby_id AS person_hobby_id
# FROM person LEFT OUTER JOIN hobby ON hobby.id = person.hobby_id

##自定义on的规则的方法：
# ret = session.query(Person).join(Hobby,Person.hobby_id==hobby.id isouter=True)


# 组合
# q1 = session.query(Users.name).filter(Users.id > 2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union(q2).all()
#
# q1 = session.query(Users.name).filter(Users.id > 2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union_all(q2).all()


session.close()

##备注：如果进行insert操作后，没有commit的情况下，ID正常增长，虽然数据中的数据没有写入