#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 面向对象编程即OOP，适合于开发大型项目；
# 类：具有某种特征的事物的集合
# 对象：类里面的个体
# 类是抽象的，对象是具体的
# 对象为类的实例化，即从抽象到具体

# 创建一个类的格式
# class 类名:
#     类里面的内容

class cl1:
    pass

print(cl1)
# 输出： <class '__main__.cl1'>
# 即此时cl1就是一个类

##创建一个对象，即实例化一个类
a=cl1()
print(a)
# 输出：<__main__.cl1 object at 0x000002C1F8DC9128>
# 即此是一个对象

# 构造函数：类在实例化的时候自动首先触发执行的方法
##构造函数的名字
# __init__(参数)
##self 参数：类中的所有方法，第一个参数必须是self,否则会报错


class cl2:
    def __init__(self):
        print("i am cl2 self")

b=cl2()
# 输出： i am cl2 self
# 即类实例化的时候，会自动的触发执行，所以构造函数经常用来进行初始化的操作

##给类加上参数，实际上就是在构造方法上加上参数

class cl3:
    def __init__(self,name,job):
        print("my name is "+name,"my job is "+job)

c=cl3('jack','engineer')
# 输出：my name is jack my job is engineer
c2=cl3('tom','teacher')
# 输出：my name is tom my job is teacher
# 同样是实例化的时候自动执行，但需要传参数，注意


# 属性和方法
# 属性：静态的特征，比如，头发，手臂等
# 方法：动态的特征，比如 唱歌，写字等

#属性：就是类里面的变量,定义的方法： self.属性名
class cl4:
    def __init__(self,name,job):
        self.myname=name
        self.myjob=job

d=cl4('alex','poster')
print(d.myname)
print(d.myjob)
# 输出：
# alex
# poster
# 即实例化后，对象就有了myname,myjob两个属性

#方法：就是类里面的函数， def 方法名（self,参数）

class cl5:
    def myfunc1(self):
        print("hello cl5")
    def myfunc2(self,name):
        print("hello "+name)
e=cl5()
e.myfunc1()
e.myfunc2("thunder")
# 输出：
# hello cl5
# hello thunder
# 即方法也通过 “对象.方法名()”来调用，
#如果方法定义时有附加参数，需要再执行的时候附带参数才可以；
#请注意，构造函数有附加参数时，在实例化的时候传参数；方法有附加参数时，在执行的时候传参数；

class cl6:
    def __init__(self,name):
        self.myname=name

    def myfunc1(self):
        print("hello"+self.myname)

f=cl6('ttony')
f.myfunc1()
# 输出：
# hellottony
# 这是另外一种使用方法，方法和属性结合的方式，在方法中直接调用属性的形式


#类的继承和重载
#继承：把一个或多个类（基类）的特征拿过来
#重载：在子类（派生类）里面对继承过来的特征进行重新定义
# 父类：基类
# 子类：派生类


#继承：单继承（父类只有一个），多继承（父类为多个）
#某一个家庭，有父亲，母亲，儿子，女儿，父亲可以说话，母亲可以写字，儿子继承了父亲，
# 女儿同时继承了父亲和母亲，并且具有新能力，小儿子继承了父亲，但进行了优化

#父类
class father:
    def speak(self):
        print("i can speak")
#子类
class son1(father):
    pass
s=son1()
s.speak()
# 输出：
# i can speak
#即因为儿子继承了父亲，所以有了speak的方法；

#母亲类
class mother:
    def write(self):
        print("i can write")
class daughter(father,mother):
    def listen(self):
        print("i can listen")

dd=daughter()
dd.speak()
dd.write()
dd.listen()
# 输出：
# i can speak
# i can write
# i can listen
# 即女儿有三个方法

##重载
class son2(father):
    def speak(self): #和父类中的方法同名，就会覆盖父亲中的方法
        print("i can speak 2")

ss=son2()
ss.speak()
# 输出：
# i can speak 2
# 即进行了重载







