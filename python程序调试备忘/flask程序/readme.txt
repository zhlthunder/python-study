github代码操作命令：
$ git clone https://github.com/miguelgrinberg/flasky.git   下载代码

check-out指定版本的程序：
$ git checkout 1a
上述命令中的 1a 代表一个标签（tag），是项目中某次提交历史的名字

一般情况下，你无需修改程序的源文件，但如果修改了，Git 会阻止你签出其他历史版本，
因为这会导致本地修改历史的丢失。签出其他历史版本之前，你要把文件还原到原始状态。最简单的方法是使用 git reset 命令：
$ git reset --hard
这个命令会损坏本地修改，所以执行此命令前你需要保存所有不想丢失的改动。

你可能经常需要从 GitHub 上下载修正和改进后的源码用于更新本地仓库。完成这个操作
的命令如下所示：
$ git fetch --all 
$ git fetch --tags 
$ git reset --hard origin/master

git  fetch 命令用于利用 GitHub 上的远程仓库更新本地仓库的提交历史和标签，但不会改
动真正的源文件，随后执行的 git  reset 命令才是用于更新文件的操作。再次提醒，执行
git reset 命令后，本地修改会丢失。

另一个有用的操作是查看程序两个版本之间的区别，以便了解改动详情。在命令行中，你
可以使用 git diff 命令进行查看。例如，执行下述命令可以查看 2a 和 2b 两个修订版本之
间的区别：
$ git diff  2a 2b



初始代码checkout方法及虚拟环境的搭建：
$ git clone https://github.com/miguelgrinberg/flasky.git 
$ cd flasky 
$ git checkout 1a
下一步是使用 virtualenv 命令在 flasky 文件夹中创建 Python 虚拟环境。这个命令只有一
个必需的参数，即虚拟环境的名字。创建虚拟环境后，当前文件夹中会出现一个子文件
夹，名字就是上述命令中指定的参数，与虚拟环境相关的文件都保存在这个子文件夹中。
按照惯例，一般虚拟环境会被命名为 venv：
$ virtualenv venv 
New python executable in venv/bin/python2.7 
Also creating executable in venv/bin/python 
Installing setuptools............done. 
Installing pip...............done.

现在，flasky 文件夹中就有了一个名为 venv 的子文件夹，它保存一个全新的虚拟环境，其
中有一个私有的 Python 解释器。在使用这个虚拟环境之前，你需要先将其“激活”。如果
你使用 bash 命令行（Linux 和 Mac OS X 用户），可以通过下面的命令激活这个虚拟环境：
$ source venv/bin/activate
如果使用微软 Windows 系统，激活命令是：
$ venv\Scripts\activate
虚拟环境被激活后，其中 Python 解释器的路径就被添加进 PATH 中，但这种改变不是永久
性的，它只会影响当前的命令行会话。为了提醒你已经激活了虚拟环境，激活虚拟环境的
命令会修改命令行提示符，加入环境名：
(venv) $
当虚拟环境中的工作完成后，如果你想回到全局 Python 解释器中，可以在命令行提示符下
输入 deactivate。


线程是可单独管理的最小指令集。进程经常使用多个活动线程，有时还会共
享内存或文件句柄等资源。多线程 Web 服务器会创建一个线程池，再从线
程池中选择一个线程用于处理接收到的请求。

#########################
下面这个 Python shell 会话演示了程序上下文的使用方法：
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
在这个例子中，没激活程序上下文之前就调用 current_app.name 会导致错误，但推送完上
下文之后就可以调用了。注意，在程序实例上调用 app.app_context() 可获得一个程序上
下文。

##############################
查看映射关系：
(venv) $ python 
>>> from hello import app 
>>> app.url_map 
Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>, 
 <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>, 
 <Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])
 
 
 #####################
 请求钩子或请求扩展：
 before_first_request 
：注册一个函数，在处理第一个请求之前运行。
before_request
：注册一个函数，在每次请求之前运行。
after_request
：注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
teardown_request
：注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。
在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量 g。例如，before_
request 处理程序可以从数据库中加载已登录用户，并将其保存到 g.user 中。随后调用视
图函数时，视图函数再使用 g.user 获取用户。


################# 
使用Flask-Bootstrap集成Twitter Bootstrap
说明：安装完flask-bootstrap，在C:\python3\Lib\site-packages\flask_bootstrap 下
就有了 static文件夹（包含css,js,fonts）和templates文件夹（里面包含常用的模板）

使用方法如下：
说明：
bootstrap_find_resource 用于加载flask-bootstrap打包的静态文件；对于我们自己的静态文件，使用 url_for来指定；
 <link href="{{ url_for('static',filename='css/bootstrap.css') }}" rel="stylesheet">
 
 Flask-Bootstrap 中的基模板提供了一个网页框架，引入了 Bootstrap 中的所有 CSS 和JavaScript 文件。
 
 初始化 Flask-Bootstrap 之后，就可以在程序中使用一个包含所有 Bootstrap 文件的基模板。
