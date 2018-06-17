1.url匹配模式说明：
  url(r'^test1/\d{2}/$', test1),   正则匹配方式1，这种方式不需要传参数到后台；后台视图函数只有一个request参数；
  url(r'^test2/(?P<id>\d{2})/$', test2), 正则匹配方式2，使用了命名分组的方式，需要向后台传递数据（id=\d{2}），且后台视图函数必须包含一个名称为id的参数，否则会报错；
      url(r'^test3/(\d{2})/$', test3),   正则匹配方式3，使用了无命名分组的方式，需要向后台传递数据（\d{2}），且后台视图函数需要定义一个参数来接收前段发送过来的数据，参数名称任意；
	  
2.djago上下文对象：
多数时间，你可以通过传递一个完全填充(full populated)的字典给  Context()  来初始化  上下文(Context)  。
但是初始化以后，你也可以使用标准的 Python 字典语法(syntax)向``上下文(Context)``  对象添加或者删除条目:

>>>  from  django.template  import  Context
>>>  c  =  Context({"foo":  "bar"})
>>>  c['foo']
'bar'
>>>  del  c['foo']
>>>  c['foo']
Traceback  (most  recent  call  last):
...
KeyError:  'foo'
>>>  c['newvariable']  =  'hello'
>>>  c['newvariable']
'hello'

3.过滤器
就象本章前面提到的一样，模板过滤器是在变量被显示前修改它的值的一个简单方法。  过滤器使用管道字符
{{  name|lower  }} 它功能是转换文本为小写
{{  my_list|first|upper  }} 查找列表的第一个元素并将其转化为大写

有些过滤器有参数。  过滤器的参数跟随冒号之后并且总是以双引号包含
{{  bio|truncatewords:"5"  }} 这个将显示变量  bio  的前 5个词  //验证不成功，待排查

4. settings.py中模板文件路径配置：
使用绝对路径的方式：
默认是在app/templates中寻找模板，如果创建在其它地方，需要在settings.py中做如下的配置。
TEMPLATE_DIRS  =  (
'/home/django/mysite/templates',  //如果是windows，需要把\ -->/
)
Python  要求单元素元组中必须使用逗号，以此消除与圆括号表达式之间的歧义。  这是新手常犯的错误。
如果使用的是  Windows  平台，请包含驱动器符号并使用 Unix 风格的斜杠（/）而不是反斜杠（\）

灵活的配置方法：
TEMPLATE_DIRS  =  (
    os.path.join(os.path.dirname(os.path.dirname(__file__)),  'templates').replace('\\','/'),
)

 Python  内部变量  __file__  ，该变量被自动设置为代码所在的  Python  模块文件
名。  `` os.path.dirname(os.path.dirname(__file__))``  将会获取自身所在的文件，即 settings.py  所在的目录的上一级目录，
然后由
os.path.join  这个方法将这目录与  templates  进行连接。如果在 windows 下，它会智能地选择正确的后向斜
杠”“进行连接，而不是前向斜杠”/”


5.locals()  技巧
。它
返回的字典对所有局部变量的名称与值进行映射
return  render_to_response('current_datetime.html',  locals())
使用  locals()  时要注意是它将包括 所有  的局部变量，它们可能比你想让模板访问的要多。

6. 模板文件分层处理：
return  render_to_response('dateapp/current_datetime.html',  {'current_date':  now})
对子目录树的深度没有限制，你想要多少层都可以。  只要你喜欢，用多少层的子目录都无所谓。


7.  forms
表单验证时，当用户提交的表单发生错误时，可以将已经正确的字段返回到前端 ，例子：
html:
<html>
<head>
<title>Contact  us</title>
</head>

