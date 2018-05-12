#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
生成依赖文件：
    pipreqs ./

"""
from sansa import create_app

app = create_app()  ##使用flask的推荐用法

if __name__ == '__main__':
    app.run()

#测试访问方法： http://127.0.0.1:5000/login
##注意不是http://127.0.0.1:5000/login/