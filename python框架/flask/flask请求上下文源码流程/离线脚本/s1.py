#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask,current_app,globals,_app_ctx_stack

app1=Flask('app01')
app1.debug=True
##如果app中存储了数据库的用户名，密码，数据库等信息， 在下面就可以获取到，然后建立数据库的连接

app2=Flask('app02')
app2.debug=False

with app1.app_context():  #相当于执行 with AppContext(self): 会自动执行它的__enter__方法，最终也是执行 _app_ctx_stack.push(self)，即自动执行了压栈的操作
        ##实例化对象： app_ctx=AppContext
        ##里面包含：
        #  app_ctx.app
        #  app_ctx.g
    #既然上面已经完成了压栈的操作，我现在直接打印出来看看
    print(_app_ctx_stack._local.__storage__)
    #输出： {<greenlet.greenlet object at 0x06240B20>: {'stack': [<flask.ctx.AppContext object at 0x059F4E50>]}}
    print(type(current_app)) #这是返回app对象
    print(current_app.config)
    print(current_app.config['DEBUG'])

    ##且上面的操作执行完成之后，就会执行pop操作

with app2.app_context():
    print(_app_ctx_stack._local.__storage__)


print("------------------------------")


##所以如果并排写两个with,那就是一个一个处理，local始终只有一个对象
#但如果用下面的方法来写的话：

with app1.app_context():
    print(_app_ctx_stack._local.__storage__)  #此时栈中存放的是app1,且app1是最后的一个，执行top时获取的就是它 ；
    #{<greenlet.greenlet object at 0x05C70B20>: {'stack': [<flask.ctx.AppContext object at 0x05D7E050>]}}
    with app2.app_context():
        print(_app_ctx_stack._local.__storage__)#此时栈中存放了app1,app2
        #{<greenlet.greenlet object at 0x05C70B20>: {'stack': [<flask.ctx.AppContext object at 0x05D7E050>, <flask.ctx.AppContext object at 0x05D7E0D0>]}}
        print(current_app.config['DEBUG'])
        #重要：在这个代码块中执行top操作时，获取的也是自己,即获取的是app2，发生错乱
    ##当上面的代码块执行结束后，会pop掉app2,这样栈中最后一个还是app1,不影响下面对app1的获取操作（非常重要，这就是为什么要使用栈的原因，这也就回答了readme中问题2）
    ##！！只有这种情况才会出现这样的应用场景， 如果写网站的话，栈中同时只会有一个对象@@@
    print(current_app.config['DEBUG'])