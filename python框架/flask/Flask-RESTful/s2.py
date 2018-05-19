#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
#refer:https://blog.csdn.net/dream_flying_bj/article/details/61198475
#安装pip3 install flask-restful

##使用参考： pip3 install flask-restful

##重要：判断一个迭代器是否为空,需要先转换为列表才可以 list(iteral)

from flask import Flask, jsonify
from flask import abort
from flask import make_response
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
    # if len(task) == 0:  ##for python2
    if len(list(task)) == 0:  ##for python3
        abort(404)
    task = filter(lambda t: t['id'] == task_id, tasks)  ##此处存在重复编码，实现方式待修改
    return jsonify({'task': task.__next__()})





if __name__ == '__main__':
    app.run(debug=True)