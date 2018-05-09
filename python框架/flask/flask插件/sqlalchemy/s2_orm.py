#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 创建单表
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

Base = declarative_base()  #step1

class Users(Base): #step2
    __tablename__ = 'users' #表名
    id = Column(Integer, primary_key=True)  #字段，主键
    name = Column(String(32), index=True, nullable=False)#字段
    email = Column(String(32), unique=True)  ##唯一索引
    ctime = Column(DateTime, default=datetime.datetime.now)  #创建时间，有个默认值 @@如果使用了括号，datetime.datetime.now（）是有问题，因为使用datetime.datetime.now（）获取了值
    extra = Column(Text, nullable=True)

    __table_args__ = (##设定当前表的一些其它信息
        # UniqueConstraint('id', 'name', name='uix_id_name'),  ##联合唯一索引
        # Index('ix_id_name', 'name', 'email'), ##联合索引
    )


def init_db():
    """
    根据类创建数据库表
    :return:
    """
    #step 3
    engine = create_engine(
        "mysql+pymysql://root:123456@127.0.0.1:3306/mydb?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.create_all(engine) #step 4


def drop_db():
    """
    根据类删除数据库表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:123456@127.0.0.1:3306/mydb?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    # drop_db()
    init_db()


##重要，只支持创建表和删除表，无法修改表；
#即修改表之后，无法更新到数据库中。如果要修改，可以去数据库中自己修改，然后在类中添加一个字段，保持一致即可；
