#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

##补充1：

##装饰器基础


#之前我们学习的装饰如下:
def wrapper(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

@wrapper  ##这部相当于执行 index=wrapper(index), 即将index函数作为参数带入wrapper函数中，执行结束后，返回innner函数，即index函数被重新装饰成inner函数
def index(request):
    pass

##即上面的代码，完成的是对index的重新装饰，即新的index函数等于inner函数；
# 之后执行index(),就是在执行inner()


##现在我们对上面的装饰器进行改造一下：


def wrapper(option):
    def inner(func,*args,**kwargs):
        pass
    return inner

@wrapper({'k1':'v1'})
def index(request):
    pass

#说明：
# @wrapper({'k1':'v1'})的执行步骤如下：
#step1:执行 wrapper({'k1':'v1'})，返回inner函数；
#step2:执行@inner,即执行 inner(index),即将index函数做为参数带入inner中执行

##对比说明，和我们上面的装饰器不同的地方如下：
# @wrapper ：只执行wrapper函数；   需要调用index才可以执行inner函数；
#@wrapper({'k1':'v1'})：先执行wrapper函数，再执行inner函数； 不需要调用就可以执行inner函数；


##继续对上面的装饰器进行改造：
url_map={

}  ##定义一个空列表

def route(option):
    def inner(func,*args,**kwargs):
        url_map[option['path']]=func
    return inner

@route({'path':'/index'})
def index(request):
    pass
##经过上面装饰器执行后,url_map变为： url_map={'/index':index}
##即通过这种装饰器，实际上就生成了一个路由关系，当用户访问/index时，会自动执行index函数，这就是
# flask中路由的原理


##补充2：
# session&cookie原理
##session相当于一个大字典
#当客户端来请求的时候，会带着一个随机字符串过来，服务器端会根据这个随机字符串作为key创建一个字典，并将
# 用户的数据存储在内存中，当用户请求结束时，将数据写入数据库中
#类似于这样：
{
    'asdfadf':{'name':'jack','age':12},
    'sdfsadfafd':{'name':'tony','age':12},

}


#补充3：
##OOP相关，有下面的一个用法
class Mydic(dict):
    def __init__(self,*args,**kwargs):
        super(Mydic,self).__init__(*args,**kwargs)
        self['modify']=True
obj=Mydic()  ##这样实例化后，就具有 obj.modify=True

##上面的用法在flask中会用到


##补充强度： 配置文件或全局变量，需要大写


##python主流web框架介绍
##介绍flask和django,tornado的区别；
#django 是个重武器，内部包含了非常多的组件：ORM,Form,ModelForm,缓存，Session,中间件，信号等， 适用于大项目
#Flash 短小精悍，内部没有太多的组件，但第三方组件非常丰富。 即flask能缩能伸，可定制性很强。 适用于小项目，大项目
##tornado 异步非阻塞，通过一个线程来执行一千个请求，性能更强
#bottle: 比flask更简洁，但线上应用很少，第三方组件少
#web.py: 和bottle的情况类似，应用较少








