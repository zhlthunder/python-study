#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from sqlalchemy import Table, Column, Integer, ForeignKey,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
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
    group_id=Column(Integer,ForeignKey('group.id'))  #映射父亲的某个字段，创建一个列名
    group=relationship("Group")  #重要，这里不是创建一个列名，而只是通过relationship把group类内嵌到host类中，这样就可以通过h1.group.name 来直接调用Group类中字段了

class Group(Base):
    __tablename__='group'
    id = Column(Integer,primary_key=True)
    name=Column(String(64),unique=True,nullable=False)


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
    # h1 = Host(hostname='localhost',ip_addr='127.0.0.1',group_id=g3.id)
    # session.add(h1)
    # session.commit()

    # 执行查询操作
    h1=session.query(Host).filter(Host.hostname=='localhost').first()
    print("h1:",h1.group_id)  #如果没有定义relationship,此时通过host的 group_id字段来查询
    print("h1:",h1.group.id) #如果定义了relationship，就可以直接调用Group类下面的字段

