#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
#refer:https://blog.csdn.net/dream_flying_bj/article/details/61198475
#安装pip3 install flask-restful

##使用参考： pip3 install flask-restful

#api 安全认证相关  pip3 install flask-httpauth


from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)