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

