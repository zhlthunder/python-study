#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

"""
session和cookie的区别：

会话（Session）跟踪是Web程序中常用的技术，用来跟踪用户的整个会话。常用的会话跟踪技术是
Cookie与Session。Cookie通过在客户端记录信息确定用户身份，Session通过在服务器端记录信息确定用户身份。

本章将系统地讲述Cookie与Session机制，并比较说明什么时候不能用Cookie，什么时候不能用Session。

1.1  Cookie机制

在程序中，会话跟踪是很重要的事情。理论上，一个用户的所有请求操作都应该属于同一个会话，而另一个用户
的所有请求操作则应该属于另一个会话，二者不能混淆。例如，用户A在超市购买的任何商品都应该放在A的购物车
内，不论是用户A什么时间购买的，这都是属于同一个会话的，不能放入用户B或用户C的购物车内，这不属于同一个会话。

而Web应用程序是使用HTTP协议传输数据的。HTTP协议是无状态的协议。一旦数据交换完毕，客户端与服务器端的
连接就会关闭，再次交换数据需要建立新的连接。这就意味着服务器无法从连接上跟踪会话。即用户A购买了一件
商品放入购物车内，当再次购买商品时服务器已经无法判断该购买行为是属于用户A的会话还是用户B的会话了。
要跟踪该会话，必须引入一种机制。

Cookie就是这样的一种机制。它可以弥补HTTP协议无状态的不足。在Session出现之前，基本上所有的网站
都采用Cookie来跟踪会话。
1.1.1  什么是Cookie

Cookie意为“甜饼”，是由W3C组织提出，最早由Netscape社区发展的一种机制。目前Cookie已经成为标准，
所有的主流浏览器如IE、Netscape、Firefox、Opera等都支持Cookie。

由于HTTP是一种无状态的协议，服务器单从网络连接上无从知道客户身份。怎么办呢？就给客户端们颁发一个
通行证吧，每人一个，无论谁访问都必须携带自己通行证。这样服务器就能从通行证上确认客户身份了。
这就是Cookie的工作原理。

Cookie实际上是一小段的文本信息。客户端请求服务器，如果服务器需要记录该用户状态，就使用
response向客户端浏览器颁发一个Cookie。客户端浏览器会把Cookie保存起来。当浏览器再请求该
网站时，浏览器把请求的网址连同该Cookie一同提交给服务器。服务器检查该Cookie，以此来辨认
用户状态。服务器还可以根据需要修改Cookie的内容。

Session是另一种记录客户状态的机制，不同的是Cookie保存在客户端浏览器中，而Session保存在服务器上。
客户端浏览器访问服务器的时候，服务器把客户端信息以某种形式记录在服务器上。这就是Session。客户端
浏览器再次访问时只需要从该Session中查找该客户的状态就可以了。

如果说Cookie机制是通过检查客户身上的“通行证”来确定客户身份的话，那么Session机制就是通过检查
服务器上的“客户明细表”来确认客户身份。Session相当于程序在服务器上建立的一份客户档案，客户来访
的时候只需要查询客户档案表就可以了。

信息来源：https://www.cnblogs.com/liuwei0824/p/7699632.html

总结：
 cookie :保存在客户端，第一次访问时，服务器在响应信息中会添加cookie,下次请求时需要带上cookie;
 session: 是在服务器端建立的客户档案表，每次访问时，服务器端都会进行校验；

"""

from flask import Flask,session
app = Flask(__name__)
app.secret_key='asdfasdf'
# app.session_interface

@app.route('/')
def index():
    #flask内置的使用 加密cookie（签名cookie）来保存数据的, 即会话的数据是写到cookie中的，没有存储在服务器端，这是flask内置session的使用方式
    session['k1']='v1'
    session['k2']='v2'



    return "index"

if __name__ == '__main__':
    app.run()


##session简单会使用即可



