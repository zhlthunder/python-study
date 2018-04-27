#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 路径变量
# 如果希望获取/article/1这样的路径参数，就需要使用路径变量。路径变量的语法是/path/<converter:varname>。
# 在路径变量前还可以使用可选的转换器，有以下几种转换器。

# 转换器	    作用
# string	默认选项，接受除了斜杠之外的字符串
# int	    接受整数
# float	    接受浮点数
# path	    和string类似，不过可以接受带斜杠的字符串
# any	    匹配任何一种转换器
# uuid	    接受UUID字符串




from flask import Flask

app = Flask(__name__)
app.config.update(DEBUG=True)  # 参数形式配置

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)

##测试方法，通过浏览器访问：localhost:8088
##支持两个url: http://localhost:8088/hello ,  http://localhost:8088