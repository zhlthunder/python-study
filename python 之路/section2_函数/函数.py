#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 定义和使用
#
# def 函数名(参数):
#
#     ...
#     函数体
#     ...
#     返回值
#
# 函数的定义主要有如下要点：
#
#     def：表示函数的关键字
#     函数名：函数的名称，日后根据函数名调用函数
#     函数体：函数中进行一系列的逻辑计算，如：发送邮件、计算出 [11,22,38,888,2]中的最大数等...
#     参数：为函数体提供数据
#     返回值：当函数执行完毕后，可以给调用者返回数据。


##发送邮件代码实例（要先在163的邮箱设置中配置smtp 开启，实际验证ok）
# def sendmail():
#
#     import smtplib
#     from email.mime.text import MIMEText
#     from email.utils import formataddr
#
#
#     msg = MIMEText('邮件内容zhl', 'plain', 'utf-8')
#     msg['From'] = formataddr(["zhl",'zhlthunder@163.com'])
#     msg['To'] = formataddr(["hh",'510424723@qq.com'])
#     msg['Subject'] = "主题"
#
#     server = smtplib.SMTP("smtp.163.com", 25)
#     server.login("zhlthunder@163.com", "4281603")
#     server.sendmail('zhlthunder@163.com', ['510424723@qq.com',], msg.as_string())
#     server.quit()
#
# sendmail()
# print(123)


#范例2：
# def sendmail():
#
#     import smtplib
#     from email.mime.text import MIMEText
#     from email.utils import formataddr
#
#
#     try:
#         msg = MIMEText('邮件内容zhl', 'plain', 'utf-8')
#         msg['From'] = formataddr(["zhl",'zhlthunder@163.com'])
#         msg['To'] = formataddr(["hh",'510424723@qq.com'])
#         msg['Subject'] = "主题"
#
#         server = smtplib.SMTP("smtp.163.com", 25)
#         server.login("zhlthunder@163.com", "4281603")
#         server.sendmail('zhlthunder@163.com', ['510424723@qq.com',], msg.as_string())
#         server.quit()
#     except:
#             return False  #发送失败时执行此段代码
#     else:
#             return True   #发送陈宫时执行此段代码
#
# ret=sendmail()
# if ret==True:
#     print("发送成功")
# else:
#     print("发送失败")
#
##注意上面 try--except--else的用法；


##函数返回值
# def f1():
#     print(123)
#     return "1111"
#     print(12)  #此句永远不会被执行
#
# r=f1()
# print(r)
# 输出：
# 123
# 1111

#在函数中一旦执行return,函数执行过程立即终止；

#函数如果没有return语句，默认返回None;
# def f2():
#     print(123)
#
# ret=f2()
# print(ret)
#
# 输出：
# 123
# None

##函数之基本参数：
#形式参数，实参
# def sendmail(xxoo):
#
#     import smtplib
#     from email.mime.text import MIMEText
#     from email.utils import formataddr
#
#     try:
#         msg = MIMEText('邮件内容zhl', 'plain', 'utf-8')
#         msg['From'] = formataddr(["zhl",'zhlthunder@163.com'])
#         msg['To'] = formataddr(["hh",'510424723@qq.com'])
#         msg['Subject'] = "主题"
#
#         server = smtplib.SMTP("smtp.163.com", 25)
#         server.login("zhlthunder@163.com", "4281603")
#         server.sendmail('zhlthunder@163.com', [xxoo,], msg.as_string())
#         server.quit()
#     except:
#             return False
#     else:
#             return True
#
# while True:
#     em=input("请输入邮箱地址：")
#     ret=sendmail(em)
#     if ret==True:
#         print("发送成功")
#     else:
#         print("发送失败")


# def sendmail(xxoo,content):
#
#     import smtplib
#     from email.mime.text import MIMEText
#     from email.utils import formataddr
#
#     try:
#         msg = MIMEText(content, 'plain', 'utf-8')
#         msg['From'] = formataddr(["zhl",'zhlthunder@163.com'])
#         msg['To'] = formataddr(["hh",'510424723@qq.com'])
#         msg['Subject'] = "主题"
#
#         server = smtplib.SMTP("smtp.163.com", 25)
#         server.login("zhlthunder@163.com", "4281603")
#         server.sendmail('zhlthunder@163.com', [xxoo,], msg.as_string())
#         server.quit()
#     except:
#             return False
#     else:
#             return True
#
# while True:
#     em=input("请输入邮箱地址：")
#     ret=sendmail(em,"zhuhonglei")
#     if ret==True:
#         print("发送成功")
#     else:
#         print("发送失败")


# @@例子：