<body>
<h1>Contact  us</h1>
{%  if  errors  %}
<ul>
{%  for  error  in  errors  %}
<li>{{  error  }}</li>
{%  endfor  %}
</ul>
{%  endif  %}
<form  action="/contact/"  method="post">
<p>Subject:  <input  type="text"  name="subject"  value="{{ subject }}"  ></p>
<p>Your  e-mail  (optional):  <input  type="text"  name="email"  value="{{  email  }}" ></p>
<p>Message:  <textarea  name="message"  rows="10"  cols="50">{{  message  }}</textarea></p>
    <input  type="submit"  value="Submit">
</form>
</body>
</html>


def  contact(request):
	errors  =  []
	if  request.method  ==  'POST':
		if  not  request.POST.get('subject',  ''):
			errors.append('Enter  a  subject.')
		if  not  request.POST.get('message',  ''):
			errors.append('Enter  a  message.')
		if  not  request.POST.get('email',  ''):
			errors.append('Enter  a  email address.')
		if  request.POST.get('email')  and  '@'  not  in  request.POST['email']:
			errors.append('Enter  a  valid  e-mail  address.')
		if  not  errors:
		# 	send_mail(
		# request.POST['subject'],
		# request.POST['message'],
		# request.POST.get('email',  'noreply@example.com`_'),
		# ['siteowner@example.com`_'],
		# )
			return  HttpResponseRedirect('/contact/thanks/')
	return  render_to_response('contact_form.html',  {
'errors':  errors,
'subject':  request.POST.get('subject',  ''),
'message':  request.POST.get('message',  ''),
'email':  request.POST.get('email',  ''),
})

这看起来杂乱，且写的时候容易出错。 希望你开始明白使用高级库的用意——负责处理表单及相关校验任
务。

第一个 Form 类
Django 带有一个 form 库，称为 django.forms，这个库可以处理我们本章所提到的包括 HTML 表单显示
以及验证。

f  =  ContactForm({'subject':  'Hello',  'email':  'adrian@example.com',  'message':  'Nice  site!'})  //form实体赋值
>>>  f.is_bound
True
调用任何绑定 form 的 is_valid()方法，就可以知道它的数据是否合法。  我们已经为每个字段传入了值，
因此整个 Form 是合法的：
>>>  f.is_valid()
True

你可以逐一查看每个字段的出错消息：
>>>  f  =  ContactForm({'subject':  'Hello',  'message':  ''})
>>>  f['message'].errors
[u'This  field  is  required.']
>>>  f['subject'].errors
[]
>>>  f['email'].errors
[]
备注：每一个邦定 Form 实体都有一个 errors 属性，它为你提供了一个字段与错误消息相映射的字典表。

最终，如果一个 Form 实体的数据是合法的，它就会有一个可用的 cleaned_data 属性。 这是一个包含干净的
提交数据的字典。 Django 的 form 框架不但校验数据，它还会把它们转换成相应的 Python 类型数据，这叫做
清理数据。

>>> obj=ContactForm({'subject':"asdfasd",'message':'asdfasfdasfd'})
>>> obj.is_valid()
True
>>> obj.cleaned_data
{'message': u'asdfasfdasfd', 'email': u'', 'subject': u'asdfasd'}

8.模板：
context  是一个传递给模板的名称到值的映射（类似 Python 字典）。
模板 渲染  就是是通过从 context 获取值来替换模板中变量并执行所有的模板标签。

RequestContext 和 Context 处理器
你需要一段 context 来解析模板。一般情况下，这是一个  django.template.Context  的实例，不过在 Django
中还可以用一个特殊的子类，django.template.RequestContext  ，这个用起来稍微有些不同。 RequestContext  默
认地在模板 context 中加入了一些变量，如  HttpRequest  对象或当前登录用户的相关信息；
当你不想在一系例模板中都明确指定一些相同的变量时，你应该使用  RequestContext  


django.core.context_processors.debug：
由于调试信息比较敏感，所以这个 context 处理器只有当同时满足下面两个条件的时候才有效：
?   DEBUG  参数设置为  True  。
?  请求的 ip 应该包含在  INTERNAL_IPS  的设置里面。


