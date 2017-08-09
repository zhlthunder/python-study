
from django.http import HttpResponse
from django import forms
from django.shortcuts import render_to_response
from blog.models import User
from p_ssh_expect import ssh2
import re


class Userform(forms.Form):
	username=forms.CharField()
	headimg=forms.FileField()
"""
def regist(req):
	if req.method =="POST":
		uf=Userform(req.POST,req.FILES)
		if uf.is_valid():
			username=uf.cleaned_data['username']
			headimg=uf.cleaned_data['headimg']
			user=User()
			user.name=username
			user.headimg=headimg
			user.save()
			print username
			return HttpResponse("ok")
	else:
		uf=Userform()
		
	return render_to_response('regist.html',{'uf':uf,'list':list})
"""
def index(req):
	return render_to_response('index.html')

def regist(req):
	cpu=ssh2("128.1.2.188","root","123456","cat /proc/cpuinfo  | grep model | grep Intel | uniq -c|cut -d: -f2 ")
	memory=ssh2("128.1.2.188","root","123456","dmidecode -t memory | grep Part | grep -v Unknown | uniq -c")
	eth=ssh2("128.1.2.188","root","123456","lspci | grep -i eth")
	disk=ssh2("128.1.2.188","root","123456","storcli /c0 show all | grep '^[0-9]\{1,3\}:'")
	raid_card=ssh2("128.1.2.188","root","123456","storcli show | grep '^ \{0,2\}[0-9]'")
	return render_to_response('regist.html',{'cpu':cpu,'mem':memory,'eth':eth,'disk':disk,'raid_card':raid_card})
