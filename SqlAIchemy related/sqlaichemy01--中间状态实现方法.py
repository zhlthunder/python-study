#!/usr/bin/env python
# -*- coding:utf-8 -*-

# type 1
# 使用 Engine/ConnectionPooling/Dialect 进行数据库操作，
# Engine使用ConnectionPooling连接数据库，然后再通过Dialect执行SQL语句。

#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 因为我没有创建对象的数据表，所以下面的代码无法执行，先不执行

# from sqlalchemy import create_engine
#
# engine = create_engine("mysql+mysqldb://root:123456@127.0.0.1:3306/mydb", max_overflow=5)
#
# engine.execute(
#     "INSERT INTO ts_test (a, b) VALUES ('2', 'v1')"
# )
#
# engine.execute(
#      "INSERT INTO ts_test (a, b) VALUES (%s, %s)",
#     ((555, "v1"),(666, "v1"),)
# )
# engine.execute(
#     "INSERT INTO ts_test (a, b) VALUES (%(id)s, %(name)s)",
#     id=999, name="v1"
# )
#
# result = engine.execute('select * from ts_test')
# result.fetchall()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# type 2:
# 使用 Schema Type/SQL Expression Language/Engine/ConnectionPooling/Dialect 进行数据库操作。
# Engine使用Schema Type创建一个特定的结构对象，之后通过SQL Expression Language将该对象转换成SQL语句，
# 然后通过 ConnectionPooling 连接数据库，再然后通过 Dialect 执行SQL，并获取结果。


# from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
#
# metadata = MetaData()
#获取一个metadata的对象，可以理解为实例化了一个表格的父类，之后创建的所有表格都要继承它的特性；

 ##下面就完成类似继承的功能，即表格user继承于它的父类  metadata
 #表名，父类
 #第一列：名称，类型，主键声明
  #第二列：名称，类型
# user = Table('user', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String(20)),
# )
#
# color = Table('color', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String(20)),
# )
# engine = create_engine("mysql+mysqldb://root:123456@localhost:3306/mydb", max_overflow=5)

# metadata.create_all(engine)
# 即使这个命令不注释，已经存在的表，它不会重复去创建的

# 输出有如下的warning,推测和字符格式有关，虽然有warning,但表格已经创建成功了
# C:\Python27\python2.exe "C:/Users/lin/PycharmProjects/python_study_1s/python_study/git-zhl/python-study/SqlAIchemy related/sqlaichemy01.py"
# C:\Python27\lib\site-packages\sqlalchemy\engine\default.py:470: Warning: Incorrect string value: '\xD6\xD0\xB9\xFA\xB1\xEA...' for column 'VARIABLE_VALUE' at row 480
#   cursor.execute(statement, parameters)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



# type3:
# 数据库的增删改查
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey,select

metadata = MetaData()
user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)

color = Table('color', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)
engine = create_engine("mysql+mysqldb://root:123456@localhost:3306/mydb", max_overflow=5)

 #获取数据表操作的游标
conn = engine.connect()

#为数据表增加记录方法1：
# 创建SQL语句，INSERT INTO "user" (id, name) VALUES (:id, :name)
# conn.execute(user.insert(),{'id':7,'name':'seven'})
# conn.close()



#为数据表增加记录方法2：
# sql = user.insert().values(id=123, name='wu')
# conn.execute(sql)
# conn.close()

# sql = color.insert().values(id=222, name='alex')
# conn.execute(sql)
# conn.close()


#删除数据表中的记录的方法：
# sql = user.delete().where(user.c.id > 10)
# conn.execute(sql)
# conn.close()



#修改数据表中记录的方法：
# sql = user.update().where(user.c.name == 'seven').values(name='sseven')
# sql = user.update().where(user.c.name == 'sseven').values(name='seven',id='100')
# conn.execute(sql)


#查询数据表中记录的方法
#type 1:查询表中所有记录的所有列
# sql = select([user, ])
# result = conn.execute(sql)
# print result.fetchall()

#type 2:查询表中所有记录的id列
# sql = select([user.c.id, ])

#type 3: 输出两张表中id相同时对应的name；
# sql = select([user.c.name, color.c.name]).where(user.c.id==color.c.id)

#type4:按用户名排序后输出所有的用户名
# sql = select([user.c.name]).order_by(user.c.name)

#type5:按用户名排序后输出所有记录的所有列
sql = select([user]).order_by(user.c.name)

result = conn.execute(sql)
print result.fetchall()
# conn.close()