这个模板利用 Jinja2 的模板继承机制，让程序扩展一个具有基本页面结构的基模板，其中
就有用来引入 Bootstrap 的元素。
 
 Bootstrap 所需的文件在 styles 和 scripts 块中声明。如果程序需要向已经有内容的块
中添加新内容，必须使用 Jinja2 提供的 super() 函数。例如，如果要在衍生模板中添加新
的 JavaScript 文件，需要这么定义 scripts 块：
{% block scripts %} 
{{ super() }} 
<script type="text/javascript" src="my-script.js"></script> 
{% endblock %}

q&a：之所以样式没有适用，是因为使用的样式是网络上的，需要修改
C:\python3\Lib\site-packages\flask_bootstrap\__init__.py 文件，
app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', False) ==> app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', True)
这样修改之后，就会自动使用 flask-bootstrap安装目录下的 static文件（C:\python3\Lib\site-packages\flask_bootstrap\static；）了：


#########################
链接
在模板中直接编写简单路由的 URL 链接不难，但对于包含可变部分的动态路由，在模板
中构建正确的 URL 就很困难。而且，直接编写 URL 会对代码中定义的路由产生不必要的
依赖关系。如果重新定义路由，模板中的链接可能会失效。

为了避免这些问题，Flask 提供了 url_for() 辅助函数，它可以使用程序 URL 映射中保存
的信息生成 URL。
url_for() 函数最简单的用法是以视图函数名（或者 app.add_url_route() 定义路由时使用
的端点名）作为参数，返回对应的 URL。

比如在前端页面中
调用：    {{ url_for('index') }}   得到的结果是：‘/’
调用：  {{ url_for('index',_external=True) }}  得到的结果是： http://127.0.0.1:5000/

使 用 url_for() 生 成 动 态 地 址 时， 将 动 态 部 分 作 为 关 键 字 参 数 传 入。 例 如，url_for 
('user', name='john', _external=True) 的返回结果是 http://localhost:5000/user/john。
传入 url_for() 的关键字参数不仅限于动态路由中的参数。函数能将任何额外参数添加到
查询字符串中。例如，url_for('index', page=2) 的返回结果是 /?page=2。

==》：

   {{ url_for('index') }} <br/>
   {{ url_for('index',_external=True) }} <br/>
   {{ url_for('user', name='john', _external=True) }} <br/>
   {{ url_for('index', page=2) }}
   
   ==》对应输出：
   / 
http://127.0.0.1:5000/ 
http://127.0.0.1:5000/user/john 
/?page=2


####################################
静态文件：
Web 程序不是仅由 Python 代码和模板组成。大多数程序还会使用静态文件，例如 HTML
代码中引用的图片、JavaScript 源码文件和 CSS。

>>> from ss4 import app
>>> app.url_map
Map([<Rule '/index' (GET, OPTIONS, HEAD) -> index>, 
 <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>,   #即这条路由是默认包含的。
 <Rule '/user/<name>' (GET, OPTIONS, HEAD) -> user>])

 默认设置下，Flask 在程序根目录中名为 static 的子目录中寻找静态文件。如果需要，可在
static 文件夹中使用子文件夹存放文件。服务器收到前面那个 URL 后，会生成一个响应，
包含文件系统中 static/css/styles.css 文件的内容。

将favicon.ico app根目录的static文件夹下：
使用方法：
<link rel="icon" href="{{ url_for('static', filename = 'favicon.ico') }}"
    type="image/x-icon">

	
###################################
使用Flask-Moment本地化日期和时间  ？？？？？？？？？？？

使用时报错：
jinja2.exceptions.UndefinedError: 'moment' is undefined

