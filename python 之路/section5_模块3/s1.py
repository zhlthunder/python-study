#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 相关博客：
# http://www.cnblogs.com/wupeiqi/articles/5501365.html


# 内置模块是Python自带的功能，在使用内置模块相应的功能时，需要【先导入】再【使用】
# sys : 用于提供对Python解释器相关的操作,即和pYthon 解释器相关的模块；

import sys

# sys.argv           命令行参数List，第一个元素是程序本身路径
# sys.exit(n)        退出程序，正常退出时exit(0)
# sys.exit("异常退出")   ##退出并输出 “异常退出”
# sys.version        获取Python解释程序的版本信息
# sys.maxint         最大的Int值
# sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform       返回操作系统平台名称
# sys.stdin          输入相关
# sys.stdout         输出相关
# sys.stderror       错误相关

##实例：进度百分比

# print("%d%%"% 1)   #  输出： 1%

##ver1:
# import sys
# import time
#
# def view_bar(num, total):
#     # rate = float(num) / float(total) ##用于python2，需要用float
#     rate = num/total  ##用于python3
#     rate_num = int(rate * 100)  #转换成百分数
#     r = '%d%%' % (rate_num)
#     print(r)
#
# if __name__ == '__main__':
#     for i in range(0, 101):
#         time.sleep(0.1)  ##延时
#         view_bar(i, 100)


##ver2
# import sys
# import time
#
# def view_bar(num, total):
#     # rate = float(num) / float(total) ##用于python2，需要用float
#     rate = num/total  ##用于python3
#     rate_num = int(rate * 100)  #转换成百分数
#     r = '%d%%' % (rate_num)
#     sys.stdout.write(r)  #也是输出到屏幕，和print的区别是，print每次输出会在最好默认加上\n 换行符
#     sys.stdout.flush() ##输出后会清空一下
#
# if __name__ == '__main__':
#     for i in range(0, 101):
#         time.sleep(0.1)  ##延时
#         view_bar(i, 100)

##这样会输出一行，没有在同一个位置输出；


##ver3
# import sys
# import time
#
# def view_bar(num, total):
#     # rate = float(num) / float(total) ##用于python2，需要用float
#     rate = num/total  ##用于python3
#     rate_num = int(rate * 100)  #转换成百分数
#     r = '\r%d%%' % (rate_num, )  ##加上\r退格，即每次都退到当前行的开始位置
#     sys.stdout.write(r)  #也是输出到屏幕，和print的区别是，print每次输出会在最好默认加上\n 换行符
#     sys.stdout.flush() ##输出后会清空一下,经验证，没有这句实现效果相同，推测可能和跨平台有关，跨平台时可能需要
#
# if __name__ == '__main__':
#     for i in range(0, 101):
#         time.sleep(0.1)  ##延时
#         view_bar(i, 100)


##ver4，@@最终版本
# import sys
# import time
#
# def view_bar(num, total):
#     # rate = float(num) / float(total) ##用于python2，需要用float
#     rate = num/total  ##用于python3
#     rate_num = int(rate * 100)  #转换成百分数
#     r = '\r%s>%d%%' % ("-"*num,rate_num, )  ##加上\r退格，即每次都退到当前行的开始位置
#     sys.stdout.write(r)  #也是输出到屏幕，和print的区别是，print每次输出会在最好默认加上\n 换行符
#     sys.stdout.flush() ##输出后会清空一下,经验证，没有这句实现效果相同，推测可能和跨平台有关，跨平台时可能需要
#
# if __name__ == '__main__':
#     for i in range(0, 101):
#         time.sleep(0.1)  ##延时
#         view_bar(i, 100)

# 输出：
# ---------------------------------------------------------------------------------------------------->100%




