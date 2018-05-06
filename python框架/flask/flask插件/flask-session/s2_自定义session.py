#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask,session
import json

app=Flask(__name__)
app.secret_key='asdfad'


#不使用源码中创建的session,此处通过自定义创建一个字典来实现
class Mysessioninterface(object):
    def open_session(self,app,request):
        return {}

    def save_session(self, app, session, response):
        response.set_cookie('session_asfsafd',json.dumps(session))

    def is_null_session(self, obj):
        return False

app.session_interface=Mysessioninterface()

@app.route('/')
def index():
    ##执行session对象的__setitem__方法
    session['xxx']=123
    #这句完成的操作： 在local的ctx中找到session（初始状态为一个空字典），并在空字典中写值

    return "index"

if __name__ == '__main__':
    app.run()

##替换之后，在浏览器的session中可以看到我们下面的信息：
#session_asfsafd=“session['xxx']=123”

##另外，自定义的session的例子，请参考：
#下面的例子也是参考flask-session组件来实现的，可以直接使用那个组件就可以了。

# """
# http://www.cnblogs.com/wupeiqi/articles/7552008.html
#
# pip3 install Flask-Session
#
#         run.py
#             from flask import Flask
#             from flask import session
#             from pro_flask.utils.session import MySessionInterface
#             app = Flask(__name__)
#
#             app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#             app.session_interface = MySessionInterface()
#
#             @app.route('/login.html', methods=['GET', "POST"])
#             def login():
#                 print(session)
#                 session['user1'] = 'alex'
#                 session['user2'] = 'alex'
#                 del session['user2']
#
#                 return "内容"
#
#             if __name__ == '__main__':
#                 app.run()
#
#         session.py
#             #!/usr/bin/env python
#             # -*- coding:utf-8 -*-
#             import uuid
#             import json
#             from flask.sessions import SessionInterface
#             from flask.sessions import SessionMixin
#             from itsdangerous import Signer, BadSignature, want_bytes
#
#
#             class MySession(dict, SessionMixin):
#                 def __init__(self, initial=None, sid=None):
#                     self.sid = sid
#                     self.initial = initial
#                     super(MySession, self).__init__(initial or ())
#
#
#                 def __setitem__(self, key, value):
#                     super(MySession, self).__setitem__(key, value)
#
#                 def __getitem__(self, item):
#                     return super(MySession, self).__getitem__(item)
#
#                 def __delitem__(self, key):
#                     super(MySession, self).__delitem__(key)
#
#
#
#             class MySessionInterface(SessionInterface):
#                 session_class = MySession
#                 container = {}
#
#                 def __init__(self):
#                     import redis
#                     self.redis = redis.Redis()
#
#                 def _generate_sid(self):
#                     return str(uuid.uuid4())
#
#                 def _get_signer(self, app):
#                     if not app.secret_key:
#                         return None
#                     return Signer(app.secret_key, salt='flask-session',
#                                   key_derivation='hmac')
#
#                 def open_session(self, app, request):
#
#                     # 程序刚启动时执行，需要返回一个session对象
#                     """
#                     sid = request.cookies.get(app.session_cookie_name)
#                     if not sid:
#                         sid = self._generate_sid()
#                         return self.session_class(sid=sid)
#
#                     signer = self._get_signer(app)
#                     try:
#                         sid_as_bytes = signer.unsign(sid)
#                         sid = sid_as_bytes.decode()
#                     except BadSignature:
#                         sid = self._generate_sid()
#                         return self.session_class(sid=sid)
#
#                     # session保存在redis中
#                     # val = self.redis.get(sid)
#                     # session保存在内存中
#                     val = self.container.get(sid)
#
#                     if val is not None:
#                         try:
#                             data = json.loads(val)
#                             return self.session_class(data, sid=sid)
#                         except:
#                             return self.session_class(sid=sid)
#                     return self.session_class(sid=sid)
#
#                 def save_session(self, app, session, response):
#                     """
#                     # 程序结束前执行，可以保存session中所有的值
#                     # 如：
#                     #     保存到resit
#                     #     写入到用户cookie
#                     """
#                     domain = self.get_cookie_domain(app)
#                     path = self.get_cookie_path(app)
#                     httponly = self.get_cookie_httponly(app)
#                     secure = self.get_cookie_secure(app)
#                     expires = self.get_expiration_time(app, session)
#
#                     val = json.dumps(dict(session))
#
#                     # session保存在redis中
#                     # self.redis.setex(name=session.sid, value=val, time=app.permanent_session_lifetime)
#                     # session保存在内存中
#                     self.container.setdefault(session.sid, val)
#
#                     session_id = self._get_signer(app).sign(want_bytes(session.sid))
#
#                     response.set_cookie(app.session_cookie_name, session_id,
#                                         expires=expires, httponly=httponly,
#                                         domain=domain, path=path, secure=secure)
#
# 自定义Session


