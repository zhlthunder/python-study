#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#sample 1: 第一程序，默认模式
# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello Flask——zhl!'
#
# if __name__ == '__main__':
#     app.run()

##测试方法，通过浏览器访问：localhost:5000

##sample 2：修改IP及端口
# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello Flask——zhl!'
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8088)
##测试方法，通过浏览器访问：localhost:8088

##sample 3： Debug模式的开启
### 为什么需要开启DEBUG模式：
# 1. 如果开启了DEBUG模式，那么在代码中如果抛出了异常，在浏览器的页面中可以看到具体的错误信息，以及具体的错误代码位置。方便开发者调试。
# 2. 如果开启了DEBUG模式，那么以后在`Python`代码中修改了任何代码，只要按`ctrl+s`，`flask`就会自动的重新记载整个网站。不需要手动点击重新运行。
#
# ### 配置DEBUG模式的四种方式：
# 1. 在`app.run()`中传递一个参数`debug=True`就可以开启`DEBUG`模式。
# 2. 给`app.deubg=True`也可以开启`debug`模式。
# 3. 通过配置参数的形式设置DEBUG模式：`app.config.update(DEBUG=True)`。
# 4. 通过配置文件的形式设置DEBUG模式：`app.config.from_object(config)`。
#
# ### PIN码：
# 如果想要在网页上调试代码，那么应该输入`PIN`码。


from flask import Flask

app = Flask(__name__)
app.config.update(DEBUG=True)  # 参数形式配置
# print(isinstance(app.config, dict))  # True
# app.config.from_object(config)  # 加载配置文件，但需要安装模块后，执行import config才可以

@app.route('/')
def hello_world():
    return 'Hello World-----pppaap!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)

##进入debug模式，时候如果再次修改代码，会发现这次Flask会自动重启
# * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 112-845-219
#  * Running on http://0.0.0.0:8088/ (Press CTRL+C to quit)

