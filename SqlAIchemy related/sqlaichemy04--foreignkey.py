#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from sqlalchemy import Table, Column, Integer, ForeignKey,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,func
from  sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base() #生成一个SqlORM 基类，所有的子类都继承这个基类，类似于之前的metadata父类一样

engine = create_engine("mysql+mysqldb://root:123456@127.0.0.1:3306/mydb",echo=True)

#要求：一个组包含多个主机，但一个主机只可以属于一个组
#说明，对于host和group两个表，为多个host对应一个group,即多对一的关系，即外键要定义在host类中，而不可以定义在group;
#如果定义在group中，相当于group的一条记录中要写入多条主机，是一对多的关系，这种方法是不对的；
#目前实行的定义类型如下：
#1. 多对一   使用foreign key来实现，且foreign key定义在"多"的表中；
#2. 多对多， 使用manytomany 来实现，
# 一对多的模型没有实现的实例
class Host(Base):
    __tablename__ = 'hosts'    #表名
    id = Column(Integer,primary_key=True,autoincrement=True)  #表的列名
    hostname = Column(String(64),unique=True,nullable=False)  #表的列名
    ip_addr = Column(String(128),unique=True,nullable=False)  #表的列名
    port = Column(Integer,default=22)   #表的列名
    group_id=Column(Integer,ForeignKey('group.id'))  #映射父亲的某个字段，创建一个新的列名

    # group=relationship("Group")
    #单向relationship:重要，这里不是创建一个列名，而只是通过relationship把group类内嵌到host类中，这样就可以通过h1.group.name来直接调用Group类中字段了
    group=relationship("Group",backref='host_list') #双向relationship,此处的host_list是自己定义的，是通过Group调用的字段

class Group(Base):
    __tablename__='group'
    id = Column(Integer,primary_key=True)
    name=Column(String(64),unique=True,nullable=False)
    # hosts=relationship("Host") #单向relationship内嵌


Base.metadata.create_all(engine) #创建所有表结构


if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    session = SessionCls()  #创建连接的实例
    # 先为group和host增加记录
    # g1=Group(name='g1')
    # g2=Group(name='g2')
    # g3=Group(name='g3')
    # session.add_all([g1,g2,g3])

    # g3=session.query(Group).filter(Group.name=='g3').first()
    # g2=session.query(Group).filter(Group.name=='g2').first()
    # g1=session.query(Group).filter(Group.name=='g1').first()
    # h1 = Host(hostname='localhost',ip_addr='127.0.0.1',group_id=g3.id)
    # h2 = Host(hostname='ubuntu',ip_addr='111.1.1.1',group_id=g2.id)
    # h3 = Host(hostname='centos',ip_addr='10.1.1.1',group_id=g1.id)
    # session.add(h1)
    # session.add(h2)
    # session.add(h3)
    # session.commit()

    # 执行查询操作
    # h1=session.query(Host).filter(Host.hostname=='localhost').first()
    # g3=session.query(Group).filter(Group.name=='g3').first()
    # print("h1:",h1.group_id)  #如果没有定义relationship,此时通过host自己的 group_id字段来查询
    # print("h1-->:",h1.group.id) #因为Host类下定义了relationship到Group，就可以直接调用Group类下面的字段
    # print("g-->:",g3.hosts)#因为Group类下定义了relationship到Host，就可以直接调用Host类下面的字段
    # print("g-->:",g3.host_list)


    ##执行join关联查询的方法，类似下面原生sql join类似的功能
    # objs=session.query(Host).join(Host.group).all()  #这个命令，相当于inner join，返回3条记录，
    #注意理解此处的语法， 查询Host表，并关联查询Group表（通过Host.group映射的）,也可以直接用join(Group)来关联Group表；
    # objs=session.query(Host).join(Group).all()
    # print("-->:",objs)

    #适用group_by，进行分组聚合
    ##对一张表进行分类聚合
    # objj=session.query(Group,func.count(Group.name)).group_by(Group.name).all()
    ##对两张表进行join后进行分类聚合
    #直接使用下面的这条命令的all()返回结果时会报错，推测和sqlaichemy无关，将all() 修改为filter（Group.name）就没有报错了，
    # 使用all()报错的问题，待后续继续排查
    # objj=session.query(Host,func.count(Group.name)).join(Host.group).group_by(Group.name).all()
    objj=session.query(Host,func.count(Group.name)).join(Host.group).group_by(Group.name).filter(Group.name)
    print("-->:",objj)




##原生sql join查询
# 比如有下面两张表，
# mysql> select * from hosts;
# +----+-----------+-----------+------+----------+
# | id | hostname  | ip_addr   | port | group_id |
# +----+-----------+-----------+------+----------+
# |  1 | localhost | 127.0.0.1 |   22 |        3 |
# |  2 | ubuntu    | 111.1.1.1 |   22 |        2 |
# |  3 | centos    | 10.1.1.1  |   22 |        1 |
# |  5 | test      | 1.1.1.1   | NULL |     NULL |
# +----+-----------+-----------+------+----------+
# 4 rows in set (0.00 sec)
#
# mysql> select * from mydb.group;
# +----+------+
# | id | name |
# +----+------+
# |  1 | g1   |
# |  2 | g2   |
# |  3 | g3   |
# |  4 | g4   |
# +----+------+
# 4 rows in set (0.00 sec)

#执行join查询命令如下：
    #inner join
# mysql> select * from hosts inner join mydb.group  on hosts.group_id=mydb.group.id;
# +----+-----------+-----------+------+----------+----+------+
# | id | hostname  | ip_addr   | port | group_id | id | name |
# +----+-----------+-----------+------+----------+----+------+
# |  1 | localhost | 127.0.0.1 |   22 |        3 |  3 | g3   |
# |  2 | ubuntu    | 111.1.1.1 |   22 |        2 |  2 | g2   |
# |  3 | centos    | 10.1.1.1  |   22 |        1 |  1 | g1   |
# +----+-----------+-----------+------+----------+----+------+
# 3 rows in set (0.00 sec)


#left join
# mysql> select * from hosts left join mydb.group  on hosts.group_id=mydb.group.id;
# +----+-----------+-----------+------+----------+------+------+
# | id | hostname  | ip_addr   | port | group_id | id   | name |
# +----+-----------+-----------+------+----------+------+------+
# |  1 | localhost | 127.0.0.1 |   22 |        3 |    3 | g3   |
# |  2 | ubuntu    | 111.1.1.1 |   22 |        2 |    2 | g2   |
# |  3 | centos    | 10.1.1.1  |   22 |        1 |    1 | g1   |
# |  5 | test      | 1.1.1.1   | NULL |     NULL | NULL | NULL |
# +----+-----------+-----------+------+----------+------+------+
# 4 rows in set (0.00 sec)
#
# mysql>


#right join
# mysql> select * from hosts right join mydb.group  on hosts.group_id=mydb.group.id;
# +------+-----------+-----------+------+----------+----+------+
# | id   | hostname  | ip_addr   | port | group_id | id | name |
# +------+-----------+-----------+------+----------+----+------+
# |    1 | localhost | 127.0.0.1 |   22 |        3 |  3 | g3   |
# |    2 | ubuntu    | 111.1.1.1 |   22 |        2 |  2 | g2   |
# |    3 | centos    | 10.1.1.1  |   22 |        1 |  1 | g1   |
# | NULL | NULL      | NULL      | NULL |     NULL |  4 | g4   |
# +------+-----------+-----------+------+----------+----+------+
# 4 rows in set (0.00 sec)
#
# mysql>