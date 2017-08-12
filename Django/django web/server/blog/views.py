import re
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
from blog.models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from p_ssh_expect import ssh2
from p_ssh_expect_multi import ssh2
import time
import threading

@login_required
def index(request):
	return render_to_response('index.html')

#important: this function 's name must be account_login, if change to login, the decorator can not work
#modify: 1)this function 's name do not need to care; 2) except this function, all other functions should add "@login_required"(this is the key words of django system, no relation with the name of login funciotn' name,so do not care about it)

def login_accounts(request):
	username=request.POST.get('username')
	password=request.POST.get('password')
	#print request.user
        user=auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request,user)
		#print request.user
		return HttpResponseRedirect("/host_manager/")
	else:
		return render_to_response('index.html',{'login_err':"Wrong username and password!"})

@login_required
def host_manager(request):
	return render_to_response('host_manager.html',{'user':request.user})


def get_pages():
        num=divmod(Disk_info.objects.filter().count(),12)
        if num[1]!=0:
                pages=num[0]+1
        else:
                pages=num[0]
        return pages


@login_required
def monitor(request,page):
        page=int(page)
        pages=[x for x in range(1,get_pages()+1)]
        end=pages[-1]
        content_list=Disk_info.objects.filter()[(page-1)*12:page*12]
        print page
        print content_list

        if get_pages()>1:
                return render_to_response('monitor.html',{'disk_info':content_list,'pages':pages,'end':end,'page':page,'errmsg':'OK'})
        else:
                return render_to_response('monitor.html',{'disk_info':content_list,'pages':pages,'end':end,'errmsg':'faile'})

"""
@login_required
def monitor(request):
	disk_info=Disk_info.objects.all()	
	return render_to_response('monitor.html',{'disk_info':disk_info,'user':request.user})
"""


@login_required
def asset(request):
	ss=Server_db.objects.all()
        cmd = ["cat /proc/cpuinfo  | grep model | grep Intel | uniq -c|cut -d: -f2","dmidecode -t memory|grep -i part | grep -v Unknown | uniq -c|awk '{print $1,$4}'","lspci | grep -i eth","storcli /c0 show all | grep -E 'HDD|SSD' | grep ^[0-9]|awk '{print $(NF-1)}' |uniq -c && sas3ircu 0 display | grep -i model | awk '{print $NF}'|uniq -c","storcli show | grep '^ \{0,2\}[0-9]'|awk '{print $2}' && sas3ircu 0 display | grep -i 'controller type'|awk '{print $NF}'"]
        for line in ss:
		result=[]
		username=line.user
        	passwd =line.passwd
        	threads = [10]
		ip=line.ip_addr
        	a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd,result))
        	a.start()
        	time.sleep(5)
		
		##for cpu processing
		cpu=result[0]
		p=re.compile(r'\s(E\d+-\d+\sv\d)\s')
		tt=p.findall(cpu)
		print tt
		tt="".join(tt)
		line.cpu=tt
		
		##for memory processing
		memory=result[1]
		print result[1]
		tt=re.sub(r'\s+','*',memory)
		print tt
		line.memory=tt

		##for network card processing
		card=result[2]
		#p=re.compile(r'\s(\D{0,1}\d+)\s')
		p=re.compile(r'\s(I?\d+[A-Z]{0,4})\s')
		tt=p.findall(card)
		t=list(tt)
		tt="/".join(t)
		#print tt
		line.ethernet=tt

		##for disk processing
		tt=result[3]
		p=re.compile(r'\S+')
		t=p.findall(tt)
		tt="/".join(t)
		line.disk=tt
		
		##for raid card processing
		line.raid=result[4]
		
		## write data to server_db database
		#dic={'name':line.name,'ip_addr':line.ip_addr,'cpu':result[0],'memory':result[1],'ethernet':result[2],'disk':result[3],'raid':result[4]}
		line.save()
	ss=Server_db.objects.all()
	return render_to_response('asset.html',{'ss':ss})
"""
def asset(request):
        cpu=ssh2("128.1.2.188","root","123456","cat /proc/cpuinfo  | grep model | grep Intel | uniq -c|cut -d: -f2 ")
        memory=ssh2("128.1.2.188","root","123456","dmidecode -t memory | grep Part | grep -v Unknown | uniq -c")
        eth=ssh2("128.1.2.188","root","123456","lspci | grep -i eth")
        disk=ssh2("128.1.2.188","root","123456","storcli /c0 show all | grep '^[0-9]\{1,3\}:'")
        raid_card=ssh2("128.1.2.188","root","123456","storcli show | grep '^ \{0,2\}[0-9]'")

	return render_to_response('asset.html',{'cpu':cpu,'mem':memory,'eth':eth,'disk':disk,'raid_card':raid_card})
"""

@login_required
def search(request):
        print request.GET
        print request.POST
        tt=request.POST.get('model')
	tu=request.POST.get('interface')
	tv=request.POST.get('rotarate')
	tw=request.POST.get('capacity')
	kwargs={ }
	if tt is not None:
		kwargs['d_model__contains']=tt
	if tu is not None:
		kwargs['d_interface__contains']=tu
	if tv is not None:
		kwargs['d_rotarate__contains']=tv
	if tw is not None:
		kwargs['d_capacity__contains']=tw
        content_list=Disk_info.objects.filter(**kwargs)
        #content_list=Disk_info.objects.filter(d_model__contains=tt)
        return render_to_response('search.html',{'disk_info':content_list})
