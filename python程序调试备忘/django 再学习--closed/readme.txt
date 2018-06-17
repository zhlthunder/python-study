1.urlƥ��ģʽ˵����
  url(r'^test1/\d{2}/$', test1),   ����ƥ�䷽ʽ1�����ַ�ʽ����Ҫ����������̨����̨��ͼ����ֻ��һ��request������
  url(r'^test2/(?P<id>\d{2})/$', test2), ����ƥ�䷽ʽ2��ʹ������������ķ�ʽ����Ҫ���̨�������ݣ�id=\d{2}�����Һ�̨��ͼ�����������һ������Ϊid�Ĳ���������ᱨ��
      url(r'^test3/(\d{2})/$', test3),   ����ƥ�䷽ʽ3��ʹ��������������ķ�ʽ����Ҫ���̨�������ݣ�\d{2}�����Һ�̨��ͼ������Ҫ����һ������������ǰ�η��͹��������ݣ������������⣻
	  
2.djago�����Ķ���
����ʱ�䣬�����ͨ������һ����ȫ���(full populated)���ֵ��  Context()  ����ʼ��  ������(Context)  ��
���ǳ�ʼ���Ժ���Ҳ����ʹ�ñ�׼�� Python �ֵ��﷨(syntax)��``������(Context)``  ������ӻ���ɾ����Ŀ:

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

3.������
������ǰ���ᵽ��һ����ģ����������ڱ�������ʾǰ�޸�����ֵ��һ���򵥷�����  ������ʹ�ùܵ��ַ�
{{  name|lower  }} ��������ת���ı�ΪСд
{{  my_list|first|upper  }} �����б�ĵ�һ��Ԫ�ز�����ת��Ϊ��д

��Щ�������в�����  �������Ĳ�������ð��֮����������˫���Ű���
{{  bio|truncatewords:"5"  }} �������ʾ����  bio  ��ǰ 5����  //��֤���ɹ������Ų�

4. settings.py��ģ���ļ�·�����ã�
ʹ�þ���·���ķ�ʽ��
Ĭ������app/templates��Ѱ��ģ�壬��������������ط�����Ҫ��settings.py�������µ����á�
TEMPLATE_DIRS  =  (
'/home/django/mysite/templates',  //�����windows����Ҫ��\ -->/
)
Python  Ҫ��Ԫ��Ԫ���б���ʹ�ö��ţ��Դ�������Բ���ű��ʽ֮������塣  �������ֳ����Ĵ���
���ʹ�õ���  Windows  ƽ̨����������������Ų�ʹ�� Unix ����б�ܣ�/�������Ƿ�б�ܣ�\��

�������÷�����
TEMPLATE_DIRS  =  (
    os.path.join(os.path.dirname(os.path.dirname(__file__)),  'templates').replace('\\','/'),
)

 Python  �ڲ�����  __file__  ���ñ������Զ�����Ϊ�������ڵ�  Python  ģ���ļ�
����  `` os.path.dirname(os.path.dirname(__file__))``  �����ȡ�������ڵ��ļ����� settings.py  ���ڵ�Ŀ¼����һ��Ŀ¼��
Ȼ����
os.path.join  �����������Ŀ¼��  templates  �������ӡ������ windows �£��������ܵ�ѡ����ȷ�ĺ���б
�ܡ����������ӣ�������ǰ��б�ܡ�/��


5.locals()  ����
����
���ص��ֵ�����оֲ�������������ֵ����ӳ��
return  render_to_response('current_datetime.html',  locals())
ʹ��  locals()  ʱҪע������������ ����  �ľֲ����������ǿ��ܱ�������ģ����ʵ�Ҫ�ࡣ

6. ģ���ļ��ֲ㴦��
return  render_to_response('dateapp/current_datetime.html',  {'current_date':  now})
����Ŀ¼�������û�����ƣ�����Ҫ���ٲ㶼���ԡ�  ֻҪ��ϲ�����ö��ٲ����Ŀ¼������ν��


7.  forms
����֤ʱ�����û��ύ�ı���������ʱ�����Խ��Ѿ���ȷ���ֶη��ص�ǰ�� �����ӣ�
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

�⿴�������ң���д��ʱ�����׳��� ϣ���㿪ʼ����ʹ�ø߼�������⡪��������������У����
��

��һ�� Form ��
Django ����һ�� form �⣬��Ϊ django.forms���������Դ������Ǳ������ᵽ�İ��� HTML ����ʾ
�Լ���֤��

f  =  ContactForm({'subject':  'Hello',  'email':  'adrian@example.com',  'message':  'Nice  site!'})  //formʵ�帳ֵ
>>>  f.is_bound
True
�����κΰ� form �� is_valid()�������Ϳ���֪�����������Ƿ�Ϸ���  �����Ѿ�Ϊÿ���ֶδ�����ֵ��
������� Form �ǺϷ��ģ�
>>>  f.is_valid()
True

�������һ�鿴ÿ���ֶεĳ�����Ϣ��
>>>  f  =  ContactForm({'subject':  'Hello',  'message':  ''})
>>>  f['message'].errors
[u'This  field  is  required.']
>>>  f['subject'].errors
[]
>>>  f['email'].errors
[]
��ע��ÿһ��� Form ʵ�嶼��һ�� errors ���ԣ���Ϊ���ṩ��һ���ֶ��������Ϣ��ӳ����ֵ��

���գ����һ�� Form ʵ��������ǺϷ��ģ����ͻ���һ�����õ� cleaned_data ���ԡ� ����һ�������ɾ���
�ύ���ݵ��ֵ䡣 Django �� form ��ܲ���У�����ݣ������������ת������Ӧ�� Python �������ݣ������
�������ݡ�

>>> obj=ContactForm({'subject':"asdfasd",'message':'asdfasfdasfd'})
>>> obj.is_valid()
True
>>> obj.cleaned_data
{'message': u'asdfasfdasfd', 'email': u'', 'subject': u'asdfasd'}

8.ģ�壺
context  ��һ�����ݸ�ģ������Ƶ�ֵ��ӳ�䣨���� Python �ֵ䣩��
ģ�� ��Ⱦ  ������ͨ���� context ��ȡֵ���滻ģ���б�����ִ�����е�ģ���ǩ��

RequestContext �� Context ������
����Ҫһ�� context ������ģ�塣һ������£�����һ��  django.template.Context  ��ʵ���������� Django
�л�������һ����������࣬django.template.RequestContext  �������������΢��Щ��ͬ�� RequestContext  Ĭ
�ϵ���ģ�� context �м�����һЩ��������  HttpRequest  �����ǰ��¼�û��������Ϣ��
���㲻����һϵ��ģ���ж���ȷָ��һЩ��ͬ�ı���ʱ����Ӧ��ʹ��  RequestContext  


django.core.context_processors.debug��
���ڵ�����Ϣ�Ƚ����У�������� context ������ֻ�е�ͬʱ������������������ʱ�����Ч��
?   DEBUG  ��������Ϊ  True  ��
?  ����� ip Ӧ�ð�����  INTERNAL_IPS  ���������档


9. �Ự���û���ע�᣺
cookie& session�Աȣ�
��ͬ�㣺
���߶���Ҫ����cookie�Ļ�����ͻ��˷�����Ϣ��
�ڷ������ˣ��û�����Ч��Ϣ���洢�����ݿ��У�

���� 
session �Ļ�����Ը�����һЩ�����Դ洢�û��ڷ������˵����в��������繺������ȵȣ������еĿͻ����ݶ��洢�ڷ������ˣ�ֻ�ǰ����ݵĹ�ϣ�ỰIDͨ��cookie���͵��ͻ��ˣ�
cookie ��ʵ����Լ򵥣�ֻ֧�ּ򵥵����ã������õ����ݻᱻ���͵��ͻ���

cookie:
 cookies  �������Ϊ  Web  �������洢��һС����Ϣ��  ÿ���������ĳ������������ҳ
��ʱ���������������֮ǰ�յ��� cookies

