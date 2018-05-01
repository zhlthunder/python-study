#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint

blog = Blueprint('blog', __name__)

@blog.route('/blog', methods=['GET', "POST"])
def blue_blog():
    return "it is blue_blog"