查询后发现： Flask-Moment 模块使用的moment.js文件是从网络上下载的，引用位置如下：
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
                 'moment.js/%s/%s"></script>\n' % (version, js_filename)  ##此处为引用moment.js文件的位置；
        return Markup('''%s<script>

	

	
#######################
表单：
默认情况下，Flask-WTF 能保护所有表单免受跨站请求伪造（Cross-Site Request Forgery，
CSRF）的攻击。恶意网站把请求发送到被攻击者已登录的其他网站时就会引发 CSRF 攻击。
为了实现 CSRF 保护，Flask-WTF 需要程序设置一个密钥。Flask-WTF 使用这个密钥生成
加密令牌，再用令牌验证请求中表单数据的真伪。

使用 Flask-WTF 时，每个 Web 表单都由一个继承自 Form 的类表示。这个类定义表单中的
一组字段，每个字段都用对象表示。字段对象可附属一个或多个验证函数。验证函数用来
验证用户提交的输入值是否符合要求。


前端页面接收表单对象后渲染的方法：

{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}  ##相关步骤1

{% block title %}Flasky{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
</div>
{{ wtf.quick_form(form) }}   ##相关步骤2
{% endblock %}



############################
重定向和用户会话：
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    data=form.name.data
    if request.method=='POST':
        name = request.form.get('name')
        form.name.data = ''
        session['name']=name   ##将会话信息写入session
        return  redirect('/')   ##接收post 请求后，重定向到别的URL地址；
	# session.pop('name')  #移除session中存储的数据
        # print(name)
    return render_template('index.html', form=form, name=session.get('name'))  ##在跳转之后的请求中，获取这个会话信息


	

#####################
Flash消息
仅调用 flash() 函数并不能把消息显示出来，程序使用的模板要渲染这些消息。最好在
基模板中渲染 Flash 消息，因为这样所有页面都能使用这些消息。Flask 把 get_flashed_
messages() 函数开放给模板，用来获取并渲染消息，

使用如下：
后台写入flash后：
@app.route('/', methods=['GET', 'POST'])
def index():
    flash('Looks like you have changed your name!')
    return render_template('index.html')

##前端直接调用get_flashed_messages() 获取写入flash中的数据
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

 
当然也可以在后端调用get_flashed_messages()，然后通过变量把信息传递到前端页面；
@app.route('/user/<name>')
def user(name):
    # data=get_flashed_messages()
    # print(data)
    return render_template('user.html',name=name)

总结：flash是基于session实现的，即在多次访问过程中有记忆的功能，但要注意闪现中的消息写入后，读取一次的同时会销毁掉。




########################
数据库：
通过命令行手动创建数据表的方法：
C:\Users\Administrator\Desktop\python_related_data\zhl_working_directory\cmdb\flasky>python
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from flask_sqlalchemyyy import db  //导入db
C:\Users\Administrator\Desktop\python_related_data\zhl_working_directory\cmdb\flasky\flask_sqlalchemyyy.py:5: ExtDeprecationWarning: Importing flask.ext.bootstrap is deprecated, use flask_bootstrap instead.
  from flask.ext.bootstrap import Bootstrap
C:\python3\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppre
ss this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
>>> db.create_all()  //执行创建数据库的操作
执行之后，在目录下就看到了数据库文件：data.sqlite

数据库会话也可回滚。调用 db.session.rollback() 后，添加到数据库会话
中的所有对象都会还原到它们在数据库时的


####################
集成Python shell:
每次启动 shell 会话都要导入数据库实例和模型，这真是份枯燥的工作。为了避免一直重复
导入，我们可以做些配置，让 Flask-Script 的 shell 命令自动导入特定的对象。
若想把对象添加到导入列表中，我们要为 shell 命令注册一个 make_context 回调函数


用 manager 封装app后，执行 python **.py 输出如下的帮助信息
usage: manager&shell.py [-?] {shell,runserver} ...

positional arguments:
  {shell,runserver}
    shell            Runs a Python shell inside Flask application context.  //此处就是我们需要使用的内置shell脚本；
    runserver        Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help         show this help message and exit


配置方法：
manager=Manager(app)
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role) #将上下文环境所需导入的内容都添加进来
manager.add_command("shell", Shell(make_context=make_shell_context))

此时执行：python "manager&shell.py" shell 后，相关的变量已经导入完成，信息如下：
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
为了导出数据库迁移命令，Flask-Migrate 提供了一个 MigrateCommand 类，可附加到 Flask-
Script 的 manager 对象上。在这个例子中，MigrateCommand 类使用 db 命令附加。

在维护数据库迁移之前，要使用 init 子命令创建迁移仓库：
    # 运行时提示下面的错误，待继续排查：
    # ImportError: cannot import name 'Migrate'
	
	
########################
用户认证：
	
使用Werkzeug实现密码散列
Werkzeug 中的 security 模块能够很方便地实现密码散列值的计算。这一功能的实现只需要
两个函数，分别用在注册用户和验证用户阶段。
generate_password_hash(password, method=
? 
pbkdf2:sha1, salt_length=8)：这个函数将
原始密码作为输入，以字符串形式输出密码的散列值，输出的值可保存在用户数据库中。
method 和 salt_length 的默认值就能满足大多数需求。
check_password_hash(hash, password)
? 
：这个函数的参数是从数据库中取回的密码散列
值和用户输入的密码。返回值为 True 表明密码正确。



#####
多app 离线操作时：
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

##输出： 此时可以看到内部的存储信息
# {20468: {'stack': [<flask.ctx.AppContext object at 0x00000084502F53C8>]}}
# {20468: {'stack': [<flask.ctx.AppContext object at 0x00000084502F53C8>, <flask.ctx.AppContext object at 0x00000084502F5518>]}}
# {}

"""
完整的存储结构：
在_app_ctx_stack._local.__storage__中存储的信息：
{20468（线程唯一标识）: {'stack'（固定字段）: [<flask.ctx.AppContext object at 0x00000084502F53C8>]//在一个列表中存储flask对象}}


"""


"""
注意在访问栈中的详细信息和栈操作时的区别：
访问栈中的内容，使用下面的路径进行访问
_app_ctx_stack._local.__storage__

压栈和弹栈时，使用如下的操作：
_app_ctx_stack.push
_app_ctx_stack.top
_app_ctx_stack.pop

"""


#######################################








