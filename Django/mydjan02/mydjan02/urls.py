"""mydjan02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin  #related with admin web

#import views module file
from app1.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),  #related with admin web
    url(r'^$', index),
    url(r'^login/$',login),
    url(r'^logout/$',logout),
    url(r'^host_manager/$',host_manager),
    url(r'^dashboard/$',dashboard),
    url(r'^asset/$',asset),
    url(r'^monitor/$',monitor),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'index.html'}), ##for login_required

]
