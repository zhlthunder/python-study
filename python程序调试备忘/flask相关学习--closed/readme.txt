1. ģ��̳��У�block�������в����зǷ��ַ����������£�  �����ֵ�Ҫ�󣺾�������ĸ�����֣��»�������ɣ�
{% block page-content %} 
����ʱ��ʾ�Ĵ���jinja2.exceptions.TemplateSyntaxError: Block names in Jinja have to be valid Python identifiers and may not contain hyphens, use an underscore instead.

######################################################################
2. ����2��AttributeError: type object 'Asset_db2Cpu' has no attribute 'foreign_keys'
  �����������������м���йأ�
  Ҫ��1. �м��������� �������벻��ͬ�� ���ֻ�Ǵ�Сд��ͬ���д���
  
  class asset_db2_cpu(db.Model):
    __tablename__ = 'asset_db2cpu'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    asset_db_id=db.Column(db.Integer,db.ForeignKey('asset_db.id'))
    cpu_id=db.Column(db.Integer,db.ForeignKey('cpu.id'))

	2.secondary='asset_db2cpu' ������ʱ����Ҫʹ�ñ������ַ��������ʹ�����������м�
	cpus=db.relationship('Cpu',secondary='asset_db2cpu',backref='asset_dbs')
	

���������˵����ʹ�õ�ʵ�����£�
from . import db


class Class2student(db.Model):
    __tablename__="class2student"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    class_id=db.Column(db.Integer,db.ForeignKey("class.id"))
    student_id=db.Column(db.Integer,db.ForeignKey("student.id"))


class Student(db.Model):
    __tablename__="student"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),nullable=True)
    age=db.Column(db.String(100),nullable=True)

    def __repr__(self):
        return "<strund %r>"%self.name

class Class(db.Model):
    __tablename__="class"   ##�����ͱ���һ��Ҫ���ֿ�
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),nullable=True)
    floor=db.Column(db.String(100),nullable=True)

    students=db.relationship("Student",secondary="class2student",backref=db.backref("classs",lazy="dynamic"),lazy="dynamic")
	##����ʱ������ࣺ
	 ��һ����������Ʋ��Ǳ�����ƣ�����"Student"�����д��"student"�ͻᱨ��
	 �ڶ������м��ı�����Ʋ���������ƣ�����"class2student"�������ǡ�Class2student����
	 �����ܽ᣺  sqlalchemy ���������ݱ�������������ݱ���д������һֱ��������������������������ɵģ��мǣ�
	 
	 
	
######################################################################	
3.������Ϣ��//django��flaskһ��������
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd4 in position 101: invalid continuation byte
����������
��baseģ����������ʱ����������ʾ����ģ��ͨ��extends�̳к������������ʱ�ͻ���ʾ�쳣��������Ĵ���
��ʹ����ģ��Ŀ�ͷ���� ��<meta charset="utf-8">��Ҳ������ʾ�쳣��

ԭ�򣺾����Ų��������ȷʵ���ļ��ı����ʽ�����⣬����ȷ��Ҫ��ʾ�����HTML�ļ������ĸ�ʽ��ANSI���޸ĳ�UTF-8 without BOM ���������⣬
�Ʋ�����Ŀ�е������ļ�û��ʹ��UTF-8�ĸ�ʽ��ԭ�򣬽����е��ļ����޸�ΪUTF-8�ĸ�ʽ������ͽ���ˣ��мǡ�����ס����������е��ļ����ĳ�utf-8�ĸ�ʽ�ſ��Ա���������⣩

��������Բߣ���pycharm�� �ļ�--����--�ļ�����--����IDE encoding,project encoding,�ļ�Ĭ�ϱ��� ������ΪUTF-8�ĸ�ʽ�༭��ԭ��
�������Ŀ�е��ļ��Ǵӱ�ĵط����������ģ���Ҫ��Ŀ¼���� Ϊÿ���ļ��ֶ�ָ�������ʽ�ſ��ԣ��мǣ�����
  
  �ر��ע����ʱ���Կ�����Ŀ¼���е��ļ����е���ʾ����encoding is hard coded in the text��, ��Ϊ�ļ��Ŀ�ͷ�����ˣ�# -*- coding: utf-8 -*-
   ��ʱɾ��# -*- coding: utf-8 -*- �� ��ȥ�鿴���ļ��ĸ�ʽ���ǿհ׵��ˡ���@@@@@��
  
