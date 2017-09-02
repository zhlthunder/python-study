#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


from sqlalchemy import create_engine,and_,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from  sqlalchemy.orm import sessionmaker

Base = declarative_base() #生成一个SqlORM 基类，所有的子类都继承这个基类，类似于之前的metadata父类一样


engine = create_engine("mysql+mysqldb://root:123456@127.0.0.1:3306/mydb",echo=True)
#echo=True,会打印操作信息
#echo=False,不会打印操作信息

 #创建一个表结构
class Host(Base):
    __tablename__ = 'hosts'    #表名
    id = Column(Integer,primary_key=True,autoincrement=True)  #表的列名
    hostname = Column(String(64),unique=True,nullable=False)  #表的列名
    ip_addr = Column(String(128),unique=True,nullable=False)  #表的列名
    port = Column(Integer,default=22)   #表的列名

Base.metadata.create_all(engine) #创建所有表结构

# 创建完表结构之后，下面来进行数据的增删改查等操作
# 首先要先建立数据库的连接关系（类似于获取光标的功能），然后再进行数据的操作
if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    session = SessionCls()  #创建连接的实例

    #增加数据记录的方法
    # h1 = Host(hostname='localhost',ip_addr='127.0.0.1')
    # h2 = Host(hostname='ubuntu',ip_addr='192.168.2.243',port=20000)
    # h3 = Host(hostname='ubuntu2',ip_addr='192.168.2.244',port=20000)

    #增加记录方法1
    # session.add(h3)
    #增加记录方法2
    # session.add_all([h1,h2])
    # h2.hostname = 'ubuntu_test' #只要没提交,此时修改也没问题
    # session.commit() #提交，只有执行提交后，才会真正去添加记录


    #修改数据记录的方法，先查询出来，然后再修改；
    # obj=session.query(Host).filter(Host.hostname=="localhost").first()  #注意，此处使用的是clssname，而不是table name; 支持first() last() all()等方法
    # print("--->:",obj)
    # obj.hostname="test server"
    # session.commit()


    # 删除数据记录的方法：
    # obj=session.query(Host).filter(Host.hostname=="test server").first()
    # session.delete(obj)
    # session.commit()

    ##查询数据记录的方法：
    #涉及的方法， like  and_ in_
    # objs=session.query(Host).filter(and_(Host.hostname.like("%test"),Host.port>4000)).all()
    # print(objs)

    res = session.query(Host).filter(Host.hostname.in_(['ubuntu2','ubuntu_test'])).all()
    print(res)
    # session.commit()

# 更多内容详见：
#
#     http://www.jianshu.com/p/e6bba189fcbd
#
#     http://docs.sqlalchemy.org/en/latest/core/expression_api.html
#
# 注：SQLAlchemy无法修改表结构，如果需要可以使用SQLAlchemy开发者开源的另外一个软件Alembic来完成。

