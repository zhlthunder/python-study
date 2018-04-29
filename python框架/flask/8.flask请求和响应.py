#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import make_response

app = Flask(__name__)


@app.route('/login.html', methods=['GET', "POST"])
def login():

    # 请求相关信息
    # request.method
    # request.args
    # request.form
    # request.values
    # request.cookies
    # request.headers
    # request.path
    # request.full_path
    # request.script_root
    # request.url
    # request.base_url
    # request.url_root
    # request.host_url
    # request.host
    # request.files
    # obj = request.files['the_file_name']
    # obj.save('/var/www/uploads/' + secure_filename(obj.filename))
     ##secure_filename 实际上是对文件名进行加密，以加密后字符串作为文件名，防止文件名重复

    # 响应相关信息
    # return "字符串"
    # return render_template('html模板路径',**{})
    # return redirect('/index.html')
    # return jsonify({'k1':'v1'})  ##返回json格式的数据给前端页面

    ##对响应进行二次加工， 比如设置cookie,设置响应头等等
    # response = make_response(render_template('index.html'))  ##返回模板文件时，先创建一个响应对象
    # response = make_response(“this is index page”) ##返回的是字符串时，先创建一个响应对象
    # response是flask.wrappers.Response类型  ##对象的类型
    # response.delete_cookie('key')  ##删除cookie
    # response.set_cookie('key', 'value') ##设置cookie
    # response.headers['X-Something'] = 'A value'  ##设置响应头
    # return response   ##返回响应的对象

    ##待继续研究flask 中响应的代码实现的原理的确认


    return "内容"

if __name__ == '__main__':
    app.run()

##备注：在flask中使用jsonify和json.dumps的区别
##https://blog.csdn.net/Duke_Huan_of_Qi/article/details/76064225