######################################################################
4. flaskǰ�˰��� bootstrap�ķ�����	 ����static�� templates ����ͬ��Ŀ¼
<link href="{{ url_for('static',filename='css/bootstrap.css') }}" rel="stylesheet">
<link href="{{ url_for('static',filename='css/bootstrap-responsive.css') }}" rel="stylesheet">
<script src="{{ url_for('static',filename='js/jquery.min.js') }}"></script>
<script src="{{ url_for('static',filename='js/bootstrap.js') }}"></script>

######################################################################
5.
flask sqlalchemy ģ����ѯ��
ss=db.session.query(models.Asset_db).filter(models.Asset_db.serverno.ilike('%'+tt+'%')).all()

ͨ��flask���߽ű��������ݿ⣺

######################################################################
6. api�ӿڵ��ԣ�
��ʹ�ã�
get �ķ�����


import urllib2
res=urllib2.urlopen('http://128.1.2.250')
data=res.read()
print(data)

http�ǻ��������Ӧ����Ƶģ��ͻ���������󣬷�����ṩ��Ӧ��
urllib2��һ��request������ӳ���������http�����������Ӧ���ǣ�
����Ҫ����ĵ�ַ����һ��request����ͨ������urlopen������request���󣬽�����һ����������response����
>>> import urllib2
>>> req=urllib2.Request("http://128.1.2.250")
>>> res=urllib2.urlopen(req)
data=res.read()
print(data)



post��
[root@R5300G4-12-001 client_collect]# cat test.py 
#!/usr/bin/python
import urllib2,json

data={"ip_addr": "7.4.4.5"}
url="http://128.1.2.250/asset/api/v1.0/r57005577/update"

ddata=json.dumps(data)
header_dict={'Content-Type':"application/json"}
req = urllib2.Request(url=url,data=ddata,headers=header_dict)
res_data = urllib2.urlopen(req)
callback=res_data.read()
print(callback)


����ʱһֱ�������£������Ų��Ƿ������˵����⡣
[root@R5300G4-12-001 client_collect]# python test.py 
Traceback (most recent call last):
  File "test.py", line 10, in <module>
    res_data = urllib2.urlopen(req)
  File "urllib2.py", line 126, in urlopen
    
  File "urllib2.py", line 397, in open
    def close(self):
  File "urllib2.py", line 510, in http_response
    
  File "urllib2.py", line 435, in error
    for processor in self.process_response.get(protocol, []):
  File "urllib2.py", line 369, in _call_chain
    kind = int(kind)
  File "urllib2.py", line 518, in http_error_default
    return opener
urllib2.HTTPError: HTTP Error 500: INTERNAL SERVER ERROR
######################################################################

http����ʵ�ֵļ��ַ����ĶԱ����£�
##ͨ��pythonģ��ʵ��http����ķ���
#ʹ��urllibģ��
# 1.�򵥵�get����
# import urllib.request
# data=urllib.request.urlopen("http://128.1.2.250/asset_db_show/").read().decode('utf-8','ignore')
# print(data)

#2.ͨ��Request()����������ķ�ʽ��
# import urllib.request
# req=urllib.request.Request("http://128.1.2.250/asset_db_show/")
# data=urllib.request.urlopen(req).read().decode('utf-8')
# print(data)


#3.��������get����
# import urllib.request
# key="����"
# key=urllib.request.quote(key) ##����ؼ��������ģ�����Ҫ�����������
# url='http://www.baidu.com/s?wd='+key
# data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
# print(data)

