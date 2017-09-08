#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
# 堡垒机实例
# http://www.cnblogs.com/alex3714/articles/5286889.html

from sqlalchemy import Table, Column, Integer, ForeignKey,create_engine,UniqueConstraint,\
    DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,func
from  sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy_utils import ChoiceType,PasswordType

Base = declarative_base() #生成一个SqlORM 基类，所有的子类都继承这个基类，类似于之前的metadata父类一样




HostUser2Group = Table('hostuser_2_group',Base.metadata,
    Column('hostuser_id',ForeignKey('host_user.id'),primary_key=True),
    Column('group_id',ForeignKey('group.id'),primary_key=True),
)

UserProfile2Group = Table('userprofile_2_group',Base.metadata,
    Column('userprofile_id',ForeignKey('user_profile.id'),primary_key=True),
    Column('group_id',ForeignKey('group.id'),primary_key=True),
)

UserProfile2HostUser = Table('userprofile_2_hostuser',Base.metadata,
    Column('userprofile_id',ForeignKey('user_profile.id'),primary_key=True),
    Column('hostuser_id',ForeignKey('host_user.id'),primary_key=True),
)

class Host(Base):
    __tablename__='host'
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
    __tablename__='user_profile'
    id = Column(Integer,primary_key=True)
    username=Column(String(64),unique=True,nullable=False)
    password=Column(String(64),nullable=False)

    host_list=relationship('HostUser',
                        secondary=UserProfile2HostUser,
                        backref='userprofiles')

    groups=relationship('Group',
                        secondary=UserProfile2Group,
                        backref='userprofiles')

    def __repr__(self):
        # return self.hostname
        return "<id=%s,name=%s>"%(self.id,self.username)

class HostUser(Base):
    __tablename__='host_user'
    id = Column(Integer,primary_key=True)
    host_id=Column(Integer,ForeignKey('host.id'))
    AuthTypes = [
        (u'ssh-passwd',u'SSH/Password'),
        (u'ssh-key',u'SSH/KEY'),
    ]
    auth_type = Column(ChoiceType(AuthTypes))
    username=Column(String(64),unique=True,nullable=False)
    password=Column(String(64))
    groups=relationship('Group',
                        secondary=HostUser2Group,
                        backref='host_list')  # backref 是从组里反向调用使用的字段

    ##下面是联合唯一，
    # 应用的场景，在这个表里，默认主机+用户名  是唯一的，即不同机器的root密码不共用，是不同的。但同一台机器只能有一个root密码，所以主机+root必须是唯一的
    #如何采用共享的用户名，就需要为  主机--用户  之间建立多对多的关系
    __table_args__ = (UniqueConstraint('host_id', 'username', name='_host_username_uc'),)

    def __repr__(self):
        # return self.hostname
        return "<id=%s,name=%s>"%(self.id,self.username)


class AuditLog(Base):
    __tablename__ = 'audit_log'
    id = Column(Integer,primary_key=True)
    userprofile_id = Column(Integer,ForeignKey('user_profile.id'))
    hostuser_id = Column(Integer,ForeignKey('host_user.id'))

    ##这种方式实际执行时报错，采用ChoiceType+元祖的方式进行
    action_choices = [
        (0,'CMD'),
        (1,'Login'),
        (2,'Logout'),
        (3,'GetFile'),
        (4,'SendFile'),
        (5,'Exception'),
    ]
    action_choices2 = [
        (u'cmd',u'CMD'),   #cmd是存到数据库中的， CMD是显示给用户的
        (u'login',u'Login'),
        (u'logout',u'Logout'),
        #(3,'GetFile'),
        #(4,'SendFile'),
        #(5,'Exception'),
    ]
    action_type = Column(ChoiceType(action_choices2))
    #action_type = Column(String(64))
    cmd = Column(String(255))  ##存储操作的方式
    date = Column(DateTime)

    user_profile = relationship("UserProfile")




engine = create_engine("mysql+mysqldb://root:123456@127.0.0.1:3306/test",echo=True)

Base.metadata.create_all(engine)

##此作业以成功创建完表就结束了，后续酌情进行完善继续做；