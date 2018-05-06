#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#创建类的方法：
# 类默认是由type创建的
# Base=type('Base',(object,),{})  #用type创建一个类，这个类继承object，类里面是空的
# print(Base) # 打印：<class '__main__.Base'>



#
class Mytype(type):
    def __init__(self,*args,**kwargs):
        print("init")
        super(Mytype,self).__init__(*args,**kwargs)

    def __call__(cls, *args, **kwargs):
        print("call")
        return super(Mytype,cls).__call__(*args,**kwargs)


class Foo(Mytype('Base',(object,),{})): #可以理解为：Mytype('Base',(object,),{}) 创建一个类，然后Foo继承这个类
                                        #可以理解为：这个类Mytype('Base',(object,),{})  是有Mytype创建的，等价于metaclass=Mytype
    pass
#
obj=Foo()  #metaclass定义类，一种重要的说明： “执行这个实例化操作时，会自动执行Mytype的__call__方法”， 切记

"""
1.type可以创建类，对应的metaclass=type; Mytype也可以创建了， 对应的metaclass=Mytype;
2.class Foo(Mytype('Base',(object,),{})) --> 等价于：
 { class Base(metaclass=Mytype)
        pass

 class Foo(Base):
       pass  }
"""

#总结： s2 和 s1是两种不同的写法， 但本质上是一模一样的。