#4.post����
# import  urllib.request
# import urllib.parse
# posturl='http://www.baidu.com/mypost'
# postdata=urllib.parse.urlencode({
#     'name':'jack',
#     'pass':'123'
# }).encode('utf-8')
# req=urllib.request.Request(posturl,postdata) ##��װ������� ����ͨ������ķ�������������
# data=urllib.request.urlopen(req).read().decode("utf-8")
# print(data)


#ʹ��urllib2ģ��, with python2.7
# 1.get����
# import urllib2
# data=urllib2.urlopen('http://128.1.2.250/asset_db_show/').read()
# print(data)

#2. get������ʹ�ö���
# import urllib2
# req=urllib2.Request('http://128.1.2.250/asset_db_show/')
# data=urllib2.urlopen(req).read()
# print(data)

#3.post����
# import urllib2,json
# data={"ip_addr": "7.4.4.5"}
# url="http://128.1.2.250/asset/api/v1.0/r57005577/update"
# ddata=json.dumps(data)
# header_dict={'Content-Type':"application/json"}
# req = urllib2.Request(url=url,data=ddata,headers=header_dict)
# res_data = urllib2.urlopen(req).read()
# print(res_data)

#�ܽ᣺ urlib��urlib2�����𣺿��Լ���Ϊ�ǣ���urlib.request ��װ�� urlib2



######################################################################
��סһ���������Ұ���Ĺ��ϣ�
[root@R5300G4-12-001 ~]# cat test.py 
#!/usr/bin/python

list=[]
mm={}
for i in range(0,10):
        mm['key']=i
        list.append(mm)
        print(mm)
        print(list)

for i in list:
        print(id(i))
		
ִ�н����
[root@R5300G4-12-001 ~]# python test.py 
{'key': 0}
[{'key': 0}]
{'key': 1}
[{'key': 1}, {'key': 1}]
{'key': 2}
[{'key': 2}, {'key': 2}, {'key': 2}]
{'key': 3}
[{'key': 3}, {'key': 3}, {'key': 3}, {'key': 3}]
{'key': 4}
[{'key': 4}, {'key': 4}, {'key': 4}, {'key': 4}, {'key': 4}]
{'key': 5}
[{'key': 5}, {'key': 5}, {'key': 5}, {'key': 5}, {'key': 5}, {'key': 5}]
{'key': 6}
[{'key': 6}, {'key': 6}, {'key': 6}, {'key': 6}, {'key': 6}, {'key': 6}, {'key': 6}]
{'key': 7}
[{'key': 7}, {'key': 7}, {'key': 7}, {'key': 7}, {'key': 7}, {'key': 7}, {'key': 7}, {'key': 7}]
{'key': 8}
[{'key': 8}, {'key': 8}, {'key': 8}, {'key': 8}, {'key': 8}, {'key': 8}, {'key': 8}, {'key': 8}, {'key': 8}]
{'key': 9}
[{'key': 9}, {'key': 9}, {'key': 9}, {'key': 9}, {'key': 9}, {'key': 9}, {'key': 9}, {'key': 9}, {'key': 9}, {'key': 9}]
8491456
8491456
8491456
8491456
8491456
8491456
8491456
8491456
8491456
8491456

����취��
[root@R5300G4-12-001 ~]# cat test.py 
#!/usr/bin/python
import copy
list=[]
mm={}
for i in range(0,10):
        mm['key']=i
        temp=copy.deepcopy(mm)
        list.append(temp)
        print(temp)
        print(list)

