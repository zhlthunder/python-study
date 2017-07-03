#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

  # 参考文档：
  #
  #            1、金角大王博客：http://www.cnblogs.com/alex3714/articles/5188179.html
  #
  #            2、银角大王博客：http://www.cnblogs.com/wupeiqi/articles/5017742.html


# 1、反射之__import__:
#
#         我们知道import语句是用来导入外部模块的，当然还有from...import...也可以，但是其实import实际上是使用builtin函数__import__来工作的。
#         在一些程序中，我们可以动态地去调用函数，如果我们知道模块的名称(字符串)的时候，我们可以很方便的使用动态调用。
#
# __import__(module_name[, globals[, locals[, fromlist]]]) #可选参数默认为globals(),locals(),[]
# __import__('os')
# __import__('os',globals(),locals(),['path','pip'])  #等价于from os import path, pip

#
# 例： 以字符串的形式导入模块
#
# mod = __import__('sys')
# print(mod.path)
#
# 例：以字符串的形式调用模块中的函数
#
# func = getattr(mod,'path')
# print(func)
#
# 例：从一个包中导入一个模块 ，包名为main，模块名为mod
#
# aa = __import__('main.mod')
#
# aa = __import__('main', globals={}, locals={}, fromlist=['mod'])
#
# aa = __import__('main',globals(),locals(),['mod'])
#
# m = getattr(aa, 'mod')
# print(m.first('kevin'))
#
# n = getattr(m, 'first')
# print(type(n))
# n('kevin')

# 注：web框架中根据不同的URL，来加载不同的模块，进行不同的处理。


# 2、类与对象：
#
#         __init__ 的方法 完成初始化。构造函数
#
#         __del__ 的方法 对象销毁，析构函数
#
#        __call__ 调用方法
#
#        所有的实例方法都拥有一个 self 参数来传递当前实例，类似于 this。
#        可以使用 __class__ 来访问类型成员。
#
#        还有些内置特殊的属性：
#
#               __doc__   #类型帮助信息
#
#               __name__ # 类型名称
#
#               __module__ # 类型所在模块
#               __bases__ # 类型所继承的基类
#
#               __dict__ # 类型字典，存储所有类型成员信息。



class peason(object):
    '''this is peason class'''
    #静态字段
    aa = 'nihao'
    bb = ['a',1,'b',2,'c',3]
    cc = {'a':'wangkai','b':'gonghui'}

    def __init__(self,name,flag):
        self.name = name                             #动态字段
        self.__flag = flag                               #私有字段


    def __del__(self):
        print('i will go')

    def __call__(self,caa):                            #call方法
        print('this is call method',caa)


    def __priv(self):                                    #私有方法
        print('hello,this is privacy method',self.__flag)


    def first(self):                                       #动态方法
        print('hello,this is dymamic method',self.name)
        self.__priv()                                     #调用私有方法
        return self.__flag                              #调用私有字段

    @staticmethod                                     #静态方法
    def foo():
        print('this is static method')

    @property                                           #属性
    def bar(self):
        print(self.name)
        self.__priv()
        return "this is property"

    @property                                         #属性(只读）

    def flag(self):
        return self.__flag

    @flag.setter                                       #修改私有字段值
    def flag(self,value):
        self.__flag = value

print('#################')
print(peason.__doc__,peason.__name__,peason.__module__,peason.__bases__,peason.__dict__)
print('#################')
print(peason.aa,peason.bb,peason.cc)         #获取静态字段
print('#################')
print(peason.foo())                                    #获取静态方法
print('#################')
pp = peason('wang','true')                         #类实例化
print(pp.name)                                         #通过对象获取动态字段
print('#################')
print(pp.first())                                          #通过对象获取动态方法
print('#################')
print(pp.bar)                                             #通过对象获取属性
print('#################')
print(pp._peason__priv())                          #特殊调用方式
print('#################')
print(pp.flag)
pp.flag = 'false'                                         #通过属性修改私有字段值
print(pp.flag)

