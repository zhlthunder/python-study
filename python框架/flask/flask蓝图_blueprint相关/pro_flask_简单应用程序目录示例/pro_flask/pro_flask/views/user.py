#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint

user = Blueprint('user', __name__)

@user.route('/user', methods=['GET', "POST"])
def blue_user():
    return "it is blue_user"