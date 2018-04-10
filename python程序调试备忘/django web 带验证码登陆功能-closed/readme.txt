http://www.cnblogs.com/alex3714/articles/6662365.html

server_2018040802.tar  开发和httpd下都测试OK；
remark:使用服务器本地文件系统作为缓存；


django 开发调试模式：
# 监听机器所有可用 ip （电脑可能有多个内网ip或多个外网ip）
python manage.py runserver 0.0.0.0:8000
访问方法：http://128.1.2.170:8000

问题1：
使用http 服务器时，一直提示[Errno 13] Permission denied: '/var/www/html/server/blog/static/verify_code/20160430/aocw.png'
处理方法：尝试了各种配置，都没有版本解决。最终解决方法如下：
 删除目录 /var/www/html/server/blog/static/verify_code/20160430 后重启httpd 服务后，故障消失了。
 原因： 20160430 这个目录，是在django开发模式运行时生成的，所以需要删除，否则httpd 目前对此无访问权限。
 
 
 问题2：
 使用django 的开发模式，调试功能是正常的，但使用httpd访问时，一直提示验证码错，查看缓存文件，一直没有新产生缓存数据；
 ==》推测原因：是httpd服务器没有缓存文件的访问权限导致的。
 
 修改：
 将setttings中的缓存目录做如下修改，将缓存目录放到工程目录下，这个目录已经配置了httpd的访问权限。（实际做工程时，这个目录也不可以随意设置，需要放到工程目录下。）
 before:
 CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}


after:
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/www/html/server/tmp_cache/django_cache',
    }
}

并为如下两个目录都配置777的权限（保证所有的用户都有写的权限才可以，切记；）
/var/www/html/server/tmp_cache 
/var/www/html/server/tmp_cache/django_cache

remark:也可以只配置 /var/www/html/server/tmp_cache 这一级的目录，下面的一级目录可以不用配置。