1. 模板继承中，block的名字中不能有非法字符，比如如下：  （名字的要求：尽量用字母，数字，下划线来组成）
{% block page-content %} 
运行时提示的错误：jinja2.exceptions.TemplateSyntaxError: Block names in Jinja have to be valid Python identifiers and may not contain hyphens, use an underscore instead.

######################################################################
2. 问题2：AttributeError: type object 'Asset_db2Cpu' has no attribute 'foreign_keys'
  这个问题和下面的这个中间表有关：
  要求：1. 中间表的类名和 表名必须不相同， 如果只是大小写不同会有错误；
  
  class asset_db2_cpu(db.Model):
    __tablename__ = 'asset_db2cpu'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    asset_db_id=db.Column(db.Integer,db.ForeignKey('asset_db.id'))
    cpu_id=db.Column(db.Integer,db.ForeignKey('cpu.id'))

	2.secondary='asset_db2cpu' 关联的时候，需要使用表名的字符串，如果使用类名报错，切记
	cpus=db.relationship('Cpu',secondary='asset_db2cpu',backref='asset_dbs')
	

此问题二次说明，使用的实例如下：
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
    __tablename__="class"   ##类名和表名一定要区分开
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),nullable=True)
    floor=db.Column(db.String(100),nullable=True)

    students=db.relationship("Student",secondary="class2student",backref=db.backref("classs",lazy="dynamic"),lazy="dynamic")
	##关联时问题最多：
	 第一项是类的名称不是表的名称，即是"Student"，如果写成"student"就会报错；
	 第二项是中间表的表的名称不是类的名称，即是"class2student"，而不是“Class2student”，
	 最终总结：  sqlalchemy 创建完数据表，如果发现往数据表中写入数据一直报错，基本都是上面两个问题造成的，切记；
	 
	 
	
######################################################################	
3.错误信息：//django和flask一样的问题
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd4 in position 101: invalid continuation byte
问题描述：
在base模板中有中文时可以正常显示，子模板通过extends继承后，里面包含中文时就会显示异常，报上面的错误。
即使在子模板的开头加上 “<meta charset="utf-8">”也还是显示异常；

原因：经过排查这个问题确实和文件的编码格式有问题，单独确认要显示的这个HTML文件，它的格式是ANSI，修改成UTF-8 without BOM 后还是有问题，
推测是项目中的其它文件没有使用UTF-8的格式的原因，将所有的文件都修改为UTF-8的格式后，问题就解决了，切记。（记住：必需把所有的文件都改成utf-8的格式才可以避免这个问题）

根本解决对策：在pycharm的 文件--设置--文件编码--，将IDE encoding,project encoding,文件默认编码 都设置为UTF-8的格式编辑的原因
且如果项目中的文件是从别的地方拷贝过来的，需要在目录树中 为每个文件手动指定编码格式才可以，切记！！！
  
  特别关注：此时可以看到，目录树中的文件，有的显示：‘encoding is hard coded in the text’, 因为文件的开头定义了：# -*- coding: utf-8 -*-
   此时删除# -*- coding: utf-8 -*- 后， 再去查看，文件的格式就是空白的了。（@@@@@）
  
######################################################################
4. flask前端包含 bootstrap的方法：	 其中static和 templates 处于同级目录
<link href="{{ url_for('static',filename='css/bootstrap.css') }}" rel="stylesheet">
<link href="{{ url_for('static',filename='css/bootstrap-responsive.css') }}" rel="stylesheet">
<script src="{{ url_for('static',filename='js/jquery.min.js') }}"></script>
<script src="{{ url_for('static',filename='js/bootstrap.js') }}"></script>

######################################################################
5.
flask sqlalchemy 模糊查询：
ss=db.session.query(models.Asset_db).filter(models.Asset_db.serverno.ilike('%'+tt+'%')).all()

通过flask离线脚本操作数据库：

######################################################################
6. api接口调试：
简单使用：
get 的方法：


import urllib2
res=urllib2.urlopen('http://128.1.2.250')
data=res.read()
print(data)

http是基于请求和应答机制的，客户端提出请求，服务端提供响应；
urllib2用一个request对象来映射你提出的http请求，最基本的应用是：
将你要请求的地址创建一个request对象，通过调用urlopen并传入request对象，将返回一个相关请求的response对象。
>>> import urllib2
>>> req=urllib2.Request("http://128.1.2.250")
>>> res=urllib2.urlopen(req)
data=res.read()
print(data)



post：
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


调试时一直报错如下，最终排查是服务器端的问题。
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

http请求实现的几种方法的对比如下：
##通过python模块实现http请求的方法
#使用urllib模块
# 1.简单的get请求
# import urllib.request
# data=urllib.request.urlopen("http://128.1.2.250/asset_db_show/").read().decode('utf-8','ignore')
# print(data)

#2.通过Request()对象发送请求的方式：
# import urllib.request
# req=urllib.request.Request("http://128.1.2.250/asset_db_show/")
# data=urllib.request.urlopen(req).read().decode('utf-8')
# print(data)


#3.带参数的get请求
# import urllib.request
# key="测试"
# key=urllib.request.quote(key) ##如果关键字是中文，才需要调用这个方法
# url='http://www.baidu.com/s?wd='+key
# data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
# print(data)

#4.post请求
# import  urllib.request
# import urllib.parse
# posturl='http://www.baidu.com/mypost'
# postdata=urllib.parse.urlencode({
#     'name':'jack',
#     'pass':'123'
# }).encode('utf-8')
# req=urllib.request.Request(posturl,postdata) ##封装请求对象， 这是通过对象的方法来发送请求
# data=urllib.request.urlopen(req).read().decode("utf-8")
# print(data)


#使用urllib2模块, with python2.7
# 1.get方法
# import urllib2
# data=urllib2.urlopen('http://128.1.2.250/asset_db_show/').read()
# print(data)

#2. get方法，使用对象：
# import urllib2
# req=urllib2.Request('http://128.1.2.250/asset_db_show/')
# data=urllib2.urlopen(req).read()
# print(data)

#3.post请求
# import urllib2,json
# data={"ip_addr": "7.4.4.5"}
# url="http://128.1.2.250/asset/api/v1.0/r57005577/update"
# ddata=json.dumps(data)
# header_dict={'Content-Type':"application/json"}
# req = urllib2.Request(url=url,data=ddata,headers=header_dict)
# res_data = urllib2.urlopen(req).read()
# print(res_data)

#总结： urlib和urlib2的区别：可以简单认为是：把urlib.request 封装成 urlib2



######################################################################
记住一个困扰了我半天的故障：
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
		
执行结果：
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

解决办法：
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

输出：
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
多线程lock的使用方法：
import threading
lock=threading.Lock()
lock.acquire()
互斥操作
lock.release()
######################################################################

######################################################################
@@mysql 数据库配置相关：
   mysql数据库的导出和导入：
   
   导出整个数据库： mysqldump -u root -p mydb > mydb.sql     
   导入整个数据库：先创建一个同名的数据库，比如mydb;  create database mydb;
                   use mydb;
                   source C:\cmdb\client\mydb.sql   #这样就可以完成导入了



   导出数据表： mysqldump -u root -p mydb blog_disk_info > blog_disk_info.sql
   导入数据表：在一台新的mysql服务器上，myslq -uroot 登陆后，
   创建数据库：create database mydb;
　 use mydb；然后执行：
   mysql> source /home/nn/blog_disk_info.sql   //和导入数据库的命令类似
######################################################################   
   
######################################################################   
mysql数据库相关中文显示的问题： 
   1.alter table blog_asset_db default charset utf8;  修改数据库表  ==》alter table blog_cpu default character set utf8 collate utf8_bin;
   2.alter database mydb default character set utf8 collate utf8_general_ci; 修改数据库
   3.mysql> ALTER TABLE `blog_cpu` CHANGE `cpu_model` `cpu_model` VARCHAR(100) CHARACTER SET utf8 NULL;  修改字段；
