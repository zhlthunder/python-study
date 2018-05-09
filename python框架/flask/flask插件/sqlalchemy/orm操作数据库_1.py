#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from s2_orm import Users

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/mydb", max_overflow=0, pool_size=5) #step1
connection = sessionmaker(bind=engine) #step2

# 每次执行数据库操作时，都需要创建一个session
conn = connection()

# ############# 执行ORM操作 #############
obj1 = Users(name="thunder")
conn.add(obj1)
obj2 = Users(name="tom")
conn.add(obj2)

# 提交事务
conn.commit()
# 关闭session
conn.close()