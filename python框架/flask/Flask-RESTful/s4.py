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


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if not len(list(task)):
        return "404"
    task = filter(lambda t: t['id'] == task_id, tasks)
    return jsonify({'task': task.__next__()})




@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


if __name__ == '__main__':
    app.run(debug=True)