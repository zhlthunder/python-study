#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl


"""
这表示：类由type来创建
class Foo(metaclass=type)

这表示继承type
class Foo(type)
"""

##已有知识：对象是由类创建的。
class Foo(object):
    pass
obj=Foo()  ##这是类的实例化，这个对象obj是由Foo类创建的。

##还有一句话：python中一切皆是对象，按照这个思路，那类也是对象
#那类是由谁创建的呢？  按照之前说的，默认是由type创建的。

#————————————————————————————————
#下面两种创建类的方法是等价的，只不过是两种不同的写法而言
##这叫创建一个类
class Foo(object):
    pass

#这也叫创建一个类
Foo=type('Foo',(object,),{})
#————————————————————————————————

# 所以，我们说，类是由type创建的。
#既然type可以创建类，我们可以自定义一个type吗？ 答案是可以的。
#那我们就需要自定义一个自己的type. 比如：
class Mytype(type):
    pass
##即定义一个Mytype 类继承type,这样就可以用Mytype来创建类了。
Foo=Mytype('Foo',(object,),{})

#另外，下面这种定义的类的方式默认都是用type来创建类的
class Foo(object):
    pass
# 如果要改成用我们自己定义的Mytype来创建类，需要做如下的修改：
class Foo(object,metaclass=Mytype):
    pass


##再继续看前面的用法：

class Mytype(type):
    def __init__(self,*args,**kwargs):
        print("init")
        super(Mytype,self).__init__(*args,**kwargs)  ##这句可以理解成什么都没做

    def __call__(cls, *args, **kwargs):
        print("call")
        return super(Mytype,cls).__call__(*args,**kwargs) ##这句可以理解成什么都没做


class Foo(object,metaclass=Mytype):  #创建这个对象时，可以看做是Mytype类的实例化，所以会执行__init__方法
    pass

obj=Foo()  #而实例化时，因为Foo是一个对象（可以看做是Mytype类的对象），对象+（）会执行Mytype类的__call__方法