#os模块 ： 用于提供系统级别的操作：
# os.getcwd()                 获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir("dirname")         改变当前脚本工作目录；相当于shell下cd
# os.curdir                   返回当前目录: ('.')
# os.pardir                   获取当前目录的父目录字符串名：('..')
# os.makedirs('dir1/dir2')    可生成多层递归目录
# os.removedirs('dirname1')   若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')         生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')         删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.listdir('dirname')       列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove()                 删除一个文件
# os.rename("oldname","new")  重命名文件/目录
# os.stat('path/filename')    获取文件/目录信息，比如在socket编程时，会用文件大小；
# os.sep                      操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# os.linesep                  当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# os.pathsep                  用于分割文件路径的字符串
# os.name                     字符串指示当前使用平台。win->'nt'; Linux->'posix'
# os.system("bash command")   运行shell命令，直接显示
# os.environ                  获取系统环境变量
# os.path.abspath(path)       返回path规范化的绝对路径  -----@@重要
# os.path.split(path)         将path分割成目录和文件名二元组返回
# os.path.dirname(path)       返回path的目录。其实就是os.path.split(path)的第一个元素  ----@@重要
# os.path.basename(path)      返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)        如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)         如果path是绝对路径，返回True
# os.path.isfile(path)        如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)         如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略 ---@@重要
# os.path.getatime(path)      返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)      返回path所指向的文件或者目录的最后修改时间



# import os
# print(os.pathsep)  #输出为";",其它的特殊符号定义如下：
# These are primarily for export; internally, they are hardcoded.
# curdir = '.'
# pardir = '..'
# extsep = '.'
# sep = '\\'
# pathsep = ';'
# altsep = '/'
# defpath = '.;C:\\bin'
# devnull = 'nul'





##加密模块
# hashlib  用于加密相关的操作，代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
##重要： md5是不可逆的，即可以正向加密，但不可以反向解密；
# 虽然不可以反解回来，但可以都转换成密码进行比较；
# 即比如用户登录时，要检查用户名和密码是否正确，既然不可以用明文进行比较，那就用密码进行比较，即把用户输入的用户名和密码用
# md5编码方式转换成密文后，再与数据库中保存的用户账户信息的密文进行比较就可以了
#因为md5的加密规则是一定的，即只要明文相同，那密文就必然相同


##1 ： # ######## md5 加密 ########
import hashlib

hash = hashlib.md5()
# hash.update("admin") ##python2.7 就用这种方式进行加密
hash.update(bytes('123', encoding='utf-8'))  ##用于python3
ret=hash.hexdigest() #获取加密后的值；
print(ret)
# 输出：
# 202cb962ac59075b964b07152d234b70  #这就是123 用md5加密后的值

##此时又引入新的问题，如果所有的内容都是用这种方式进行加密，虽然不可以反解，但可以生成常用字符串的
# md5加密后的密文库，然后采用查找密文的方法来反推被加密的信息，即为所谓的 撞库

##如何提高加密的等级呢？ 即这种方式相对来说加密等级比较高了，这也是我们最常用的方式
# @@重要
import hashlib

hash = hashlib.md5(bytes("asdfafaf",encoding="utf-8")) ##加入一个额外的基础加密key
# hash.update("admin") ##python2.7 就用这种方式进行加密
hash.update(bytes('123', encoding='utf-8'))  ##用于python3
ret=hash.hexdigest() #获取加密后的值；
print(ret)
# 输出：
# 7659ead65e8caf6a9aa7b5f5f5b81353  #此为123 在基础加密key 之上 再用md5加密后获得的值；


# 除了md5外，其他的加密的方法，以下的内容了解，需要时查询，主要掌握上面的MD5加密；
######## sha1 ########

hash = hashlib.sha1()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha256 ########

hash = hashlib.sha256()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())


# ######## sha384 ########

hash = hashlib.sha384()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# 以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。

import hashlib

# ######## md5 ########

hash = hashlib.md5(bytes('898oaFs09f',encoding="utf-8"))
hash.update(bytes('admin',encoding="utf-8"))
print(hash.hexdigest())

# python内置还有一个 hmac 模块，它内部对我们创建 key 和 内容 进行进一步的处理然后再加密

import hmac

h = hmac.new(bytes('898oaFs09f',encoding="utf-8"))
h.update(bytes('admin',encoding="utf-8"))
print(h.hexdigest())