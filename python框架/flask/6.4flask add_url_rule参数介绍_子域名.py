#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


# subdomain=None,             子域名访问
##  www.baidu.com  为主域名
##  api.baidu.com  为子域名


from flask import Flask, views, url_for

app = Flask(import_name=__name__)
app.config['SERVER_NAME'] = 'thunder.com:5000'  #配置域名


@app.route("/", subdomain="admin")
def static_index():
    """Flask supports static subdomains
    This is available at static.your-domain.tld"""
    return "static.your-domain.tld"


@app.route("/dynamic", subdomain="<username>")    #<username>  类似于字符串表达式
def username_index(username):
    """Dynamic subdomains are also supported
    Try going to user1.your-domain.tld/dynamic"""
    return username + ".your-domain.tld"


if __name__ == '__main__':
    app.run()


##运行说明：
# 配置本地的hosts文件
# 127.0.0.1 www.thunder.com
# 127.0.0.1 api.thunder.com
# 127.0.0.1 admin.thunder.com

# 然后就可以访问如下的地址了：
# http://www.thunder.com:5000/dynamic  没有定义主网站，此时www也被匹配成了subdomain="<username>"
# http://admin.thunder.com:5000
# http://api.thunder.com:5000/dynamic