9. 会话，用户和注册：
cookie& session对比：
相同点：
两者都需要基于cookie的机制向客户端发送信息；
在服务器端，用户的有效信息都存储在数据库中；

区别： 
session 的机制相对更复杂一些，可以存储用户在服务器端的所有操作，比如购物操作等等；且所有的客户数据都存储在服务器端，只是把数据的哈希会话ID通过cookie发送到客户端；
cookie 的实现相对简单，只支持简单的设置，且设置的数据会被发送到客户。

cookie:
 cookies  是浏览器为  Web  服务器存储的一小段信息。  每次浏览器从某个服务器请求页
面时，它向服务器回送之前收到的 cookies

于是  Cookies  的值会告诉 Google，你就是早些时候访问过 Google 网站的人。  这个值可能是数据库中存
储用户信息的 key，可以用它在页面上显示你的用户名。  Google 会（以及目前）使用它在网页上显示你账号
的用户名。


实例：
def  set_color(request):
	if  "favorite_color"  in  request.GET:
		response  =  HttpResponse("Your  favorite  color  is  now  %s"  % request.GET["favorite_color"])
		response.set_cookie("favorite_color",request.GET["favorite_color"])
		return  response
	else:
		return  HttpResponse("You  didn't  give  a  favorite  color.")
在浏览器中输入如下内容，提交get请求到服务器端，并携带favorite_color 字段；
http://127.0.0.1:8000/set_color/?favorite_color=zzzzz  
返回的响应信息： Your favorite color is now zzzzz

且浏览器的cookie中记录如下的信息：
名字：	favorite_color
内容：	zzzzz
域：	127.0.0.1
路径：	/
发送用途：	各种连接
脚本可访问：	是
创建时间：	2016年6月2日星期四 上午8:21:31
过期时间：	浏览会话结束时


Session:
Django 的  Session  框架
由于存在的限制与安全漏洞，cookies 和持续性会话已经成为 Web 开发中令人头疼的典范。 好消息是，
Django 的目标正是高效的“头疼杀手”，它自带的 session 框架会帮你搞定这些问题。
你可以用 session  框架来存取每个访问者任意数据，  这些数据在服务器端存储，并对 cookie 的收发进
行了抽象。  Cookies 只存储数据的哈希会话 ID，而不是数据本身，从而避免了大部分的常见 cookie 问题。


从内部来看，每个 session 都只是一个普通的 Django model（在  django.contrib.sessions.models  中
定义)。每个 session 都由一个随机的 32 字节哈希串来标识，并存储于 cookie 中。  因为它是一个标准的
模型，所以你可以使用 Django 数据库 API 来存取 session。
##使用浏览器缓存的cookie在服务器的数据库下查询到的信息：
>>> s=Session.objects.get(pk='7sxh301z7ymsbcsz6rpkmuqfvwttlui7')  ##这是客户端浏览器中获取到的sessionid
>>> s.expire_date
datetime.datetime(2016, 6, 15, 8, 19, 36, tzinfo=<UTC>)
>>> s.session_data
u'OGRlMDU2N2NhNDdkZTYxYmZjODY0OTIzZjk5NGI4ZDMyODQyNDkxZDp7fQ=='
>>> s.get_decoded()
{}  //此时没有存储session数据；

缺省的情况下，Django 只会在 session 发生变化的时候才会存入数据库，比如说，字典赋值或删除。

在视图函数中执行：
request.session['foo']  =  'bar' 后 ：
重新登录到交换模式后再次 查询到的信息：>>> from django.contrib.sessions.models import Session
>>> s=Session.objects.get(pk='7sxh301z7ymsbcsz6rpkmuqfvwttlui7')
>>> s.session_data
u'MjQ0ZWQzNDY0ODNlMzBjNDU3ZDc3OTM5OTRkNjc2ZWNiMmIyMTA4Yzp7ImZvbyI6ImJhciJ9'
>>> s.get_decoded()
{u'foo': u'bar'}