#type 1: 普通参数：
# def send(xxoo,content,xx):
#     print("发送邮件成功:",xxoo,content,xx)
#     return True
#
# while True:
#     em=input("请输入邮箱地址：")
#     ret=send(em,"SB","ok")
#     if ret==True:
#         print("发送成功")
#     else:
#         print("发送失败")
#
# 备注： 默认情况下，形式参数和实参是一一对应的。

#type 2: 默认参数：
#type 1: 普通参数：
# def send(xxoo,content,xx="hhhhh"):
#     print("发送邮件成功:",xxoo,content,xx)
#     return True
#
# while True:
#     em=input("请输入邮箱地址：")
#     ret=send(em,"SB","ok")  #传了三个参数，不使用默认参数；
#     ret=send(em,"SB")   #s使用默认参数
#     if ret==True:
#         print("发送成功")
#     else:
#         print("发送失败")


# #type 3:指定参数：
# def send(xxoo,content):
#     print("发送邮件成功:",xxoo,content)
#     return True
#
# send(content="zhl",xxoo="jack")  #使用指定参数时，就不需要按顺序写了


# 函数参数总结：
# 1.普通参数：一一对应；
# 2.默认参数； 但要注意，默认参数必须放到所有参数的最后，
#   send(xxoo,content,xx="hhhhh")  #这个写法是正确的；
#   send(xxoo,xx="hhhhh"，content)  #这个写法是错误的；
# 3.指定参数
# 4.动态参数：
#    1） *  默认将传入的参数全部放置在一个元祖中，让函数内部去使用； f1(*[11,22,33,44])
#    2）**  默认将传入的参数全部放入一个字典中，让函数内部去使用；  f1(**{"k1":"v1","k2":"v2"})
# 5.万能参数： f1(*args,**kwargs)   固定格式；


#使用一个*，就有超能力，可以接受N个参数，并放到一个元祖中；
# def f1(*args):
#     print(args,type(args))
#
# f1(11,22,'alex',"hhhh")
# 输出： (11, 22, 'alex', 'hhhh') <class 'tuple'>


# def f1(*args):
#     print(args,type(args))
# li=[11,22,"alex","hhhh"]
# f1(li)
# 输出： ([11, 22, 'alex', 'hhhh'],) <class 'tuple'>
# #即把列表作为元祖的一个元素传入；

# def f1(*args):
#     print(args,type(args))
# f1(11)
# li=[11,22,"alex","hhhh"]
# f1(li,12)
#
# 输出：
# (11,) <class 'tuple'>
# ([11, 22, 'alex', 'hhhh'], 12) <class 'tuple'>


# def f1(*args):
#     print(args,type(args))
# li=[11,22,"alex","hhhh"]
# f1(li)  #以普通的方式传参数时，会把所有的元素都加入到一个元祖中；
# f1(*li) #以这种方式传递时，会把列表中的每个元素都传递到元祖中；
# 输出：
# ([11, 22, 'alex', 'hhhh'],) <class 'tuple'>
# (11, 22, 'alex', 'hhhh') <class 'tuple'>

# def f1(*args):
#     print(args,type(args))
# li="alex"
# f1(*li)
#
# 输出：('a', 'l', 'e', 'x') <class 'tuple'>




#动态参数类型2： ** 时，传递的参数必须是k,v的键值对；
# def f1(**args):
#     print(args,type(args))
#
# # f1("alex")  #执行时报错：TypeError: f1() takes 0 positional arguments but 1 was given
# f1(n1="alex") #输出： {'n1': 'alex'} <class 'dict'>
# f1(n1="alex",n2=18) #输出：{'n1': 'alex', 'n2': 18} <class 'dict'>


# def f1(**args):
#     print(args,type(args))
#
# dic={'k1':"v1","k2":"v2"}
# f1(kk=dic)
# 输出：{'kk': {'k1': 'v1', 'k2': 'v2'}} <class 'dict'>


# def f1(**args):
#     print(args,type(args))
#
# dic={'k1':"v1","k2":"v2"}
# f1(**dic)
# 输出： {'k1': 'v1', 'k2': 'v2'} <class 'dict'>


#万能参数：
# def f1(*args,**kwargs):
#     print(args)
#     print(kwargs)
# f1(11,22,33,44,k1="v1",k2="v2")
# #默认会将11,22,33,44 封装到args中；将k1="v1",k2="v2" 封装到kwargs中；
# 输出：
# (11, 22, 33, 44)
# {'k1': 'v1', 'k2': 'v2'}


# str.format
# 比如python 内置函数的参数形式： def format(*args, **kwargs): # known special case of str.form


##python 中有两种字符串格式化：
# 1） %s,%d
# 2)format  ：应用了上面的万能参数；