pp('aa')                                                      #call方法调用


# 注：静态的可以直接通过类来访问，而动态的只能通过调用对象的方式来访问；
#
#        私有字段和方法能通过方法和属性调用；
#
#        只读或只写的字段，修改需要@flag.setter 和 class peason(object):来实现



# 3、继承：
#
# Python编程中类可以承继父类属性，形式为class 类名（父类），子类可以继承父类的所有方法和属性，也可以重载父类的成
# 员函数及属性，须注意的是子类成员函数若重载父类（即名字相同），则会使用子类成员函数

class SchoolMember(object):
    members = 0 #初始学校人数为0
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def  tell(self):
        pass

    def enroll(self):
        '''注册'''
        SchoolMember.members +=1
        print("\033[32;1mnew member [%s] is enrolled,now there are [%s] members.\033[0m " %(self.name,SchoolMember.members))

    def __del__(self):
        '''析构方法'''
        print("\033[31;1mmember [%s] is dead!\033[0m" %self.name)

class Teacher(SchoolMember):
    def __init__(self,name,age,course,salary):
        super(Teacher,self).__init__(name,age)
        self.course = course
        self.salary = salary
        self.enroll()


    def teaching(self):
        '''讲课方法'''
        print("Teacher [%s] is teaching [%s] for class [%s]" %(self.name,self.course,'s12'))

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' %(self.name,'Oldboy', self.course)
        print(msg)

class Student(SchoolMember):
    def __init__(self, name,age,grade,sid):
        super(Student,self).__init__(name,age)
        self.grade = grade
        self.sid = sid
        self.enroll()


    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' %(self.name, self.grade,'Oldboy')
        print(msg)

if __name__ == '__main__':
    t1 = Teacher("Alex",22,'Python',20000)
    t2 = Teacher("TengLan",29,'Linux',3000)

    s1 = Student("Qinghua", 24,"Python S12",1483)
    s2 = Student("SanJiang", 26,"Python S12",1484)

    t1.teaching()
    t2.teaching()
    t1.tell()

        #    新式类以object为基类，在python3之后版本原来有经典类将不在使用，而且新式类的多类继承是以广度代替了经典类的深度搜索方式。
        #
        # 例，A、B、C、D四个类，其中B和C继承A，D又继承B和C，即class D(B,C)
        #
        # 继承的方法：
        #
        #       经典类的搜索顺序是B，A，C     搜索到第一个方法结束
        #
        #       新式类的搜索顺序是B,C。


    # 例：经典类写法
#     class A(object):
#     def __init__(self):
#         print('this is class A')
#     def test(self):
#         print('this is parent test')
#
# class B(A):
#     def __init__(self):
#         print('this is class B')
#
# class C(A):
#     def __init__(self):
#         print('this is class C')
#     def test(self):
#         print('this is son C test')
#
# class D(B,C):
#     def __init__(self):
#         print('this is class D')
#
# R = D()
# R.test()
#
# 经典类写法结果为：
#
# this is class D
# this is parent test
#
# 新式类写法结果为：
#
# this is class D
# this is son C test


# 4、抽象类+抽象方法 = 接口 （用于规范）
#
# 由于python 没有抽象类、接口的概念，所以要实现这种功能得abc.py 这个类库,
#
# 抽象基类（或者ABCs）是Python里一个相同的特性。抽象基类由abc模块构成，包含了一个叫做ABCMeta的metaclass。这个metaclass由内置的isinstance()和issubclass()特别处理
#
# 具体方式如下：

from abc import ABCMeta,abstractmethod
from _pyio import __metaclass__

class headers(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        print('this is abc class')

    @abstractmethod
    def fun(self):
        pass

class foo(headers):
    def __init__(self):
        print('__init__')

    def fun(self):
        print('foo.fun')

f = foo()
f.fun()