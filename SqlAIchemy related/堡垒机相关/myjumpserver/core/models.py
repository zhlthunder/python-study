#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from sqlalchemy import Table, Column, Integer, ForeignKey,create_engine,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,func
from  sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base() #生成一个SqlORM 基类，所有的子类都继承这个基类，类似于之前的metadata父类一样

engine = create_engine("mysql+mysqldb://root:123456@127.0.0.1:3306/mydb",echo=True)



class Host(Base):
    __table__='host'
    id = Column(Integer,primary_key=True,autoincrement=True)  #表的列名
    hostname = Column(String(64),unique=True,nullable=False)  #表的列名
    ip_addr = Column(String(128),unique=True,nullable=False)  #表的列名
    port = Column(Integer,default=22)   #表的列名
    def __repr__(self):
    # return self.hostname
        return "<id=%s,hostname=%s,ip_addr=%s>"%(self.id,self.hostname,self.ip_addr)

class Group(Base):
    __tablename__= 'group'
    id = Column(Integer,primary_key=True)
    name=Column(String(64),unique=True,nullable=False)

    def __repr__(self):
        # return self.hostname
        return "<id=%s,name=%s>"%(self.id,self.name)

class UserProfile(Base):
    __table__='user_profile'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String(64),unique=True,nullable=False)
    password=Column(String(64),nullable=False)
    def __repr__(self):
        # return self.hostname
        return "<id=%s,name=%s>"%(self.id,self.username)

class HostUser(Base):
    __table__='host_user'
    id = Column(Integer,primary_key=True)
    host_id=Column(Integer,ForeignKey('host.id'))
    username=Column(String(64),unique=True,nullable=False)
    password=Column(String(64),nullable=False)
    __table_args__ = (UniqueConstraint('host_id', 'username', name='_host_username_uc'),)
    def __repr__(self):
        # return self.hostname
        return "<id=%s,name=%s>"%(self.id,self.username)