�����
[root@R5300G4-12-001 ~]# python test.py 
{'key': 0}
[{'key': 0}]
{'key': 1}
[{'key': 0}, {'key': 1}]
{'key': 2}
[{'key': 0}, {'key': 1}, {'key': 2}]
{'key': 3}
[{'key': 0}, {'key': 1}, {'key': 2}, {'key': 3}]
{'key': 4}
[{'key': 0}, {'key': 1}, {'key': 2}, {'key': 3}, {'key': 4}]
{'key': 5}
[{'key': 0}, {'key': 1}, {'key': 2}, {'key': 3}, {'key': 4}, {'key': 5}]
{'key': 6}
[{'key': 0}, {'key': 1}, {'key': 2}, {'key': 3}, {'key': 4}, {'key': 5}, {'key': 6}]
{'key': 7}
[{'key': 0}, {'key': 1}, {'key': 2}, {'key': 3}, {'key': 4}, {'key': 5}, {'key': 6}, {'key': 7}]
{'key': 8}
[{'key': 0}, {'key': 1}, {'key': 2}, {'key': 3}, {'key': 4}, {'key': 5}, {'key': 6}, {'key': 7}, {'key': 8}]
{'key': 9}
[{'key': 0}, {'key': 1}, {'key': 2}, {'key': 3}, {'key': 4}, {'key': 5}, {'key': 6}, {'key': 7}, {'key': 8}, {'key': 9}]

######################################################################
���߳�lock��ʹ�÷�����
import threading
lock=threading.Lock()
lock.acquire()
�������
lock.release()
######################################################################

######################################################################
@@mysql ���ݿ�������أ�
   mysql���ݿ�ĵ����͵��룺
   
   �����������ݿ⣺ mysqldump -u root -p mydb > mydb.sql     
   �����������ݿ⣺�ȴ���һ��ͬ�������ݿ⣬����mydb;  create database mydb;
                   use mydb;
                   source C:\cmdb\client\mydb.sql   #�����Ϳ�����ɵ�����



   �������ݱ� mysqldump -u root -p mydb blog_disk_info > blog_disk_info.sql
   �������ݱ���һ̨�µ�mysql�������ϣ�myslq -uroot ��½��
   �������ݿ⣺create database mydb;
�� use mydb��Ȼ��ִ�У�
   mysql> source /home/nn/blog_disk_info.sql   //�͵������ݿ����������
######################################################################   
   
######################################################################   
mysql���ݿ����������ʾ�����⣺ 
   1.alter table blog_asset_db default charset utf8;  �޸����ݿ��  ==��alter table blog_cpu default character set utf8 collate utf8_bin;
   2.alter database mydb default character set utf8 collate utf8_general_ci; �޸����ݿ�
   3.mysql> ALTER TABLE `blog_cpu` CHANGE `cpu_model` `cpu_model` VARCHAR(100) CHARACTER SET utf8 NULL;  �޸��ֶΣ�
Query OK, 14 rows affected (0.04 sec)
   
 4.  mysql> show variables like 'character%';   //��������ʽ���������£���ʾ ok
+--------------------------+--------------------------+
| Variable_name            | Value                    |
+--------------------------+--------------------------+
| character_set_client     | utf8                     |
| character_set_connection | utf8                     |
| character_set_database   | utf8                     |
| character_set_filesystem | binary                   |

| character_set_results    | utf8                     |
| character_set_server     | utf8                     |
| character_set_system     | utf8                     |
| character_sets_dir       | C:\mysql\share\charsets\ |
+--------------------------+--------------------------+
8 rows in set, 1 warning (0.01 sec)

mysql> set character_set_database=utf8; //�������Ҫ�޸ĵģ�ʹ����������ÿһ������޸ļ���
Query OK, 0 rows affected, 1 warning (0.00 sec)

�ܽ᣺ ���������Ĳ��������ݿ�ı����ʽ���޸ĺ󣬲ſ�����mysql�в������ģ����м�@@@@@��
mysql> insert into blog_cpu(cpu_model) value("����");
Query OK, 1 row affected (0.00 sec)

�ܽ�2��������֤������������޸ĺ�django����ͼ��ǰ�˲������κ��޸ľͿ���ֱ��֧���������벢д�����ݿ��У�
		task=request.POST.get('task')
		print(task)
		print(type(task))
		asset_db.objects.filter(serverno=serversn).update(serverno=serverno,ip_addr=ip,user=user,passwd=passwd,status='Online',owner=owner,remark2=task)

���յ������ݼ����ͣ�

Ӳ�����ܵ��Ų���
<type 'unicode'>
######################################################################



######################################################################  
 PS C:\Users\Administrator> net stop mysql
