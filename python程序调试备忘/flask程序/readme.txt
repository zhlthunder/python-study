github����������
$ git clone https://github.com/miguelgrinberg/flasky.git   ���ش���

check-outָ���汾�ĳ���
$ git checkout 1a
���������е� 1a ����һ����ǩ��tag��������Ŀ��ĳ���ύ��ʷ������

һ������£��������޸ĳ����Դ�ļ���������޸��ˣ�Git ����ֹ��ǩ��������ʷ�汾��
��Ϊ��ᵼ�±����޸���ʷ�Ķ�ʧ��ǩ��������ʷ�汾֮ǰ����Ҫ���ļ���ԭ��ԭʼ״̬����򵥵ķ�����ʹ�� git reset ���
$ git reset --hard
���������𻵱����޸ģ�����ִ�д�����ǰ����Ҫ�������в��붪ʧ�ĸĶ���

����ܾ�����Ҫ�� GitHub �����������͸Ľ����Դ�����ڸ��±��زֿ⡣����������
������������ʾ��
$ git fetch --all 
$ git fetch --tags 
$ git reset --hard origin/master

git  fetch ������������ GitHub �ϵ�Զ�ֿ̲���±��زֿ���ύ��ʷ�ͱ�ǩ���������
��������Դ�ļ������ִ�е� git  reset ����������ڸ����ļ��Ĳ������ٴ����ѣ�ִ��
git reset ����󣬱����޸Ļᶪʧ��

��һ�����õĲ����ǲ鿴���������汾֮��������Ա��˽�Ķ����顣���������У���
����ʹ�� git diff ������в鿴�����磬ִ������������Բ鿴 2a �� 2b �����޶��汾֮
�������
$ git diff  2a 2b



��ʼ����checkout���������⻷���Ĵ��
$ git clone https://github.com/miguelgrinberg/flasky.git 
$ cd flasky 
$ git checkout 1a
��һ����ʹ�� virtualenv ������ flasky �ļ����д��� Python ���⻷�����������ֻ��һ
������Ĳ����������⻷�������֡��������⻷���󣬵�ǰ�ļ����л����һ�����ļ�
�У����־�������������ָ���Ĳ����������⻷����ص��ļ���������������ļ����С�
���չ�����һ�����⻷���ᱻ����Ϊ venv��
$ virtualenv venv 
New python executable in venv/bin/python2.7 
Also creating executable in venv/bin/python 
Installing setuptools............done. 
Installing pip...............done.

���ڣ�flasky �ļ����о�����һ����Ϊ venv �����ļ��У�������һ��ȫ�µ����⻷������
����һ��˽�е� Python ����������ʹ��������⻷��֮ǰ������Ҫ�Ƚ��䡰��������
��ʹ�� bash �����У�Linux �� Mac OS X �û���������ͨ������������������⻷����
$ source venv/bin/activate
���ʹ��΢�� Windows ϵͳ�����������ǣ�
$ venv\Scripts\activate
���⻷������������� Python ��������·���ͱ���ӽ� PATH �У������ָı䲻������
�Եģ���ֻ��Ӱ�쵱ǰ�������лỰ��Ϊ���������Ѿ����������⻷�����������⻷����
������޸���������ʾ�������뻷������
(venv) $
�����⻷���еĹ�����ɺ��������ص�ȫ�� Python �������У���������������ʾ����
���� deactivate��


�߳��ǿɵ����������Сָ������̾���ʹ�ö����̣߳���ʱ���Ṳ
���ڴ���ļ��������Դ�����߳� Web �������ᴴ��һ���̳߳أ��ٴ���
�̳���ѡ��һ���߳����ڴ�����յ�������

#########################
������� Python shell �Ự��ʾ�˳��������ĵ�ʹ�÷�����
C:\Users\Administrator\Desktop\python_related_data\zhl_working_directory\cmdb\flasky>python
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from ss1 import app
>>> from flask import current_app
>>> current_app.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\python3\lib\site-packages\werkzeug\local.py", line 367, in __getattr__
    return getattr(self._get_current_object(), name)