实例：
view:
def  login(request):
	print(request.COOKIES)
	if  request.method  ==  'POST':
	#  Check  that  the  test  cookie  worked  (we  set  it  below):
		if  request.session.test_cookie_worked():
		#  The  test  cookie  worked,  so  delete  it.
			request.session.delete_test_cookie()
            #set session
			request.session['foo']  =  'bar'
			return  HttpResponse("You're  logged  in.")
		else:
			return  HttpResponse("Please  enable  cookies  and  try  again.")
	#  If  we  didn't  post,  send  the  test  cookie  along  with  the  login  form.
	request.session.set_test_cookie()
	return  render_to_response('login.html')

login.html:
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
<form action="/login/" method="post">
    username:<input  type="text" name="username" />
    <input type="submit" value="submit">
</form>
</body>
</html>

执行及确认过程：
get /login/时：
浏览器上返回登录页面，且浏览器中记录的cookie信息如下：
名字：	sessionid
内容：	qk59nrnprklu0lsmldy3ecyc9qfsp3em
域：	127.0.0.1
路径：	/
发送用途：	各种连接
脚本可访问：	否（仅 Http）
创建时间：	2016年6月2日星期四 上午8:39:04
过期时间：	2016年6月16日星期四 上午8:39:04

进入session数据库确认:
python2 manage.py shell
from  django.contrib.sessions.models  import  Session
s=Session.objects.get(pk='qk59nrnprklu0lsmldy3ecyc9qfsp3em') //使用上面的sessionid:
>>> s.session_data
u'ODIwMDE1MDlhYjgyNmNlNzcwZGU2M2YyMDQ5YzZhOWVhMzdkMTgwNTp7InRlc3Rjb29raWUiOiJ3b3JrZWQifQ=='
>>> s.get_decoded()
{u'testcookie': u'worked'}

在前端页面上输入用户名通过post提交后：
视图函数中进行了如下的操作：
request.session.delete_test_cookie()  ##删除数据库中的testcookie
request.session['foo']  =  'bar'  ##写session操作
return  HttpResponse("You're  logged  in.")  ##响应给客户
此时浏览器的cookie信息如下：
名字：	sessionid
内容：	qk59nrnprklu0lsmldy3ecyc9qfsp3em  ##和上面的相同
域：	127.0.0.1
路径：	/
发送用途：	各种连接
脚本可访问：	否（仅 Http）
创建时间：	2016年6月2日星期四 上午8:47:57
过期时间：	2016年6月16日星期四 上午8:47:57

进入session数据库确认:
python2 manage.py shell
from  django.contrib.sessions.models  import  Session
s=Session.objects.get(pk='qk59nrnprklu0lsmldy3ecyc9qfsp3em') //使用上面的sessionid:
>>> s.session_data
u'MjQ0ZWQzNDY0ODNlMzBjNDU3ZDc3OTM5OTRkNjc2ZWNiMmIyMTA4Yzp7ImZvbyI6ImJhciJ9'
>>> s.get_decoded()
{u'foo': u'bar'}  //已经删除了testcookie，并写入了新的数据；


10. 数据表查询相关：
manytomany:
class asset_db(models.Model):
	serverno=models.CharField(max_length=50)
	ip_addr=models.CharField(max_length=50)
	user=models.CharField(max_length=50)
	passwd=models.CharField(max_length=50)
	cpu=models.CharField(max_length=400,null=True,blank=True)
	memory=models.CharField(max_length=400,null=True,blank=True)
	ethernets=models.ManyToManyField(ethernet,null=True,blank=True)
	
class ethernet(models.Model):
	TT=(
	('00','Optical'),
	('01','Electrical'),
	)
	e_model=models.CharField(max_length=50,null=True,blank=True)
	e_sn=models.CharField(max_length=50,null=True,blank=True)
	e_fw=models.CharField(max_length=50,null=True,blank=True)
	e_maker=models.CharField(max_length=50,null=True,blank=True)
	e_portnum=models.CharField(max_length=50,null=True,blank=True)
	e_porttype=models.CharField(max_length=50,null=True,blank=True,choices=TT)
	e_qty=models.CharField(max_length=50,null=True,blank=True)

