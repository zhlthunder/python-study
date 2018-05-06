#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

#1.获取类中私有字段的方法说明


#共有方法和共用字段，内部外部都可以访问
#私有字段，内部可以访问，外部可以访问

#面向对象，私有属性的问题， __age
# class  Foo(object):
#     def __init__(self):
#         self.name='tom'
#         self.__age=18  ##
#
# obj=Foo()
# print(obj.name)
# print(obj.__age) ##这条命令执行时会报错：
# AttributeError: 'Foo' object has no attribute '__age'
#即类的私有属性，在外面是无法访问的，如果要方法，可以用下面的方法：


# class  Foo(object):
#     def __init__(self):
#         self.name='tom'
#         self.__age=18  ##
#
#     def get_age(self):
#         return self.__age
#
# obj=Foo()
# print(obj.get_age())




##私有字段，另外的一个获取的方法如下：

class  Foo(object):
    def __init__(self):
        self.name='tom'
        self.__age=18  ##


obj=Foo()
print(obj._Foo__age)  #用这种方法也可以获取到。



##面向对象中with的用法

#需求： 做一次数据库操作，不用数据库连接池

#正常的使用流程如下，需要经历 打开，操作，关闭的流程
class SQLHelper(object):
    def open(self):
        pass
    def fetch(self,sql):
        pass
    def close(self):
        pass

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

obj=Foo()
obj.open()
obj.fetch("select ****")
obj.close()


##还是上面的需求，我们可以使用下面的方法来进行
class SQLHelper(object):
    def open(self):
        pass
    def fetch(self,sql):
        pass
    def close(self):
        pass

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


with SQLHelper() as obj:   #这个语法会自动调用类中的__enter__方法, obj为这个方法的返回值，可以随意命名
    obj.fetch("selec ****")
    #当执行完毕后，会自动调用类的__exit__方法
#以后如果遇到类似的需求，比如文件的操作，那么源码中都支持者两种方法：
##支持手动的打开和关闭，也支持使用with的方法，  比如我们使用的文件的操作，切记！！！！！

