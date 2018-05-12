#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 基于scoped_session实现线程安全

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from models import *

# scoped_session类说明：
# class scoped_session(object):
#     def __init__(self, session_factory, scopefunc=None):
#         self.session_factory = session_factory
#
#         if scopefunc:
#             self.registry = ScopedRegistry(session_factory, scopefunc)
#         else:
                #self.registry 中封装了两个值： 原来的session类， threading.local()
#             self.registry = ThreadLocalRegistry(session_factory)

# class ThreadLocalRegistry(ScopedRegistry):
#
#     def __init__(self, createfunc):
#         self.createfunc = createfunc
#         self.registry = threading.local()

#1.创建连接池
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/zhl", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

##2.从连接池中获取数据库连接
session = scoped_session(Session)  ##执行这个实例化之后： self.registry 中封装了两个值： 原来的session类， threading.local()
##@@@@@@使用scoped_session的作用是:可以为每个线程创建一个session对象，且线程之间是相互隔离的，即如果需要修改某个
# session的话就可以做到很好的隔离, 推荐使用这种方式

##3.执行ORM操作
obj1 = Users(name="jack2",email="jack2@163.com")
session.add(obj1) ##本质是执行do函数，
session.commit()

##4.关闭数据库连接（实际上是将连接放回连接池，并没有关闭）
session.close()


# remark:
#查看源码时，发现类scoped_session中没有定义比如add,commit等方法，但可以调用，原因如下：
# for meth in Session.public_methods:
#     setattr(scoped_session, meth, instrument(meth))

# Session.public_methods为：
#     public_methods = (
#         '__contains__', '__iter__', 'add', 'add_all', 'begin', 'begin_nested',
#         'close', 'commit', 'connection', 'delete', 'execute', 'expire',
#         'expire_all', 'expunge', 'expunge_all', 'flush', 'get_bind',
#         'is_modified', 'bulk_save_objects', 'bulk_insert_mappings',
#         'bulk_update_mappings',
#         'merge', 'query', 'refresh', 'rollback',
#         'scalar')

# instrument(meth) 为：
# def instrument(name):
#     def do(self, *args, **kwargs):  ##获取了原来的session对象，并把对象放在threading.local中。就是在执行ThreadLocalRegistry的__call__方法，如下：
#         return getattr(self.registry(), name)(*args, **kwargs)
#
#     def __call__(self):
#         try:
#             return self.registry.value
#         except AttributeError:
#             val = self.registry.value = self.createfunc()
#             return val