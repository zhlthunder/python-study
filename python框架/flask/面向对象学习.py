#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 参考： https://www.cnblogs.com/maskice/p/6493404.html

# 继承 __init__
# 派生类默认不继承基类__init__，需要用super声明

class A:
    def __init__(self):
        self.name = "nick"

class B(A):
    def __init__(self):
        self.age = 18
        super(B, self).__init__()   #super首先找到B的父类A，然后把类B的对象self转换为类A的对象，然后“被转换”的类A对象调用自己的__init__函数
        # A.__init__(self)          #指定运行A中__init__，  实现的功能和上面完全相同，但不推荐使用

obj = B()
print(obj.__dict__)

#不使用super(B, self).__init__() 时：输出：{'age': 18}
#使用super(B, self).__init__() 时：输出： {'age': 18, 'name': 'nick'}