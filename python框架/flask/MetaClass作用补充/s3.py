#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl



#
class Mytype(type):
    def __init__(self,*args,**kwargs):
        print("init")
        super(Mytype,self).__init__(*args,**kwargs)

    def __call__(cls, *args, **kwargs):
        print("call")
        return super(Mytype,cls).__call__(*args,**kwargs)

def with_metaclass(arg,base):
    return Mytype('MyType', (base,), {})

class Foo(with_metaclass(Mytype,object)):
    pass
#
obj=Foo()  #metaclass定义类，一种重要的说明： “执行这个实例化操作时，会自动执行Mytype的__call__方法”， 切记


##本质功能和s1,s2相同。