python2 manage.py shell
from blog.models import *


##从asset_db查ethernet的方法：
>>> ss=asset_db.objects.get(id=1)
>>> ss.user
u'root'
>>> ss.ethernets
<django.db.models.fields.related.ManyRelatedManager object at 0x0000000003B9E1D0>
>>> ss.ethernets.all()  
[<ethernet: i350>]

##从ethernet反查asset_db的方法：
>>> ee=ethernet.objects.get(id=1)
>>> ee.asset_db_set.all()
[<asset_db: r5300g3-8-1>]


foreign key相关：
正向查找：
>>>  b  =  Book.objects.get(id=50)
>>>  b.publisher
<Publisher:  Apress  Publishing>
>>>  b.publisher.website
u'http://www.apress.com/'

反向查找：
>>>  p  =  Publisher.objects.get(name='Apress  Publishing')
>>>  p.book_set.all()
[<Book:  The  Django  Book>,  <Book:  Dive  Into  Python>,  ...]

多对多增加记录的方法：
 
 >>> e1=ethernet.objects.get(id=1)
>>> e1
<ethernet: i350>
>>> s2=asset_db.objects.get(id=2)
>>> s2
<asset_db: r8500g4-1>

>>> s2.ethernets=[e1,]
>>> s2.save()




django  ushell 下调试 数据库：
from blog.models import *
>>> obj=fccard(f_model="11111");     //这么写，因为多了一个“；”，虽然没有报错，数据无法写入数据库，切记；且确认中发现，不光无法写入，还会把最后一条记录删除；
>>> obj.save()
>>> obj=fccard(f_model="11111")
>>> obj.save()



记一次故障调试的信息：
在视图中进行数据库的写入时，一直报下面的错误：
_wrapped_view() takes at least 1 argument (0 given)
但在django shell 中进行调试时，可以正常进行数据库的写入。
我的models中的相关部分的定义如下：
class nvme(models.Model):
	n_model=models.CharField(max_length=50,null=True,blank=True)
	n_sn=models.CharField(max_length=50,null=True,blank=True)
	n_fw=models.CharField(max_length=50,null=True,blank=True)
	n_maker=models.CharField(max_length=50,null=True,blank=True)
	n_qty=models.CharField(max_length=50,null=True,blank=True)
	n_remark=models.CharField(max_length=200,null=True,blank=True)
	n_remark2=models.CharField(max_length=200,null=True,blank=True)
	n_remark3=models.CharField(max_length=200,null=True,blank=True)
	n_remark4=models.CharField(max_length=200,null=True,blank=True)

视图中的代码如下：
				##for nvme:
				try:
					n_list=[]
					restt=result['nvme_info']
					for dd in restt:
						obj=nvme(
						n_model=dd[0],
						n_sn=dd[1],
						n_fw=dd[2],
						n_maker=dd[3],
						n_qty=dd[4],
						)
						n_list.append(obj)
						obj.save()
						print(dd[0])
					line.nvmes=n_list

				except Exception as err:
					print(err)
					err_list.append(err)
排查了好久，没有发现任何问题。
百度了一下，提示可能是视图中定义了和model中类的名称相关的视图函数。
找了一下，果然发现了下面的这个函数：

@login_required
def nvme(request,page,temple):
        page=int(page)
        pages=[x for x in range(1,get_pages(Nvme_ssd_db)+1)]
        end=pages[-1]
        content_list=Nvme_ssd_db.objects.filter()[(page-1)*12:page*12]
        # print page
        # print content_list

        if get_pages(Nvme_ssd_db)>1:
                return render_to_response(temple,{'nvme_info':content_list,'pages':pages,'end':end,'page':page,'errmsg':'OK'})
        else:
                return render_to_response(temple,{'nvme_info':content_list,'pages':pages,'end':end,'errmsg':'faile'})
@@这真的是编程不规范引发的血的教训呀。
以后建议，对models中的类和 views中的视图函数采用两套完全不同的命名规则，来避免类似的问题再次发生（！！！！切记）



django更新数据库字段的方法：
增加字段：
step1: 在models.py中新增字段；
class Disk_resource(models.Model):
	Model=models.CharField(max_length=80)
	inch=models.CharField(max_length=30)
	Qty=models.CharField(max_length=30)
	BOX_NO=models.CharField(max_length=30)
	Capacity=models.CharField(max_length=30)
	Interface=models.CharField(max_length=30)
	remark=models.CharField(max_length=30)  //为新增字段

step2:执行 python  manage.py  sqlall  [yourapp]  来测试模型新的  CREATE  TABLE  语句。  注意为新字段的列定义。

C:\Users\Administrator\Desktop\python_related_data\zhl_working_directory\server>python27 manage.py sqlall blog
//下面只截取我们修改的这个表的那个字段；

BEGIN;
CREATE TABLE `blog_disk_resource` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `Model` varchar(80) NOT NULL,
    `inch` varchar(30) NOT NULL,
    `Qty` varchar(30) NOT NULL,
    `BOX_NO` varchar(30) NOT NULL,
    `Capacity` varchar(30) NOT NULL,
    `Interface` varchar(30) NOT NULL,
    `remark` varchar(30) NOT NULL
)


step3:然后运行 python27 manage.py dbshell  连接数据库客户端，执行mysql 命令更新数据库的对应字段：
mysql> alter table blog_disk_resource add column remark varchar(100);   //参考上面python27 manage.py sqlall blog中的信息，执行对应的数据库修改命令
Query OK, 72 rows affected (0.03 sec)

mysql> use mydb;
Database changed


mysql> desc blog_disk_resource;
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int(11)      | NO   | PRI | NULL    | auto_increment |
| Model     | varchar(80)  | NO   |     | NULL    |                |
| inch      | varchar(30)  | NO   |     | NULL    |                |
| Qty       | varchar(30)  | NO   |     | NULL    |                |
| BOX_NO    | varchar(30)  | NO   |     | NULL    |                |
| Capacity  | char(30)     | YES  |     | NULL    |                |
| Interface | char(30)     | YES  |     | NULL    |                |
| remark    | varchar(100) | YES  |     | NULL    |                |  //修改后确认已经增加了
+-----------+--------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)


注意： //待验证；
添加非空字段需要执行下面的命令：
alter table blog_disk_resource add column remark varchar(100);
update blog_disk_resource set remark=None;
alter table blog_disk_resource alter column remark SET  NOT  NULL;



删除字段：
从 Model 中删除一个字段要比添加容易得多。  删除字段，仅仅只要以下几个步骤：

1）删除models中的字段，然后重新启动你的 web 服务器。
2）用以下命令从数据库中删除字段：	
ALTER  TABLE  books_book  DROP  COLUMN  num_pages;

请保证操作的顺序正确。  如果你先从数据库中删除字段，Django 将会立即抛出异常。			


删除多对多关联字段  //@@重要： 关联字段对应的就是数据库中管理表；
由于多对多关联字段不同于普通字段，所以删除操作是不同的。

1）从你的模型中删除 ManyToManyField，然后重启 web 服务器。
2）用下面的命令从数据库删除关联表：
DROP  TABLE  books_book_authors;
像上面一样，注意操作的顺序。

删除模型
删除整个模型要比删除一个字段容易。  删除一个模型只要以下几个步骤：

1）从文件中删除你想要删除的模型，然后重启 web  服务器 models.py
2）然后用以下命令从数据库中删除表：			
DROP  TABLE  books_book;
当你需要从数据库中删除任何有依赖的表时要注意（也就是任何与表 books_book 有外键的表  ）。
正如在前面部分，一定要按这样的顺序做。



			
			
				