����  Cookies  ��ֵ����� Google���������Щʱ����ʹ� Google ��վ���ˡ�  ���ֵ���������ݿ��д�
���û���Ϣ�� key������������ҳ������ʾ����û�����  Google �ᣨ�Լ�Ŀǰ��ʹ��������ҳ����ʾ���˺�
���û�����


ʵ����
def  set_color(request):
	if  "favorite_color"  in  request.GET:
		response  =  HttpResponse("Your  favorite  color  is  now  %s"  % request.GET["favorite_color"])
		response.set_cookie("favorite_color",request.GET["favorite_color"])
		return  response
	else:
		return  HttpResponse("You  didn't  give  a  favorite  color.")
��������������������ݣ��ύget���󵽷������ˣ���Я��favorite_color �ֶΣ�
http://127.0.0.1:8000/set_color/?favorite_color=zzzzz  
���ص���Ӧ��Ϣ�� Your favorite color is now zzzzz

���������cookie�м�¼���µ���Ϣ��
���֣�	favorite_color
���ݣ�	zzzzz
��	127.0.0.1
·����	/
������;��	��������
�ű��ɷ��ʣ�	��
����ʱ�䣺	2016��6��2�������� ����8:21:31
����ʱ�䣺	����Ự����ʱ


Session:
Django ��  Session  ���
���ڴ��ڵ������밲ȫ©����cookies �ͳ����ԻỰ�Ѿ���Ϊ Web ����������ͷ�۵ĵ䷶�� ����Ϣ�ǣ�
Django ��Ŀ�����Ǹ�Ч�ġ�ͷ��ɱ�֡������Դ��� session ��ܻ����㶨��Щ���⡣
������� session  �������ȡÿ���������������ݣ�  ��Щ�����ڷ������˴洢������ cookie ���շ���
���˳���  Cookies ֻ�洢���ݵĹ�ϣ�Ự ID�����������ݱ����Ӷ������˴󲿷ֵĳ��� cookie ���⡣


���ڲ�������ÿ�� session ��ֻ��һ����ͨ�� Django model����  django.contrib.sessions.models  ��
����)��ÿ�� session ����һ������� 32 �ֽڹ�ϣ������ʶ�����洢�� cookie �С�  ��Ϊ����һ����׼��
ģ�ͣ����������ʹ�� Django ���ݿ� API ����ȡ session��
##ʹ������������cookie�ڷ����������ݿ��²�ѯ������Ϣ��
>>> s=Session.objects.get(pk='7sxh301z7ymsbcsz6rpkmuqfvwttlui7')  ##���ǿͻ���������л�ȡ����sessionid
>>> s.expire_date
datetime.datetime(2016, 6, 15, 8, 19, 36, tzinfo=<UTC>)
>>> s.session_data
u'OGRlMDU2N2NhNDdkZTYxYmZjODY0OTIzZjk5NGI4ZDMyODQyNDkxZDp7fQ=='
>>> s.get_decoded()
{}  //��ʱû�д洢session���ݣ�

ȱʡ������£�Django ֻ���� session �����仯��ʱ��Ż�������ݿ⣬����˵���ֵ丳ֵ��ɾ����

����ͼ������ִ�У�
request.session['foo']  =  'bar' �� ��
���µ�¼������ģʽ���ٴ� ��ѯ������Ϣ��>>> from django.contrib.sessions.models import Session
>>> s=Session.objects.get(pk='7sxh301z7ymsbcsz6rpkmuqfvwttlui7')
>>> s.session_data
u'MjQ0ZWQzNDY0ODNlMzBjNDU3ZDc3OTM5OTRkNjc2ZWNiMmIyMTA4Yzp7ImZvbyI6ImJhciJ9'
>>> s.get_decoded()
{u'foo': u'bar'}


ʵ����
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

ִ�м�ȷ�Ϲ��̣�
get /login/ʱ��
������Ϸ��ص�¼ҳ�棬��������м�¼��cookie��Ϣ���£�
���֣�	sessionid
���ݣ�	qk59nrnprklu0lsmldy3ecyc9qfsp3em
��	127.0.0.1
·����	/
������;��	��������
�ű��ɷ��ʣ�	�񣨽� Http��
����ʱ�䣺	2016��6��2�������� ����8:39:04
����ʱ�䣺	2016��6��16�������� ����8:39:04

����session���ݿ�ȷ��:
python2 manage.py shell
from  django.contrib.sessions.models  import  Session
s=Session.objects.get(pk='qk59nrnprklu0lsmldy3ecyc9qfsp3em') //ʹ�������sessionid:
>>> s.session_data
u'ODIwMDE1MDlhYjgyNmNlNzcwZGU2M2YyMDQ5YzZhOWVhMzdkMTgwNTp7InRlc3Rjb29raWUiOiJ3b3JrZWQifQ=='
>>> s.get_decoded()
{u'testcookie': u'worked'}

��ǰ��ҳ���������û���ͨ��post�ύ��
��ͼ�����н��������µĲ�����
request.session.delete_test_cookie()  ##ɾ�����ݿ��е�testcookie
request.session['foo']  =  'bar'  ##дsession����
return  HttpResponse("You're  logged  in.")  ##��Ӧ���ͻ�
��ʱ�������cookie��Ϣ���£�
���֣�	sessionid
���ݣ�	qk59nrnprklu0lsmldy3ecyc9qfsp3em  ##���������ͬ
��	127.0.0.1
·����	/
������;��	��������
�ű��ɷ��ʣ�	�񣨽� Http��
����ʱ�䣺	2016��6��2�������� ����8:47:57
����ʱ�䣺	2016��6��16�������� ����8:47:57

����session���ݿ�ȷ��:
python2 manage.py shell
from  django.contrib.sessions.models  import  Session
s=Session.objects.get(pk='qk59nrnprklu0lsmldy3ecyc9qfsp3em') //ʹ�������sessionid:
>>> s.session_data
u'MjQ0ZWQzNDY0ODNlMzBjNDU3ZDc3OTM5OTRkNjc2ZWNiMmIyMTA4Yzp7ImZvbyI6ImJhciJ9'
>>> s.get_decoded()
{u'foo': u'bar'}  //�Ѿ�ɾ����testcookie����д�����µ����ݣ�


10. ���ݱ��ѯ��أ�
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


##��asset_db��ethernet�ķ�����
>>> ss=asset_db.objects.get(id=1)
>>> ss.user
u'root'
>>> ss.ethernets
<django.db.models.fields.related.ManyRelatedManager object at 0x0000000003B9E1D0>
>>> ss.ethernets.all()  
[<ethernet: i350>]

##��ethernet����asset_db�ķ�����
>>> ee=ethernet.objects.get(id=1)
>>> ee.asset_db_set.all()
[<asset_db: r5300g3-8-1>]


foreign key��أ�
������ң�
>>>  b  =  Book.objects.get(id=50)
>>>  b.publisher
<Publisher:  Apress  Publishing>
>>>  b.publisher.website
u'http://www.apress.com/'

������ң�
>>>  p  =  Publisher.objects.get(name='Apress  Publishing')
>>>  p.book_set.all()
[<Book:  The  Django  Book>,  <Book:  Dive  Into  Python>,  ...]

��Զ����Ӽ�¼�ķ�����
 
 >>> e1=ethernet.objects.get(id=1)
>>> e1
<ethernet: i350>
>>> s2=asset_db.objects.get(id=2)
>>> s2
<asset_db: r8500g4-1>

>>> s2.ethernets=[e1,]
>>> s2.save()




django  ushell �µ��� ���ݿ⣺
from blog.models import *
>>> obj=fccard(f_model="11111");     //��ôд����Ϊ����һ������������Ȼû�б��������޷�д�����ݿ⣬�мǣ���ȷ���з��֣������޷�д�룬��������һ����¼ɾ����
>>> obj.save()
>>> obj=fccard(f_model="11111")
>>> obj.save()



