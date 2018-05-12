#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
生成依赖文件：
    pipreqs ./

"""
from sansa import create_app,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand  ##migrate 配置1

app = create_app()  ##使用flask的推荐用法
manager=Manager(app)  ##用于对app进行管理

migrate=Migrate(app,db)##migrate 配置2
manager.add_command('db',MigrateCommand)  ##migrate 配置3
#经过上面migrate的三个配置后，在终端下就可以执行如下的命令了：
"""
数据库迁移命名：
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
"""


@manager.command
def custom(arg):
    """
    自定义命令
    python manage.py custom 123
    :param arg:
    :return:
    """
    print(arg)

@manager.option('-n','--name',dest='name')
@manager.option('-u','--url',dest='url')
def cmd(name,url):
    """
    自定义命令
    执行：python manage.py cmd -n thunder -u http://www.zhlthunder.com
    :param name:
    :param url:
    :return:
    """
    print(name,url)

if __name__ == '__main__':
    manager.run()

#运行程序时： python manage.py runserver