MySQL ��������ֹͣ.
MySQL �����ѳɹ�ֹͣ��

PS C:\Users\Administrator> net start mysql
MySQL ������������ .
MySQL �����Ѿ������ɹ���
######################################################################


######################################################################
###flask���Զ����ǩ��صĹ��ܣ�

from run import app

# self-define filter-tag:����һ����������Ϊ�����˵Ķ���ǰ��ͨ���ܵ�������ֵ��{{ line.cpus.all()|funcccc }}
def funcccc(obj):
    res={}
    for i in obj:
        res[i.cpu_model]=res.get(i.cpu_model,0)+1
    la=[k for k in res.keys()]
    lb=[k for k in res.values()]
    temp=zip(la,lb)
    result=''
    for ii in temp:
        result+=str(ii[0])+'*'+str(ii[1])+'\r'
    return result




##ʵ�ַ������ fro �ڴ�
def funcc(obj):
    res={}
    for i in obj:
        res[i.mm_pn]=res.get(i.mm_pn,0)+1
    la=[k for k in res.keys()]
    lb=[k for k in res.values()]
    temp=zip(la,lb)
    return temp

##ʵ�ַ������ fro Ӳ��
def funccc(obj):
    res={}
    for i in obj:
        res[i.d_model]=res.get(i.d_model,0)+1
    la=[k for k in res.keys()]
    lb=[k for k in res.values()]
    temp=zip(la,lb)
    return temp


env=app.jinja_env
env.filters['funcccc']=funcccc  ##ע���Զ��������
env.filters['funcc']=funcc  ##ע���Զ��������
env.filters['funccc']=funccc ##ע���Զ��������


def interval(test_str,start,end): #��һ������Ϊ�����˶��󣬵ڶ������������Լ����룬 ���÷�����{{test_str| interval(0,2)}}
    return test_str[int(start):int(end)]
env.filters['interval']=interval #ע���Զ��������

   
������Ŀǰ����Ҫ��run.py��ִ�����µ����
from sansa import create_app
from table_process_offline import table_process


app = create_app()  ##ʹ��flask���Ƽ��÷�
from sansa.templatetag.mytag import *   ##�����Զ����ǩ����Ϊ����ʹ����app,��Ҫ�ڴ���app��ִ�е���
######################################################################


