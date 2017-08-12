from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login,logout_then_login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csvt02.views.home', name='home'),
    # url(r'^csvt02/', include('csvt02.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^regist/$','blog.views.regist'),
    url(r'^$','blog.views.index'),
    url(r'^host_manager/$','blog.views.host_manager'),
    #url(r'^monitor/$','blog.views.monitor'),
    url(r'^monitor/(?P<page>[0-9]+)/$','blog.views.monitor'),
    url(r'^asset/$','blog.views.asset'),
    url(r'^accounts/login/$',login,{'template_name':'index.html'}),
    #url(r'^accounts/login/$','django.contrib.auth.views.login',{'template_name':'index.html'}),
    url(r'^login/$','blog.views.login_accounts'),
    #url(r'^logout/$','blog.views.logout'),
    url(r'^logout/$',logout_then_login),
    url(r'^search/$','blog.views.search'),
    #url(r'^multi_search/$','blog.views.multi_search'),
)
