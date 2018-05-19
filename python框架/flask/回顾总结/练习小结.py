#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask,render_template,request,redirect
app=Flask(__name__)

USERS={
    1:{"name":'jack',"age":23,"commit":"阿萨德发发士大夫士大夫的"},
    2:{"name":'tony',"age":24,"commit":"了健康快乐记录空间领口就可理解"},
    3:{"name":'jack',"age":14,"commit":"手动阀发的飞洒的发送到发送到"},
}

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html',user=USERS)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template("login.html")
    else:

        user=request.form.get('user')
        pwd=request.form.get('passwd')
        if user=='zhl' and pwd=='123':
            return redirect("/index")
        return render_template("login.html",err="用户名或密码错误")
if __name__ == '__main__':
    app.run(debug=True)