Query OK, 14 rows affected (0.04 sec)
   
 4.  mysql> show variables like 'character%';   //如果编码格式的配置如下，表示 ok
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

mysql> set character_set_database=utf8; //如果有需要修改的，使用这个命令对每一项进行修改即可
Query OK, 0 rows affected, 1 warning (0.00 sec)

总结： 进行上面四步关于数据库的编码格式的修改后，才可以向mysql中插入中文：（切记@@@@@）
mysql> insert into blog_cpu(cpu_model) value("测试");
Query OK, 1 row affected (0.00 sec)

总结2：经过验证，进行上面的修改后，django的视图和前端不用做任何修改就可以直接支持中文输入并写入数据库中：
		task=request.POST.get('task')
		print(task)
		print(type(task))
		asset_db.objects.filter(serverno=serversn).update(serverno=serverno,ip_addr=ip,user=user,passwd=passwd,status='Online',owner=owner,remark2=task)

接收到的数据及类型：

硬盘性能调优测试
<type 'unicode'>
######################################################################



######################################################################  
 PS C:\Users\Administrator> net stop mysql
MySQL 服务正在停止.
MySQL 服务已成功停止。

PS C:\Users\Administrator> net start mysql
MySQL 服务正在启动 .
MySQL 服务已经启动成功。
######################################################################


######################################################################
###flask中自定义标签相关的功能；

from run import app

# self-define filter-tag:接收一个参数，即为被过滤的对象，前端通过管道符来赋值：{{ line.cpus.all()|funcccc }}
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




##实现分类汇总 fro 内存
def funcc(obj):
    res={}
    for i in obj:
        res[i.mm_pn]=res.get(i.mm_pn,0)+1
    la=[k for k in res.keys()]
    lb=[k for k in res.values()]
    temp=zip(la,lb)
    return temp

##实现分类汇总 fro 硬盘
def funccc(obj):
    res={}
    for i in obj:
        res[i.d_model]=res.get(i.d_model,0)+1
    la=[k for k in res.keys()]
    lb=[k for k in res.values()]
    temp=zip(la,lb)
    return temp


env=app.jinja_env
env.filters['funcccc']=funcccc  ##注册自定义过滤器
env.filters['funcc']=funcc  ##注册自定义过滤器
env.filters['funccc']=funccc ##注册自定义过滤器


def interval(test_str,start,end): #第一个参数为被过滤对象，第二三参数需求自己传入， 调用方法：{{test_str| interval(0,2)}}
    return test_str[int(start):int(end)]
env.filters['interval']=interval #注册自定义过滤器

   
运行项目前，需要在run.py中执行如下的命令：
from sansa import create_app
from table_process_offline import table_process


app = create_app()  ##使用flask的推荐用法
from sansa.templatetag.mytag import *   ##导入自定义标签，因为其中使用了app,需要在创建app后执行导入
######################################################################


