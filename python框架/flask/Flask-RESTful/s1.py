#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
#refer:https://blog.csdn.net/dream_flying_bj/article/details/61198475
#安装pip3 install flask-restful

##使用参考： pip3 install flask-restful

from flask import Flask, jsonify
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

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)