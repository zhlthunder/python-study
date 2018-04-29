#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##sample 1
from flask import Flask,render_template,request,redirect,session,url_for
app = Flask(__name__)
app.debug=True
app.secret_key = '123456'

USERS={
    1:{'name':'jack','age':18,'gender':'男','text':"简报的种类很多，从内容上讲，有综合性简报、典型经验性简报、动态性简报、反馈性简报和会议简报等等。无论是何种类型的简报，其写作方法基本相同，既可以采用新闻稿的写作方法"},
    2:{'name':'tony','age':28,'gender':'女','text':"各级金融部门每天都发生着许许多多的事情，对这些近来发生的金融事实，并非都能够编写成简报，需要严格筛选。在选择的标准上，从大的方面来讲要符合"},
    3:{'name':'jerry','age':28,'gender':'女','text':"反映问题的简报应当反映出问题的实际情况，分析问题产生的原因，提出解决问题的办法措施。只有如此，才能引起人们的注意，吸取教训，促进工作"}
}


def verify(func):
    def inner(*args,**kwargs):
        user=session.get('user_info')
        if not user:
            url=url_for('l1')
            return redirect(url)
            # return redirect("/login")
        func()
    return inner


@verify
@app.route('/detail/<int:nid>',methods=['GET'])
def detail(nid):
    info=USERS.get(nid)
    return render_template('detail.html',info=info)


@verify
@app.route('/index',methods=['GET'])
def index():
    #     url=url_for('l1')
    #     return redirect(url)
    return render_template('index.html',user_dict=USERS)



@app.route('/login',methods=['GET','POST'],endpoint='l1')
def login():
    if request.method=='GET':
        return render_template("login.html")
    else:
        # request.form  存放请求体中的数据
        # request.query_string 请求头中的数据
        user=request.form.get('user')
        pwd=request.form.get('pwd')
        if user=='thunder' and pwd=='123':
            session['user_info']=user
            return redirect("http://www.luffycity.com")
        return render_template("login.html",err="用户名或密码错误")


if __name__ == '__main__':
    app.run()