ajax:
<script src="{{ url_for('static',filename='js/jquery.min.js') }}"></script>
<script>
 $('html').bind('keypress',function(e){
{#     console.log(e.keyCode)#}
     if (e.keyCode==13){
{#         console.log("11111");#}
         var cmd=$('input:text').val()
         console.log(cmd); //获取input输入框中输入的命令

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


            # return "ok"   //当后端返回的是“OK”时，ajax进入error进行处理，因为返回的不是json格式的数据；
            return jsonify({'name':'zhuhonglei'})  //当返回这个格式的数据时，进入success进行处理，测试返回的数据是json格式的。
  
ajax+flask总结：
<script src="{{ url_for('static',filename='js/jquery.min.js') }}"></script>
<script>
 $('html').bind('keypress',function(e){
{#     console.log(e.keyCode)#}
     if (e.keyCode==13){
{#         console.log("11111");#}
         var cmd=$('input:text').val()
         console.log(cmd); //获取input输入框中输入的命令   

         var data={
             'cmd':cmd    //1.从前端页面接收数据后，通过ajax的POST请求向后台发送数据
         }

         $.ajax({
             url:"/jumper_term/server/",
             type:"POST",
             data:data,
             dataType:"json",
             success:function(data){
{#                 alert("11111111");#}
                 alert(JSON.stringify(data));  //接收后端发送过来的数据并进行反序列化后显示
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
        cmd=request.form.get('cmd')  //接收前端发送过来的数据
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
            return jsonify({'name':'zhuhonglei'})  //向后端发送json格式的数据；
  
  
 
 另外一个问题：
 
  $.ajax({
             url:"/jumper_term/server/",
             type:"POST",
             data:data,
             dataType:"json",
             success:function(data){
                 var res=JSON.stringify(data);      //直接接收并进行反序列化后的数据带有“”，直接赋值给textarea会导致显示的问题，固采用eval('('+res+')') 对数据进行二次处理后就可以解决了。---重要；
                 var res=eval('('+res+')')
                  $('textarea').val(res);
             },
             error:function(data){
                 alert("2222222");
             }
         })



通过ajax 上传文件：
    <label for="exampleInputFile">附件上传</label>
    <input type="file" name="file" id="file_upload"/>
    <button type="button" onclick="FileUpload()">开始上传附件</button><br>

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


        return "上传成功！"



django+ajax:实现信息交换及文件上传：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<div>
  <h5>支持的第三方全局命令： linux--{storcli,sas3ircu}; windows--{sas3ircu-win}<br>
  系统内置过滤命令： linux--{grep [-i]}; windows--{findstr [-i]}</h5>
    <label for="exampleInputFile">附件上传:</label>
    <input type="file" name="file" id="file_upload"/>
    <button type="button" onclick="FileUpload()">开始上传附件</button><br>
    <hr>
==>：<input type="text" name="cmd" style="width: 755px;"/> <br>
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
         console.log(cmd); //获取input输入框中输入的命令

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
            alert("上传成功!!");
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

		return HttpResponse(json.dumps('上传成功!!'))


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


flask 多app:
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
    #此处的理解：
    ##run_simple('localhost',5000,dm)  ==》会执行dm() ==>自动执行DispatcherMiddleware类的__call__,返回：return app(environ, start_response),
    ##此时app=app01 或 app=app02, 比如为app01(environ, start_response)， 即为app01(),会自动执行app01.__call__,又回到了老路上了。
	


手动模拟操作_request_ctx_stack：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.globals import _request_ctx_stack
from functools import partial


def _lookup_req_object(name): ##name='request  (partial(_lookup_req_object, 'request'))'
    top = _request_ctx_stack.top   # 这句是从local中获取之前存储的requestcontext 对象 ，即ctx
    #执行后，top=ctx
    if top is None:
        raise RuntimeError("no key")
    return getattr(top, name)  #从requestcontext对象 获取 'request',即执行了 ctx.request

class Foo:
    def __init__(self):
        self.aaa=123
        self.xxx=323

aa=partial(_lookup_req_object,'aaa')
xx=partial(_lookup_req_object,'xxx')

##请求进来
_request_ctx_stack.push(Foo())

##视图操作
ret=aa()
print(ret)

ret=xx()
print(ret)
	
		 
##请求结束时：		 
_request_ctx_stack.pop()
ret=_request_ctx_stack.top
print(ret)		 



#自定义flask session:
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
    ##自定义简单的session的方法：
    #将app.session_interface = SecureCookieSessionInterface() ==》app.session_interface=Mysessioninterface()  ，即更换成自己定义的session类
	
	
##调用flask-session组件对session进行的操作：
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
    ##自定义简单的session的方法：
    #将app.session_interface = SecureCookieSessionInterface() ==》app.session_interface=Mysessioninterface()  ，即更换成自己定义的session类