��һ�ι��ϵ��Ե���Ϣ��
����ͼ�н������ݿ��д��ʱ��һֱ������Ĵ���
_wrapped_view() takes at least 1 argument (0 given)
����django shell �н��е���ʱ�����������������ݿ��д�롣
�ҵ�models�е���ز��ֵĶ������£�
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

��ͼ�еĴ������£�
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
�Ų��˺þã�û�з����κ����⡣
�ٶ���һ�£���ʾ��������ͼ�ж����˺�model�����������ص���ͼ������
����һ�£���Ȼ��������������������

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
@@������Ǳ�̲��淶������Ѫ�Ľ�ѵѽ��
�Ժ��飬��models�е���� views�е���ͼ��������������ȫ��ͬ�������������������Ƶ������ٴη��������������мǣ�



django�������ݿ��ֶεķ�����
�����ֶΣ�
step1: ��models.py�������ֶΣ�
class Disk_resource(models.Model):
	Model=models.CharField(max_length=80)
	inch=models.CharField(max_length=30)
	Qty=models.CharField(max_length=30)
	BOX_NO=models.CharField(max_length=30)
	Capacity=models.CharField(max_length=30)
	Interface=models.CharField(max_length=30)
	remark=models.CharField(max_length=30)  //Ϊ�����ֶ�

step2:ִ�� python  manage.py  sqlall  [yourapp]  ������ģ���µ�  CREATE  TABLE  ��䡣  ע��Ϊ���ֶε��ж��塣

C:\Users\Administrator\Desktop\python_related_data\zhl_working_directory\server>python27 manage.py sqlall blog
//����ֻ��ȡ�����޸ĵ��������Ǹ��ֶΣ�

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


step3:Ȼ������ python27 manage.py dbshell  �������ݿ�ͻ��ˣ�ִ��mysql ����������ݿ�Ķ�Ӧ�ֶΣ�
mysql> alter table blog_disk_resource add column remark varchar(100);   //�ο�����python27 manage.py sqlall blog�е���Ϣ��ִ�ж�Ӧ�����ݿ��޸�����
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
| remark    | varchar(100) | YES  |     | NULL    |                |  //�޸ĺ�ȷ���Ѿ�������
+-----------+--------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)


ע�⣺ //����֤��
��ӷǿ��ֶ���Ҫִ����������
alter table blog_disk_resource add column remark varchar(100);
update blog_disk_resource set remark=None;
alter table blog_disk_resource alter column remark SET  NOT  NULL;



ɾ���ֶΣ�
�� Model ��ɾ��һ���ֶ�Ҫ��������׵öࡣ  ɾ���ֶΣ�����ֻҪ���¼������裺

1��ɾ��models�е��ֶΣ�Ȼ������������� web ��������
2����������������ݿ���ɾ���ֶΣ�	
ALTER  TABLE  books_book  DROP  COLUMN  num_pages;

�뱣֤������˳����ȷ��  ������ȴ����ݿ���ɾ���ֶΣ�Django ���������׳��쳣��			


ɾ����Զ�����ֶ�  //@@��Ҫ�� �����ֶζ�Ӧ�ľ������ݿ��й����
���ڶ�Զ�����ֶβ�ͬ����ͨ�ֶΣ�����ɾ�������ǲ�ͬ�ġ�

1�������ģ����ɾ�� ManyToManyField��Ȼ������ web ��������
2�����������������ݿ�ɾ��������
DROP  TABLE  books_book_authors;
������һ����ע�������˳��

ɾ��ģ��
ɾ������ģ��Ҫ��ɾ��һ���ֶ����ס�  ɾ��һ��ģ��ֻҪ���¼������裺

1�����ļ���ɾ������Ҫɾ����ģ�ͣ�Ȼ������ web  ������ models.py
2��Ȼ����������������ݿ���ɾ����			
DROP  TABLE  books_book;
������Ҫ�����ݿ���ɾ���κ��������ı�ʱҪע�⣨Ҳ�����κ���� books_book ������ı�  ����
������ǰ�沿�֣�һ��Ҫ��������˳������



			
			
				
