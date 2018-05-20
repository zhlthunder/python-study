#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
#refer:https://blog.csdn.net/dream_flying_bj/article/details/61198475
#安装pip3 install flask-restful

##使用参考： pip3 install flask-restful

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
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



def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': list(map(make_public_task, tasks))})



if __name__ == '__main__':
    app.run(debug=True)

##在python3下执行有点问题，可能和iteral有关，待继续确认