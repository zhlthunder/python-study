# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
# 导入django自带的认知模块，用于登录用户的账号认知
from django.contrib import auth
from models import *




def index(req):
    # return HttpResponse("ok");
    return render_to_response('index.html');


def login(req):
    # 打印前台通过post方法提交过来的所有信息
    # print req.POST;
    # 获取post提交信息中的用户名及密码
    username=req.POST.get('username');
    password=req.POST.get('password');
    # 调用django自带的认证模块，对输入的用户名及密码进行验证，如果认证成功，则返回登录的用户的信息使用（就相当于查询账户信息数据库进行确认）
    user=auth.authenticate(username=username,password=password);
    if user is not None:
        # 认知成功后进行用户的登录
        auth.login(req,user);
        # 此处使用重定向的方法转到另一个url;
        return HttpResponseRedirect("/dashboard/");

    else:
        # 如果用户名和密码认知错误，返回登陆错误的信息到前台
        return render_to_response('index.html',{'login_error':"Wrong userword or password!!"})

def logout(req):
    temp_user=req.user
    # 注销当前的登录的用户
    auth.logout(req);
    # return HttpResponse("User [%s] logout successfully"% temp_user);
    return HttpResponseRedirect("/");

def dashboard(req):
    return render_to_response('dashboard.html',{'user':req.user});

def host_manager(req):
    ip_list=IP.objects.all();
    print ip_list;
    return render_to_response('host_manager.html',{'user':req.user,'ip_list':ip_list});

def monitor(req):
    # 在前端页面显示字典列表
    name_dic={
        'name':'alex',
        'age':28,
        'sex':'M',
    }
    name_dicc={
        'alex':[29,'M','Engineer'],
        'tony':[39,'M','SecurityGuard'],
        'jack':[19,'F','Teacher'],
    }

    return render_to_response('monitor.html',{'user':req.user,'name_dic':name_dic,'name_dicc':name_dicc});


def asset(req):
    return render_to_response('asset.html',{'user':req.user});