#{0}和{1}位占位符；
# def format(*args, **kwargs)
# s1="i am {0}, age {1}".format("alex",18)  #format定义时有两种参数，但传输一种参数也可以；
# s2="i am {0}, age {1}".format(*["alex",18])
# print(s1)
# print(s2)
# 输出：
# i am alex, age 18
# i am alex, age 18

# s1="i am {name}, age {age}".format(name="alex",age=11)
# print(s1)
# dic={"name":"alex","age":11}
# s2="i am {name}, age {age}".format(**dic)
# print(s2)
# 输出：
# i am alex, age 11
# i am alex, age 11


#函数内容补充1：


# def f1(a1,a2):
#     return a1+a2
# #f1指向 a1+a2的内存空间，此空间会变成没有使用的空间，python 会定期进行自动回收；
# def f1(a1,a2):
#     return a1*a2
# #f1指向a1*a2的内存空间；
# ret=f1(8,8)  #指向后来定义的空间中；
# print(ret)
# # 输出：64

# #原理同上
# name="alex"
# name="eric"
# print(name)


#函数内容补充2：
#python传递参数时传递的是 引用，不是重新复制一份值；
# def f1(a1):
#     a1.append(999)
#
# li=[11,22,33,44]
# f1(li)
# print(li)
# # 输出：
# [11, 22, 33, 44, 999]

##局部变量：
# def f1():
#     name="alex" ##只在f1内部有效
# def f2():
#     name="eric"  ##只在f2内部有效

##全局变量：

#全局变量：在所有的作用域都可读；

# name="alex"
# def f1():
#     name="tom" #当局部变量和全局变量相同时，优先使用局部变量
#     print(name)
# f1()
#
# 输出：
# tom


# name="alex"
# def f1():
#     age=18
#     name="123"  # 此处只能看成是新定义的局部变量，而无法修改全局的name,
#     print(age,name)
#
# def f2():
#     age=22
#     print(age,name)
#
# f1()
# f2()
# 输出：
# 18 123
# 22 alex


# name="alex"
# def f1():
#     age=18
#     global name #表示name是个全局变量，然后就可以把全局变量给修改了
#     name="123"
#     print(age,name)
#
# def f2():
#     age=22
#     print(age,name)
#
# f1()
# f2()
# 输出：
# 18 123
# 22 123



##重要，对于像列表，字典这样数据类型的全局变量，可以在子函数中直接进行append,不需要事先声明global,但不可以重新赋值 name="123"
# name=[11,22,33,44]
# def f1():
#     age=18
#     print(name)
#     name.append(999) #可以执行添加元素
#                          #name="123"   这个是错误的，无法重新赋值
#     print(name)
#
# f1()
# 输出：
# [11, 22, 33, 44]
# [11, 22, 33, 44, 999]

#备注总结：
# 1.全局变量全部作用域可读，
# 对全局变量进行重新赋值，需要先global一下；
# 特殊的：像列表，字典等特殊数据类型，可修改（增删改），但不可以重新赋值；@@@@@重要
#潜规则：  所用全局变量都要大写；@@@@重要

# name=[11,22,33,44]
# print(name)
# def f1():
#     name.remove(44) #可以执行添加元素
# f1()
# print(name)
# 输出：
# [11, 22, 33, 44]
# [11, 22, 33]


# name=[11,22,33,44]
# print(name)
# def f1():
#     name[0]=1111 #可以执行添加元素
# f1()
# print(name)
# 输出：
# [11, 22, 33, 44]
# [1111, 22, 33, 44]



##函数的几种调用方式的对比：
#1使用动态参数的方式传递的列表，在函数中会自动生成元祖，即只可以读，不可以修改，切记；
# def f1(*args):
#     print(args,type(args))
#
# li=[11,22,33]
# f1(*li)
#输出：
#(11, 22, 33) <class 'tuple'>

#2：通过普通参数传递列表时，传递的是应用，即子函数中的列表和传递的列表是同一个，切类型是列表，可以进行修改操作，且在子函数中修改时，会同时影响调用的列表，因为它们指向相同的内存空间

# def f1(args):
#     print(args,type(args))
#     args.append(44)
#     print(args)
# li=[11,22,33]
# f1(li)
# print(li)
# 输出：
# [11, 22, 33] <class 'list'>
# [11, 22, 33, 44]
# [11, 22, 33, 44]

#3.通过全局变量列表，实现在子函数中操作和修改列表中元素；
# NAME=[11,22,33]
# def f1():
#     print(NAME,type(NAME))
#     NAME.append(44)
# f1()
# print(NAME)
# 输出：
# [11, 22, 33] <class 'list'>
# [11, 22, 33, 44]

#@注意摸索以上几种方式，在和子函数交互时对列表的修改方式；


#以后我们编程时，常用的架构如下：
# 定义全局变量
#
# def xx
#
# def xx
#
# def xx
#
# def main():
#     xxx
#
# main（）