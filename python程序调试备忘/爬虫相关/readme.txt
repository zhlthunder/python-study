#!/usr/bin/env python
# -*- coding: utf-8 -*-

##������ʽ����
import re
#��ͨ�ַ���Ϊԭ��
# stt="taoyunjiaoyu"
# pat='yun'
# ret=re.search(pat, stt)
# print(ret)

#�Ǵ�ӡ�ַ���Ϊԭ��
# stt="""taoyunjiaoyu
# aa77
# """
# pat='\n'
# ret=re.search(pat, stt)
# print(ret)

##ͨ���ַ���Ϊԭ��
# """
# \w  ��ĸ ���� �»���
# \W ����ĸ ���� �»���
# \dʮ������
# \D  ��ʮ������
# \s �հ��ַ�
# \S �ǿհ��ַ�
#
# """

#
# stt="taoy$7aunjiaoy 7u"
# pat='y\S'
# ret=re.search(pat, stt)
# print(ret)

##ԭ�ӱ�
# [xyz]
# [^xyz]
# stt="taoyunjiaoyq"
# pat='y[^xyu]'
# ret=re.search(pat, stt)
# print(ret)


Ԫ�ַ���
##���������õ��ַ���ΪԪ�ַ�
# . ƥ�任�з�����������ַ�
# ^ƥ������
# $ƥ����β
# *
# +
# ��
# {n}
# {n,m}
# {n,}
# |
# ()



# stt="taoyun777jioayu"
# pat='yunn|777'
# ret=re.search(pat, stt)
# print(ret)

#ģʽ������
# re.I  ���Դ�Сд
# re.S  ��.����ƥ�任�з�
# re.M  ƥ�����

# stt="""Taoyunjiaoyu77
# 66
# aa
# """
# pat=''
# ret=re.search(pat,stt,re.S)
# print(ret)

#����ƥ�亯��
match����
search()
findall()

# stt="taoyun777jiotaoayu"
# pat='tao'
# ret=re.compile(pat).findall(stt)
# print(ret)


��ַƥ��
# str="href=http://www.baidu.com,http://sohu.cn"
# pat='[a-zA-Z]+://[^\s]*[.com|.cn]'
# ret=re.compile(pat).findall(str)
# print(ret)


�绰����ƥ��
# str="aasfdasdf025-78787878,ppppp0527-8787878"
# pat='\d{3}-\d{8}|\d{4}-\d{7}'
# ret=re.compile(pat).findall(str)
# print(ret)



#˵����
python2 ����urllib, urllib2
python3: ֻ��urllib  (����������python2�е�urllib, urllib2�Ĺ���)


#chapter 2
#��������÷�
# import urllib.request
# import re
# data=urllib.request.urlopen("http://128.1.2.250/asset_db_show/").read().decode('utf-8','ignore')
# pat='\d{4}'
# ret=re.compile(pat).findall(data)
# print(ret)


##�������ܺ���
# urlopen() ��һ����ҳ�ķ���
# urlretrieve (��ַ�����ش洢�ļ�) ֱ��������ҳ������
# urlcleanup() ���ϵͳ������
##��ִ��urllib.request.urlopen(url), Ȼ������������ִ������ķ�����
# info() ��ѯ��ȡҳ��ļ����Ϣ
#getcode() ��ȡ״̬��
#geturl() ��ȡurl




# import  urllib.request
# import os
# data=urllib.request.urlopen("http://128.1.2.250/asset_db_show/")
# print(data.info())
# print(data.getcode())
# dir='C:\cmdb'
# # print(dir)
# dir=os.path.join(dir,'test.html')
# urllib.request.urlretrieve("http://128.1.2.250/asset_db_show/",dir)
# urllib.request.urlcleanup()


##��ʱ���ã�timeout ����
##urlopen ��������timeout, ���Ը��ݲ�ͬ��վ�ķ����ٶȣ����ú��ʵ�timeout
# import urllib.request
# data=urllib.request.urlopen("http://128.1.2.250/asset_db_show/",timeout=1).read().decode('utf-8','ignore')
# print(data)



##�Զ�ģ��http����
#�ͻ������Ҫ�����������ͨ�ţ���Ҫͨ��http������У�http�����кܶ��֣�����get, post
#get ����
# http://www.baidu.com/s?wd=python


##ͨ��pythonģ��ʵ��http����ķ���
#ʹ��urllibģ��
# 1.�򵥵�get����
# import urllib.request
# data=urllib.request.urlopen("http://128.1.2.250/asset_db_show/").read().decode('utf-8','ignore')
# print(data)

