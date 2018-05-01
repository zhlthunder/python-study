#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask import request

account = Blueprint('account', __name__,url_prefix="/acc",template_folder='tpls')
#url_prefix="/acc"  用于对这个蓝图下面的所有URL 统一加个前缀； 即访问方式变更：/account--》/acc/account
##template_folder='tpls'  定义这个蓝图下专用的templates,以实现templates的分离，但有个优先级的问题，如果templates和tpls中都有相同的模块，优先寻找templates中的，




@account.route('/account', methods=['GET', "POST"])
def blue_account():
    return render_template('login_new.html')


@account.before_request
def process_request(*args,**kwargs):
    print("来了")
