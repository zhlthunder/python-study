#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()   ##必须先执行这个，再执行下面这句，因为models中调用了db

from .models import *
from .views import account

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig') #读取配置文件

    # 将db注册到app中
    db.init_app(app)  ##应用配置文件中的配置,数据库的配置文件在这边

    # 注册蓝图
    app.register_blueprint(account.account)


    return app