#2.ͨ��Request()������get����ķ�ʽ��
# import urllib.request
# req=urllib.request.Request("http://128.1.2.250/asset_db_show/")
# data=urllib.request.urlopen(req).read().decode('utf-8')
# print(data)


#3.��������get����
# import urllib.request
# key="����"
# key=urllib.request.quote(key) ##��ΪURL�в����԰������ģ�����ؼ��������ģ���Ҫ������������������ַ�����ת��ſ���
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


���䣺
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




# ����������αװ�����ַ���
# urllib.request.build_opener()  ##�˴���Ҫ�������ַ���
# urllib.request.Request.add_header()



#�û���������
# import urllib.request
# url="http://www.baidu.com"
# headers=('User-Agent','IE10.2')
# opener=urllib.request.build_opener()
# opener.addheaders=[headers]
# data=opener.open(url).read()



##�û�����صĹ���
# import urllib.request
# import re
# import random
#
# uapools=[
#     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; rv:59.0) Gecko/20100101 Firefox/59.0",
# ]
#
# def user_agent(pools):
#     ua=random.choice(pools)
#     print(ua)
#     headers=('User-Agent',ua)
#     opener=urllib.request.build_opener()
#     opener.addheaders=[headers]
#     urllib.request.install_opener(opener)

#���÷���
# url='http://128.1.2.250/asset_db_show/'
# user_agent(uapools)
# data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
# print(data)


#����IP����
import urllib.request
ip='128.1.2.250:80'
proxy=urllib.request.ProxyHandler({"http":ip})
opener=urllib.request.build_opener(proxy,urllib.request.ProxyHandler)
urllib.request.install_opener(opener)


##ͬʱʹ��IP�����UA����
import urllib.request
import random
uapools=[
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; rv:59.0) Gecko/20100101 Firefox/59.0",
]
ip="128.1.2.250:80"
##����IP����
proxy=urllib.request.ProxyHandler({"http":ip})
opener=urllib.request.build_opener(proxy,urllib.request.ProxyHandler)
##����UA����
ua=random.choice(uapools)
headers=('User-Agent',ua)
opener.addheaders=[headers]
urllib.request.install_opener(opener)

url='http://128.1.2.250/asset_db_show/'
data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
print(data)



#xpath���ʽ
"""
�Աȣ�
xpath :Ч�ʸ�
������ʽ�� ����ǿ��
==���ʣ�����ѡ��xpath���ʽ��xpath������˵�ʱ�򣬾���������ʽ

xpath���õ��﷨��
/ �����ȡ
text() ȡ��ǩ������ı�
//��ǩ��**  ȡ���б�ǩ��Ϊ**�ı�ǩ
//��ǩ��**[@������=������ֵ��]  ��ȡĳ��������Ϊ�ض�ֵ�������ض���ǩ
@������  ����ȡĳ������ֵ

ʵ����
ȡ���⣺/html/head/title/text()
��ȡ���е�div��ǩ //div
��ȡclass="tool"��div ��ǩ  //div[@class='tool']
"""


##�����urllib��ʹ��xpath��������Ϣ����ȡ����ʱ������Ҫ�Ȱ�װ lxmlģ�飬Ȼ����ҳ����ͨ��lxml�µ�etreeת��Ϊtreedata����ʽ
# ��Ҫ��python3.5�����ϣ��ڴ�lxml����etreeʱ����ʾ����ɫ�����ߡ���ֱ�Ӻ��ԣ���Ӱ��������ʹ��

# ʹ�÷�ʽ1�� etree�в����ߣ���etree.cp36-win32.pyd ����ļ�һ��Ҫ��ƽ̨����һ�£�32ϵͳ�϶�Ӧwin32,64λϵͳ�϶�Ӧλamd64����������lxmlģ�鰲װʱ�Զ����ɵģ��������޷�ִ��
import urllib.request
from lxml import etree

data=urllib.request.urlopen('http://128.1.2.250/asset_db_show/').read().decode('utf-8','ignore')
print(data)
treedata=etree.HTML(data)
title=treedata.xpath("//title/text()")

#ʹ�÷�ʽ2������ etree�в����ߣ���etree.cp36-win32.pyd ����ļ�һ��Ҫ��ƽ̨����һ�£�32ϵͳ�϶�Ӧwin32,64λϵͳ�϶�Ӧλamd64����������lxmlģ�鰲װʱ�Զ����ɵģ��������޷�ִ��
from lxml import html
page_source='''
<html>
<a>link</a>
</html>
'''
# page=html.etree.HTML(page_source)
ret=page.xpath("/html/a/text()")
print(ret)