>>> app_ctx=app.app_context()
>>> app_ctx.push()
>>> current_app.name
'ss1'
����������У�û�������������֮ǰ�͵��� current_app.name �ᵼ�´��󣬵���������
����֮��Ϳ��Ե����ˡ�ע�⣬�ڳ���ʵ���ϵ��� app.app_context() �ɻ��һ��������
���ġ�

##############################
�鿴ӳ���ϵ��
(venv) $ python 
>>> from hello import app 
>>> app.url_map 
Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>, 
 <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>, 
 <Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])
 
 
 #####################
 �����ӻ�������չ��
 before_first_request 
��ע��һ���������ڴ����һ������֮ǰ���С�
before_request
��ע��һ����������ÿ������֮ǰ���С�
after_request
��ע��һ�����������û��δ������쳣�׳�����ÿ������֮�����С�
teardown_request
��ע��һ����������ʹ��δ������쳣�׳���Ҳ��ÿ������֮�����С�
�������Ӻ�������ͼ����֮�乲������һ��ʹ��������ȫ�ֱ��� g�����磬before_
request ���������Դ����ݿ��м����ѵ�¼�û��������䱣�浽 g.user �С���������
ͼ����ʱ����ͼ������ʹ�� g.user ��ȡ�û���


################# 
ʹ��Flask-Bootstrap����Twitter Bootstrap
˵������װ��flask-bootstrap����C:\python3\Lib\site-packages\flask_bootstrap ��
������ static�ļ��У�����css,js,fonts����templates�ļ��У�����������õ�ģ�壩

ʹ�÷������£�
˵����
bootstrap_find_resource ���ڼ���flask-bootstrap����ľ�̬�ļ������������Լ��ľ�̬�ļ���ʹ�� url_for��ָ����
 <link href="{{ url_for('static',filename='css/bootstrap.css') }}" rel="stylesheet">
 
 Flask-Bootstrap �еĻ�ģ���ṩ��һ����ҳ��ܣ������� Bootstrap �е����� CSS ��JavaScript �ļ���
 
 ��ʼ�� Flask-Bootstrap ֮�󣬾Ϳ����ڳ�����ʹ��һ���������� Bootstrap �ļ��Ļ�ģ�塣
���ģ������ Jinja2 ��ģ��̳л��ƣ��ó�����չһ�����л���ҳ��ṹ�Ļ�ģ�壬����
������������ Bootstrap ��Ԫ�ء�
 
 Bootstrap ������ļ��� styles �� scripts �������������������Ҫ���Ѿ������ݵĿ�
����������ݣ�����ʹ�� Jinja2 �ṩ�� super() ���������磬���Ҫ������ģ���������
�� JavaScript �ļ�����Ҫ��ô���� scripts �飺
{% block scripts %} 
{{ super() }} 
<script type="text/javascript" src="my-script.js"></script> 
{% endblock %}

q&a��֮������ʽû�����ã�����Ϊʹ�õ���ʽ�������ϵģ���Ҫ�޸�
C:\python3\Lib\site-packages\flask_bootstrap\__init__.py �ļ���
app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', False) ==> app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', True)
�����޸�֮�󣬾ͻ��Զ�ʹ�� flask-bootstrap��װĿ¼�µ� static�ļ���C:\python3\Lib\site-packages\flask_bootstrap\static�����ˣ�


#########################
����
��ģ����ֱ�ӱ�д��·�ɵ� URL ���Ӳ��ѣ������ڰ����ɱ䲿�ֵĶ�̬·�ɣ���ģ��
�й�����ȷ�� URL �ͺ����ѡ����ң�ֱ�ӱ�д URL ��Դ����ж����·�ɲ�������Ҫ��
������ϵ��������¶���·�ɣ�ģ���е����ӿ��ܻ�ʧЧ��

Ϊ�˱�����Щ���⣬Flask �ṩ�� url_for() ����������������ʹ�ó��� URL ӳ���б���
����Ϣ���� URL��
url_for() ������򵥵��÷�������ͼ������������ app.add_url_route() ����·��ʱʹ��
�Ķ˵�������Ϊ���������ض�Ӧ�� URL��

������ǰ��ҳ����
���ã�    {{ url_for('index') }}   �õ��Ľ���ǣ���/��
���ã�  {{ url_for('index',_external=True) }}  �õ��Ľ���ǣ� http://127.0.0.1:5000/

ʹ �� url_for() �� �� �� ̬ �� ַ ʱ�� �� �� ̬ �� �� �� Ϊ �� �� �� �� �� �� �롣 �� �磬url_for 
('user', name='john', _external=True) �ķ��ؽ���� http://localhost:5000/user/john��
���� url_for() �Ĺؼ��ֲ����������ڶ�̬·���еĲ����������ܽ��κζ��������ӵ�
��ѯ�ַ����С����磬url_for('index', page=2) �ķ��ؽ���� /?page=2��

==����

   {{ url_for('index') }} <br/>
   {{ url_for('index',_external=True) }} <br/>
   {{ url_for('user', name='john', _external=True) }} <br/>
   {{ url_for('index', page=2) }}
   
   ==����Ӧ�����
   / 
http://127.0.0.1:5000/ 
http://127.0.0.1:5000/user/john 
/?page=2


####################################
��̬�ļ���
Web �����ǽ��� Python �����ģ����ɡ���������򻹻�ʹ�þ�̬�ļ������� HTML
���������õ�ͼƬ��JavaScript Դ���ļ��� CSS��

>>> from ss4 import app
>>> app.url_map
Map([<Rule '/index' (GET, OPTIONS, HEAD) -> index>, 
 <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>,   #������·����Ĭ�ϰ����ġ�
 <Rule '/user/<name>' (GET, OPTIONS, HEAD) -> user>])

 Ĭ�������£�Flask �ڳ����Ŀ¼����Ϊ static ����Ŀ¼��Ѱ�Ҿ�̬�ļ��������Ҫ������
static �ļ�����ʹ�����ļ��д���ļ����������յ�ǰ���Ǹ� URL �󣬻�����һ����Ӧ��
�����ļ�ϵͳ�� static/css/styles.css �ļ������ݡ�

��favicon.ico app��Ŀ¼��static�ļ����£�
ʹ�÷�����
<link rel="icon" href="{{ url_for('static', filename = 'favicon.ico') }}"
    type="image/x-icon">

	
###################################
ʹ��Flask-Moment���ػ����ں�ʱ��  ����������������������

ʹ��ʱ����
jinja2.exceptions.UndefinedError: 'moment' is undefined

��ѯ���֣� Flask-Moment ģ��ʹ�õ�moment.js�ļ��Ǵ����������صģ�����λ�����£�
C:\python3\Lib\site-packages\flask_moment.py

def include_moment(version='2.18.1', local_js=None):
        js = ''
        if local_js is not None:
            js = '<script src="%s"></script>\n' % local_js
        elif version is not None:
            js_filename = 'moment-with-locales.min.js' \
                if StrictVersion(version) >= StrictVersion('2.8.0') \
                else 'moment-with-langs.min.js'
            js = '<script src="//cdnjs.cloudflare.com/ajax/libs/' \
                 'moment.js/%s/%s"></script>\n' % (version, js_filename)  ##�˴�Ϊ����moment.js�ļ���λ�ã�
        return Markup('''%s<script>

	

	
#######################
����
Ĭ������£�Flask-WTF �ܱ������б����ܿ�վ����α�죨Cross-Site Request Forgery��
CSRF���Ĺ�����������վ�������͵����������ѵ�¼��������վʱ�ͻ����� CSRF ������
Ϊ��ʵ�� CSRF ������Flask-WTF ��Ҫ��������һ����Կ��Flask-WTF ʹ�������Կ����
�������ƣ�����������֤�����б����ݵ���α��

ʹ�� Flask-WTF ʱ��ÿ�� Web ������һ���̳��� Form �����ʾ������ඨ����е�
һ���ֶΣ�ÿ���ֶζ��ö����ʾ���ֶζ���ɸ���һ��������֤��������֤��������
��֤�û��ύ������ֵ�Ƿ����Ҫ��


ǰ��ҳ����ձ��������Ⱦ�ķ�����

{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}  ##��ز���1

{% block title %}Flasky{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
</div>
{{ wtf.quick_form(form) }}   ##��ز���2
{% endblock %}



############################
�ض�����û��Ự��
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    data=form.name.data
    if request.method=='POST':
        name = request.form.get('name')
        form.name.data = ''
        session['name']=name   ##���Ự��Ϣд��session
        return  redirect('/')   ##����post ������ض��򵽱��URL��ַ��
	# session.pop('name')  #�Ƴ�session�д洢������
        # print(name)
    return render_template('index.html', form=form, name=session.get('name'))  ##����ת֮��������У���ȡ����Ự��Ϣ


	

#####################
Flash��Ϣ
������ flash() ���������ܰ���Ϣ��ʾ����������ʹ�õ�ģ��Ҫ��Ⱦ��Щ��Ϣ�������
��ģ������Ⱦ Flash ��Ϣ����Ϊ��������ҳ�涼��ʹ����Щ��Ϣ��Flask �� get_flashed_
messages() �������Ÿ�ģ�壬������ȡ����Ⱦ��Ϣ��

ʹ�����£�
��̨д��flash��
@app.route('/', methods=['GET', 'POST'])
def index():
    flash('Looks like you have changed your name!')
    return render_template('index.html')

##ǰ��ֱ�ӵ���get_flashed_messages() ��ȡд��flash�е�����
{% block content %} 
<div class="container"> 
    <div class="page-header"> 
        <h1>Hello, {{ name }}!</h1>
        {% for message in get_flashed_messages() %}
        <div class="alert alert-warning">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        {{ message }}
           </div>
       {% endfor %}
    </div> 
</div> 
{% endblock %}

 
��ȻҲ�����ں�˵���get_flashed_messages()��Ȼ��ͨ����������Ϣ���ݵ�ǰ��ҳ�棻
@app.route('/user/<name>')
def user(name):
    # data=get_flashed_messages()
    # print(data)
    return render_template('user.html',name=name)

�ܽ᣺flash�ǻ���sessionʵ�ֵģ����ڶ�η��ʹ������м���Ĺ��ܣ���Ҫע�������е���Ϣд��󣬶�ȡһ�ε�ͬʱ�����ٵ���




########################
���ݿ⣺
ͨ���������ֶ��������ݱ�ķ�����
C:\Users\Administrator\Desktop\python_related_data\zhl_working_directory\cmdb\flasky>python
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from flask_sqlalchemyyy import db  //����db
C:\Users\Administrator\Desktop\python_related_data\zhl_working_directory\cmdb\flasky\flask_sqlalchemyyy.py:5: ExtDeprecationWarning: Importing flask.ext.bootstrap is deprecated, use flask_bootstrap instead.
  from flask.ext.bootstrap import Bootstrap
C:\python3\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppre
ss this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
>>> db.create_all()  //ִ�д������ݿ�Ĳ���
ִ��֮����Ŀ¼�¾Ϳ��������ݿ��ļ���data.sqlite

���ݿ�ỰҲ�ɻع������� db.session.rollback() ����ӵ����ݿ�Ự
�е����ж��󶼻ỹԭ�����������ݿ�ʱ��


####################
����Python shell:
ÿ������ shell �Ự��Ҫ�������ݿ�ʵ����ģ�ͣ������Ƿݿ���Ĺ�����Ϊ�˱���һֱ�ظ�
���룬���ǿ�����Щ���ã��� Flask-Script �� shell �����Զ������ض��Ķ���
����Ѷ�����ӵ������б��У�����ҪΪ shell ����ע��һ�� make_context �ص�����


�� manager ��װapp��ִ�� python **.py ������µİ�����Ϣ
usage: manager&shell.py [-?] {shell,runserver} ...

positional arguments:
  {shell,runserver}
    shell            Runs a Python shell inside Flask application context.  //�˴�����������Ҫʹ�õ�����shell�ű���
    runserver        Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help         show this help message and exit


���÷�����
manager=Manager(app)
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role) #�������Ļ������赼������ݶ���ӽ���
manager.add_command("shell", Shell(make_context=make_shell_context))

��ʱִ�У�python "manager&shell.py" shell ����صı����Ѿ�������ɣ���Ϣ���£�
C:\Users\Administrator\Desktop\python_related_data\zhl_working_directory\cmdb\flasky>python "manager&shell.py" shell
manager&shell.py:5: ExtDeprecationWarning: Importing flask.ext.bootstrap is deprecated, use flask_bootstrap instead.
  from flask.ext.bootstrap import Bootstrap
manager&shell.py:11: ExtDeprecationWarning: Importing flask.ext.script is deprecated, use flask_script instead.
  from flask.ext.script import Shell,Manager
C:\python3\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppre
ss this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
>>> app
<Flask 'manager&shell'>
>>> db
<SQLAlchemy engine=sqlite:///C:\Users\Administrator\Desktop\python_related_data\zhl_working_directory\cmdb\flasky\data.sqlite>


######################
Ϊ�˵������ݿ�Ǩ�����Flask-Migrate �ṩ��һ�� MigrateCommand �࣬�ɸ��ӵ� Flask-
Script �� manager �����ϡ�����������У�MigrateCommand ��ʹ�� db ����ӡ�

��ά�����ݿ�Ǩ��֮ǰ��Ҫʹ�� init �������Ǩ�Ʋֿ⣺
    # ����ʱ��ʾ����Ĵ��󣬴������Ų飺
    # ImportError: cannot import name 'Migrate'
	
	
########################
�û���֤��
	
ʹ��Werkzeugʵ������ɢ��
Werkzeug �е� security ģ���ܹ��ܷ����ʵ������ɢ��ֵ�ļ��㡣��һ���ܵ�ʵ��ֻ��Ҫ
�����������ֱ�����ע���û�����֤�û��׶Ρ�
generate_password_hash(password, method=
? 
pbkdf2:sha1, salt_length=8)�����������
ԭʼ������Ϊ���룬���ַ�����ʽ��������ɢ��ֵ�������ֵ�ɱ������û����ݿ��С�
method �� salt_length ��Ĭ��ֵ����������������
check_password_hash(hash, password)
? 
����������Ĳ����Ǵ����ݿ���ȡ�ص�����ɢ��
ֵ���û���������롣����ֵΪ True ����������ȷ��



#####
��app ���߲���ʱ��
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,current_app,globals,_app_ctx_stack

app01=Flask('app01')
app02=Flask('app02')

# app01.app_context()= AppContext(self)
with app01.app_context():
    print(_app_ctx_stack._local.__storage__)
    with app02.app_context():
        print(_app_ctx_stack._local.__storage__)
        pass
print(_app_ctx_stack._local.__storage__)

##����� ��ʱ���Կ����ڲ��Ĵ洢��Ϣ
# {20468: {'stack': [<flask.ctx.AppContext object at 0x00000084502F53C8>]}}
# {20468: {'stack': [<flask.ctx.AppContext object at 0x00000084502F53C8>, <flask.ctx.AppContext object at 0x00000084502F5518>]}}
# {}

"""
�����Ĵ洢�ṹ��
��_app_ctx_stack._local.__storage__�д洢����Ϣ��
{20468���߳�Ψһ��ʶ��: {'stack'���̶��ֶΣ�: [<flask.ctx.AppContext object at 0x00000084502F53C8>]//��һ���б��д洢flask����}}


"""


"""
ע���ڷ���ջ�е���ϸ��Ϣ��ջ����ʱ������
����ջ�е����ݣ�ʹ�������·�����з���
_app_ctx_stack._local.__storage__

ѹջ�͵�ջʱ��ʹ�����µĲ�����
_app_ctx_stack.push
_app_ctx_stack.top
_app_ctx_stack.pop

"""


#######################################