ajax:
<script src="{{ url_for('static',filename='js/jquery.min.js') }}"></script>
<script>
 $('html').bind('keypress',function(e){
{#     console.log(e.keyCode)#}
     if (e.keyCode==13){
{#         console.log("11111");#}
         var cmd=$('input:text').val()
         console.log(cmd); //��ȡinput����������������

         var data={
             'cmd':cmd
         }

         $.ajax({
             url:"/jumper_term/server/",
             type:"POST",
             data:data,
             dataType:"json",
             success:function(data){
                 alert("11111111");
             },
             error:function(data){
                 alert("2222222");
             }

         })
         
     }
 })
</script>

@myjumper.route('/jumper_term/<serverinfo>/',methods=['GET','POST'])
def jumper_term(serverinfo):
    if request.method=='POST':
        print(request.form.get('cmd'))
        cmd=request.form.get('cmd')
        serverinfo=session.get('serverno')
        if serverinfo:
            line=db.session.query(models.Asset_db).filter(models.Asset_db.serverno==serverinfo).first()
            user=line.user
            passwd=line.passwd
            ip=line.ip_addr
            print(user,passwd,ip)

            cmdd="C:/Python27/python27.exe C:/Users/Administrator/Desktop/python_related_data/zhl_working_directory/cmdb/sansa/ssh_client.py "+ip+" "+user+" "+passwd+" "+cmd
            ret=os.popen(cmdd)
            ss=ret.read()
            print(ss)


            # return "ok"   //����˷��ص��ǡ�OK��ʱ��ajax����error���д�����Ϊ���صĲ���json��ʽ�����ݣ�
            return jsonify({'name':'zhuhonglei'})  //�����������ʽ������ʱ������success���д������Է��ص�������json��ʽ�ġ�
  
ajax+flask�ܽ᣺
<script src="{{ url_for('static',filename='js/jquery.min.js') }}"></script>
<script>
 $('html').bind('keypress',function(e){
{#     console.log(e.keyCode)#}
     if (e.keyCode==13){
{#         console.log("11111");#}
         var cmd=$('input:text').val()
         console.log(cmd); //��ȡinput����������������   

         var data={
             'cmd':cmd    //1.��ǰ��ҳ��������ݺ�ͨ��ajax��POST�������̨��������
         }

         $.ajax({
             url:"/jumper_term/server/",
             type:"POST",
             data:data,
             dataType:"json",
             success:function(data){
{#                 alert("11111111");#}
                 alert(JSON.stringify(data));  //���պ�˷��͹��������ݲ����з����л�����ʾ
             },
             error:function(data){
                 alert("2222222");
             }
         })
     }
 })
</script>


@myjumper.route('/jumper_term/<serverinfo>/',methods=['GET','POST'])
def jumper_term(serverinfo):
    if request.method=='POST':
        print(request.form.get('cmd'))
        cmd=request.form.get('cmd')  //����ǰ�˷��͹���������
        serverinfo=session.get('serverno')
        if serverinfo:
            line=db.session.query(models.Asset_db).filter(models.Asset_db.serverno==serverinfo).first()
            user=line.user
            passwd=line.passwd
            ip=line.ip_addr
            print(user,passwd,ip)

            cmdd="C:/Python27/python27.exe C:/Users/Administrator/Desktop/python_related_data/zhl_working_directory/cmdb/sansa/ssh_client.py "+ip+" "+user+" "+passwd+" "+cmd
            ret=os.popen(cmdd)
            ss=ret.read()
            print(ss)

            # return "ok"
            return jsonify({'name':'zhuhonglei'})  //���˷���json��ʽ�����ݣ�
  
  
 
 ����һ�����⣺
 
  $.ajax({
             url:"/jumper_term/server/",
             type:"POST",
             data:data,
             dataType:"json",
             success:function(data){
                 var res=JSON.stringify(data);      //ֱ�ӽ��ղ����з����л�������ݴ��С�����ֱ�Ӹ�ֵ��textarea�ᵼ����ʾ�����⣬�̲���eval('('+res+')') �����ݽ��ж��δ����Ϳ��Խ���ˡ�---��Ҫ��
                 var res=eval('('+res+')')
                  $('textarea').val(res);
             },
             error:function(data){
                 alert("2222222");
             }
         })



ͨ��ajax �ϴ��ļ���
    <label for="exampleInputFile">�����ϴ�</label>
    <input type="file" name="file" id="file_upload"/>
    <button type="button" onclick="FileUpload()">��ʼ�ϴ�����</button><br>

function FileUpload(){
    var form_data=new FormData();
    var file_info=$('#file_upload')[0].files[0];
    form_data.append('file',file_info);
    $.ajax({
        url:"/jumper_file/",
        type:'POST',
        data:form_data,
        processData:false, //tell the jquery not to process the data
        contentType:false, // tell teh jquery  not to set contenttype
        success:function(callback){
            alert("success");
        },
        error:function(callback){
            alert("fail!!");
        }
    })

}


@myjumper.route('/jumper_file/',methods=['GET','POST'])
def jumper_file():
    if request.method=="POST":
        file=request.files['file']
        file_name=file.filename
        filenew=os.path.join('sansa\\templates\\files',file_name).replace("\\",'/')
        file.save(filenew)
        print(filenew)
        serverinfo=session.get('serverno')
        if serverinfo:
            line=db.session.query(models.Asset_db).filter(models.Asset_db.serverno==serverinfo).first()
            user=line.user
            passwd=line.passwd
            ip=line.ip_addr
            cmdd="C:/Python27/python27.exe C:/Users/Administrator/Desktop/python_related_data/zhl_working_directory/cmdb/sansa/sftp_client.py "+ip+" "+user+" "+passwd+" "+filenew
            ret=os.popen(cmdd)
            ss=ret.read()


        return "�ϴ��ɹ���"



django+ajax:ʵ����Ϣ�������ļ��ϴ���
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<div>
  <h5>֧�ֵĵ�����ȫ����� linux--{storcli,sas3ircu}; windows--{sas3ircu-win}<br>
  ϵͳ���ù������ linux--{grep [-i]}; windows--{findstr [-i]}</h5>
    <label for="exampleInputFile">�����ϴ�:</label>
    <input type="file" name="file" id="file_upload"/>
    <button type="button" onclick="FileUpload()">��ʼ�ϴ�����</button><br>
    <hr>
==>��<input type="text" name="cmd" style="width: 755px;"/> <br>
<br>
<textarea style="width:800px;height:800px;">
    {{ ss }}

</textarea>

</div>

<script src="/static/bootstrap/js/jquery.min.js"></script>
<script>
 $('html').bind('keypress',function(e){
{#     console.log(e.keyCode)#}
     if (e.keyCode==13){
{#         console.log("11111");#}
         var cmd=$('input:text').val()
         console.log(cmd); //��ȡinput����������������

         var data={
             'cmd':cmd
         }

         $.ajax({
             url:"/jumper_term/server/",
             type:"POST",
             data:data,
             dataType:"json",
             success:function(data){
{#                 alert("11111111");#}
{#                 alert(JSON.stringify(data));#}
                 var res=JSON.stringify(data);
{#                 alert(res);#}
                 var res=eval('('+res+')')
                  $('textarea').val(res);
             },
             error:function(data){
                 alert("2222222");
             }
         })
     }
 })

function FileUpload(){
    var form_data=new FormData();
    var file_info=$('#file_upload')[0].files[0];
    form_data.append('file',file_info);
    $.ajax({
        url:"/jumper_file/",
        type:'POST',
        data:form_data,
        processData:false, //tell the jquery not to process the data
        contentType:false, // tell teh jquery  not to set contenttype
        success:function(callback){
            alert("�ϴ��ɹ�!!");
        },
        error:function(callback){
            alert("fail!!");
        }
    })

}

</script>
</body>
</html>


@login_required
def jumper_main(request):
	ret=request.session.get('serverno',None)
	if ret:
		request.session.pop('serverno')
	ss=asset_db.objects.all()
	return render_to_response("jumpers/jumper_main.html",{'ss':ss})

@login_required
def jumper_file(request):
	file_obj=request.FILES.get('file')
	if file_obj:
		request_set={}
		print("file--obj",file_obj)
		accessory_dir=settings.accessory_dir
		if not os.path.isdir(accessory_dir):
			os.mkdir(accessory_dir)
		upload_file="%s/%s"%(accessory_dir,file_obj.name)
		recv_size=0
		with open(upload_file,'wb') as new_file:
			for chunk in file_obj.chunks():
				new_file.write(chunk)
		print("aaaaa")
		print(upload_file)
		# C:/Users/Administrator/Desktop/python_related_data/zhl_working_directory/server/blog/templates/files/aa.txt

		serverinfo=request.session.get('serverno')
		if serverinfo:
			line=asset_db.objects.all().get(serverno=serverinfo)
			user=line.user
			passwd=line.passwd
			ip=line.ip_addr
			uploadd(ip,user,passwd,upload_file)

		return HttpResponse(json.dumps('�ϴ��ɹ�!!'))


@login_required
def jumper_term(request,serverinfo):
	if request.method=='POST':
		# print(request.POST.get('cmd'))
		cmd=request.POST.get('cmd')
		serverinfo=request.session.get('serverno')
		if serverinfo:
			line=asset_db.objects.all().get(serverno=serverinfo)
			user=line.user
			passwd=line.passwd
			ip=line.ip_addr
			# print(user,passwd,ip)
			# print(cmd)

			if line.owner=='linux':
				ss=ssh22(ip,user,passwd,cmd)
			else:
				ss=winrmm(ip,user,passwd,cmd)
			print(ss)
			print(type(ss))
			return HttpResponse(json.dumps(ss))



	line=asset_db.objects.all().get(serverno=serverinfo)
	user=line.user
	passwd=line.passwd
	ip=line.ip_addr
	print(user,passwd,ip)
	request.session['serverno']=serverinfo
	ss=' '
	# cmd="C:/Python27/python27.exe C:/Users/Administrator/Desktop/python_related_data/zhl_working_directory/cmdb/sansa/ssh_client.py "+ip+" "+user+" "+passwd+" lsblk"
	# ret=os.popen(cmd)
	# ss=ret.read()
	# print(ss)
	return render_to_response("jumpers/jumper_term.html",{'ss':ss})


flask ��app:
from flask import Flask
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

app01=Flask("app01")
app02=Flask("app02")



@app01.route("/index1",methods=['GET','POST'])
def index1():
    return "app01"


@app02.route("/index2",methods=['GET','POST'])
def index2():
    return "app02"

dm=DispatcherMiddleware(app01,{
      '/sec':app02
})

if __name__ == '__main__':
    run_simple('localhost',5000,dm)
    #�˴�����⣺
    ##run_simple('localhost',5000,dm)  ==����ִ��dm() ==>�Զ�ִ��DispatcherMiddleware���__call__,���أ�return app(environ, start_response),
    ##��ʱapp=app01 �� app=app02, ����Ϊapp01(environ, start_response)�� ��Ϊapp01(),���Զ�ִ��app01.__call__,�ֻص�����·���ˡ�
	


�ֶ�ģ�����_request_ctx_stack��
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.globals import _request_ctx_stack
from functools import partial


def _lookup_req_object(name): ##name='request  (partial(_lookup_req_object, 'request'))'
    top = _request_ctx_stack.top   # ����Ǵ�local�л�ȡ֮ǰ�洢��requestcontext ���� ����ctx
    #ִ�к�top=ctx
    if top is None:
        raise RuntimeError("no key")
    return getattr(top, name)  #��requestcontext���� ��ȡ 'request',��ִ���� ctx.request

class Foo:
    def __init__(self):
        self.aaa=123
        self.xxx=323

aa=partial(_lookup_req_object,'aaa')
xx=partial(_lookup_req_object,'xxx')

##�������
_request_ctx_stack.push(Foo())

##��ͼ����
ret=aa()
print(ret)

ret=xx()
print(ret)
	
		 
##�������ʱ��		 
_request_ctx_stack.pop()
ret=_request_ctx_stack.top
print(ret)		 



#�Զ���flask session:
from flask import Flask,session
app=Flask(__name__)

import json
class Mysessioninterface(object):
    def open_session(self,app, request):
        return {}

    def save_session(self, app, session, response):
        response.set_cookie("zhuhonglei",json.dumps(session))

    def is_null_session(self, obj):
        return False

app.session_interface=Mysessioninterface()

@app.route('/index')
def index():
    session['xxx']=123
    return "index"


if __name__ == '__main__':
    app.run()
    # app.__call__
    # self.session = self.app.open_session(self.request)
    app.open_session
    ##�Զ���򵥵�session�ķ�����
    #��app.session_interface = SecureCookieSessionInterface() ==��app.session_interface=Mysessioninterface()  �����������Լ������session��
	
	
##����flask-session�����session���еĲ�����
from flask import Flask,session
from flask_session import RedisSessionInterface
app=Flask(__name__)
app.secret_key="asdfasdfa"

from redis import Redis
conn=Redis()
app.session_interface=RedisSessionInterface(conn,key_prefix='__')

@app.route('/index')
def index():
    session['xxx']=123
    return "index"


if __name__ == '__main__':
    app.run()
    # app.__call__
    # self.session = self.app.open_session(self.request)
    app.open_session
    ##�Զ���򵥵�session�ķ�����
    #��app.session_interface = SecureCookieSessionInterface() ==��app.session_interface=Mysessioninterface()  �����������Լ������session��
