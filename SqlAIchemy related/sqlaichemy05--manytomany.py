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

#注意，此处创建表的方法不是用类的方法,且一个表里设置了两个主键 ，
# 主键的定义，非空且唯一，因为任意一条记录中，如果host_id或group_id为空的话，这条记录就没有存在的意义了
#且要在最开始定义
Host2Group=Table('host_2_group',Base.metadata,
                 Column('host_id',ForeignKey('host.id'),primary_key=True),
                 Column('group_id',ForeignKey('group.id'),primary_key=True),
                 )

class Host(Base):
    __tablename__ = 'host'    #表名
    id = Column(Integer,primary_key=True,autoincrement=True)  #表的列名
    hostname = Column(String(64),unique=True,nullable=False)  #表的列名
    ip_addr = Column(String(128),unique=True,nullable=False)  #表的列名
    port = Column(Integer,default=22)   #表的列名
    groups=relationship('Group',secondary=Host2Group,backref='host_list')
    # secondary: 指定中间表的实例
    #backref:定义group表反向调用host时使用的字段

    def __repr__(self):
        # return self.hostname
        return "<id=%s,hostname=%s,ip_addr=%s>"%(self.id,self.hostname,self.ip_addr)


class Group(Base):
    __tablename__='group'
    id = Column(Integer,primary_key=True)
    name=Column(String(64),unique=True,nullable=False)

    def __repr__(self):
        # return self.hostname
        return "<id=%s,name=%s"%(self.id,self.name)

Base.metadata.create_all(engine) #创建所有表结构

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    session = SessionCls()  #创建连接的实例

    ##为组添加记录
    # g1=Group(name='g1')
    # g2=Group(name='g2')
    # g3=Group(name='g3')
    # g4=Group(name='g4')
    # session.add_all([g1,g2,g3,g4])
    # session.commit()

    ##为主机添加记录
    # h1 = Host(hostname='h1',ip_addr='127.0.0.1')
    # h2 = Host(hostname='h2',ip_addr='111.1.1.1',port=10000)
    # h3 = Host(hostname='centos',ip_addr='10.1.1.1',port=10000)
    # session.add_all([h1,h2,h3])
    # session.commit()

    #为第三张表添加记录
    # groups=session.query(Group).all()
    # h1=session.query(Host).filter(Host.hostname=='h1').first()
    # h1.groups=groups
    # h2=session.query(Host).filter(Host.hostname=='h2').first()
    # h2.groups=groups[1:-1]
    # session.commit()

    #为第三张表添加记录任意删除一条记录
    # h1=session.query(Host).filter(Host.hostname=='h1').first()
    # h1.groups.pop()
    # session.commit()

    #关联查询
    #通过主机查询它属于哪些组
    # h2=session.query(Host).filter(Host.hostname=='h2').first()
    # print("-->",h2.groups)

    g1=session.query(Group).filter(Group.name=='g1').first()
    g2=session.query(Group).filter(Group.name=='g2').first()
    print("--->",g1.host_list)
    print("--->",g2.host_list)


# 总结：
# 1.先创建一个中间表，table返回的是一个表的实例对象；
#2.创建两个表；
#3.增加组记录，主机记录；