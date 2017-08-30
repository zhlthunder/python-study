#!/usr/bin/env python
# -*- coding:utf-8 -*-
  
from sqlalchemy import create_engine
  
  
# engine = ("sqlite:///C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\SqlAIchemy related\mysqlite.db", max_overflow=5)

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