#!/usr/bin/env python
# -*- coding: utf-8 -*-


# python 知识学习博客  http://www.cnblogs.com/wupeiqi/articles/5433893.html
#from : http://www.cnblogs.com/alex3714/articles/5465198.html
#python 简介：
# Python 是一门什么样的语言？
# 编程语言主要从以下几个角度为进行分类，编译型和解释型、静态语言和动态语言、强类型定义语言和弱类型定义语言，每个分类代表什么意思呢，我们一起来看一下。
# 编译和解释的区别是什么？
#
# 编译器是把源程序的每一条语句都编译成机器语言,并保存成二进制文件,这样运行时计算机可以直接以机器语言来运行此程序,速度很快;
#
# 而解释器则是只在执行程序时,才一条一条的解释成机器语言给计算机来执行,所以运行速度是不如编译后的程序运行的快的.
#
# 这是因为计算机不能直接认识并执行我们写的语句,它只能认识机器语言(是二进制的形式)
#
# 编译型vs解释型
#
# 编译型
# 优点：编译器一般会有预编译的过程对代码进行优化。因为编译只做一次，运行时不需要编译，所以编译型语言的程序执行效率高。可以脱离语言环境独立运行。
# 缺点：编译之后如果需要修改就需要整个模块重新编译。编译的时候根据对应的运行环境生成机器码，不同的操作系统之间移植就会有问题，需要根据运行的操作系统环境编译不同的可执行文件。
#
# 解释型
# 优点：有良好的平台兼容性，在任何环境中都可以运行，前提是安装了解释器（虚拟机）。灵活，修改代码的时候直接修改就可以，可以快速部署，不用停机维护。
#
# 缺点：每次运行的时候都要解释一遍，性能上不如编译型语言。

# 强类型定义语言和弱类型定义语言
#
# （1）强类型定义语言：强制数据类型定义的语言。也就是说，一旦一个变量被指定了某个数据类型，如果不经过强制转换，那么它就永远是这个数据类型了。举个例子：如果你定义了一个整型变量a,那么程序根本不可能将a当作字符串类型处理。强类型定义语言是类型安全的语言。
#
# （2）弱类型定义语言：数据类型可以被忽略的语言。它与强类型定义语言相反, 一个变量可以赋不同数据类型的值。
#
# 强类型定义语言在速度上可能略逊色于弱类型定义语言，但是强类型定义语言带来的严谨性能够有效的避免许多错误。另外，“这门语言是不是动态语言”与“这门语言是否类型安全”之间是完全没有联系的！
# 例如：Python是动态语言，是强类型定义语言（类型安全的语言）; VBScript是动态语言，是弱类型定义语言（类型不安全的语言）; JAVA是静态语言，是强类型定义语言（类型安全的语言）。


# 通过上面这些介绍，我们可以得出，python是一门动态解释性的强类型定义语言。那这些基因使成就了Python的哪些优缺点呢？我们继续往下看。

# Python的优缺点
# 先看优点
#
#     Python的定位是“优雅”、“明确”、“简单”，所以Python程序看上去总是简单易懂，初学者学Python，不但入门容易，而且将来深入下去，可以编写那些非常非常复杂的程序。
#     开发效率非常高，Python有非常强大的第三方库，基本上你想通过计算机实现任何功能，Python官方库里都有相应的模块进行支持，直接下载调用后，在基础库的基础上再进行开发，大大降低开发周期，避免重复造轮子。
#     高级语言————当你用Python语言编写程序的时候，你无需考虑诸如如何管理你的程序使用的内存一类的底层细节
#     可移植性————由于它的开源本质，Python已经被移植在许多平台上（经过改动使它能够工 作在不同平台上）。如果你小心地避免使用依赖于系统的特性，那么你的所有Python程序无需修改就几乎可以在市场上所有的系统平台上运行
#     可扩展性————如果你需要你的一段关键代码运行得更快或者希望某些算法不公开，你可以把你的部分程序用C或C++编写，然后在你的Python程序中使用它们。
#     可嵌入性————你可以把Python嵌入你的C/C++程序，从而向你的程序用户提供脚本功能。
#
# 再看缺点：
#
#     速度慢，Python 的运行速度相比C语言确实慢很多，跟JAVA相比也要慢一些，因此这也是很多所谓的大牛不屑于使用Python的主要原因，但其实这里所指的运行速度慢在大多数情况下用户是无法直接感知到的，必须借助测试工具才能体现出来，比如你用C运一个程序花了0.01s,用Python是0.1s,这样C语言直接比Python快了10倍,算是非常夸张了，但是你是无法直接通过肉眼感知的，因为一个正常人所能感知的时间最小单位是0.15-0.4s左右，哈哈。其实在大多数情况下Python已经完全可以满足你对程序速度的要求，除非你要写对速度要求极高的搜索引擎等，这种情况下，当然还是建议你用C去实现的。
#     代码不能加密，因为PYTHON是解释性语言，它的源码都是以名文形式存放的，不过我不认为这算是一个缺点，如果你的项目要求源代码必须是加密的，那你一开始就不应该用Python来去实现。
#     线程不能利用多CPU问题，这是Python被人诟病最多的一个缺点，GIL即全局解释器锁（Global Interpreter Lock），是计算机程序设计语言解释器用于同步线程的工具，使得任何时刻仅有一个线程在执行，Python的线程是操作系统的原生线程。在Linux上为pthread，在Windows上为Win thread，完全由操作系统调度线程的执行。一个python解释器进程内有一条主线程，以及多条用户程序的执行线程。即使在多核CPU平台上，由于GIL的存在，所以禁止多线程的并行执行。关于这个问题的折衷解决方法，我们在以后线程和进程章节里再进行详细探讨。
#
#
#
# 当然，Python还有一些其它的小缺点，在这就不一一列举了，我想说的是，任何一门语言都不是完美的，都有擅长和不擅长做的事情，建议各位不要拿一个语言的劣势去跟另一个语言的优势来去比较，语言只是一个工具，是实现程序设计师思想的工具，就像我们之前中学学几何时，有的时候需要要圆规，有的时候需要用三角尺一样，拿相应的工具去做它最擅长的事才是正确的选择。之前很多人问我Shell和Python到底哪个好？我回答说Shell是个脚本语言，但Python不只是个脚本语言，能做的事情更多，然后又有钻牛角尖的人说完全没必要学Python, Python能做的事情Shell都可以做，
# 只要你足够牛B,然后又举了用Shell可以写俄罗斯方块这样的游戏，对此我能说表达只能是，不要跟SB理论，SB会把你拉到跟他一样的高度，然后用充分的经验把你打倒。

#
# Python解释器
# 当我们编写Python代码时，我们得到的是一个包含Python代码的以.py为扩展名的文本文件。要运行代码，就需要Python解释器去执行.py文件。
#
# 由于整个Python语言从规范到解释器都是开源的，所以理论上，只要水平够高，任何人都可以编写Python解释器来执行Python代码（当然难度很大）。事实上，确实存在多种Python解释器。
# CPython
#
# 当我们从Python官方网站下载并安装好Python 2.7后，我们就直接获得了一个官方版本的解释器：CPython。这个解释器是用C语言开发的，所以叫CPython。在命令行下运行python就是启动CPython解释器。
#
# CPython是使用最广的Python解释器。教程的所有代码也都在CPython下执行。



#@@@@@@@@@@@@@@@@@@@@@@@@@@
# py2与3的详细区别
# 1）PRINT IS A FUNCTION
#
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study>python2
# Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print "hello world"
# hello world


# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study>python3
# Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print ("hello world")
# hello world
# >>>

# 2)ALL IS UNICODE NOW
#
# 从此不再为讨厌的字符编码而烦恼

#将编译器切换到python3后（settings--project interpreter ），就可以直接打印 中文了。
# print("你好")
#
# 3）还可以这样玩： (A,*REST,B)=RANGE(5)

# 4）某些库改名了



# @@变量：
# name = "Alex Li"
#
# name2 = name
# print(name,name2)
#
# name = "Jack"
# print(name,name2)

#备注： 注意name2的值不变；

# @@字符编码：
# python解释器在加载 .py 文件中的代码时，会对内容进行编码（默认ascill）
#
# ASCII（American Standard Code for Information Interchange，美国标准信息交换代码）是基于拉丁字母的一套电脑编码系统，
# 主要用于显示现代英语和其他西欧语言，其最多只能用 8 位来表示（一个字节），即：2**8 = 256-1，所以，ASCII码最多只能表示 255 个符号。
#
# 显然ASCII码无法将世界上的各种文字和符号全部表示，所以，就需要新出一种可以代表所有字符和符号的编码，即：Unicode
#
# Unicode（统一码、万国码、单一码）是一种在计算机上使用的字符编码。Unicode 是为了解决传统的字符编码方案的局限而产生的，它为每种语言中的每个字符
# 设定了统一并且唯一的二进制编码，规定虽有的字符和符号最少由 16 位来表示（2个字节），即：2 **16 = 65536，
# 注：此处说的的是最少2个字节，可能更多
#
# UTF-8，是对Unicode编码的压缩和优化，他不再使用最少使用2个字节，而是将所有的字符和符号进行分类：ascii码中的内容用1个字节保存、欧洲的字符用2个字节保存，
# 东亚的字符用3个字节保存...
#==》 即汉字使用3个字节；


# #python2 默认使用 ascill进行编码，所以在python2中执行下面的代码会报错：
# 报错：ascii码无法表示中文
# #!/usr/bin/env python
#
# print "你好，世界"
#
#
# 改正：应该显示的告诉python解释器，用什么编码来执行源代码，即：
#
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# print "你好，世界"
#
# #python3 默认使用unicode的编码方式，所以对中文是默认支持的，再也不需要担心字符编码的问题了



# @@格式化字符串
# 备注：
# python2 使用 raw_input, 如果使用input,输入的字符串会被当成变量，所以不使用input
# python3中使用input
#input 默认输入的都是字符串，如果要获得数字，需要使用int 方法；
# name=input("input your name:")
# #convert str to int
# age=int(input("input your age:"))
# job=input("input your job:")
#
# msg='''
# information of user %s:
# -----------------------
# Name: %s
# Age: %d
# Job: %s
# ---------END-----------
# ''' %(name,name,age,job)
# print(msg)


#
# @@注释：
# 　单行注视：# 被注释内容
#
# 　多行注释：""" 被注释内容 """

# # @@用户输入：
# import getpass
#
# # 将用户输入的内容赋值给 name 变量
# pwd = getpass.getpass("请输入密码：")
#
# # 打印输入的内容
# print(pwd)

# getpass说明：
# 1.getpass在pycharm下无法使用；
# 2.getpass在python3 {linux 下或 windows的命令行下}可以使用；
# 3.getpass 在python2下不是密文，是明文的；
#
# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study>python3
# Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import getpass
# >>> pwd=getpass.getpass("请请输输入入密密码码：：")
# 请请输输入入密密码码：：
# >>> print (pwd)
# 123

#
# @@模块初识
# Python的强大之处在于他有非常丰富和强大的标准库和第三方库，几乎你想实现的任何功能都有相应的Python库支持，以后的课程中会深入讲解常用到的各种库，现在，我们先来象征性的学2个简单的。
#
# @sys模块：
# test.py:
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# import sys
#
# print(sys.argv)
#
# #输出
# $ python test.py helo world
# ['test.py', 'helo', 'world']  #把执行脚本时传递的参数获取到了

# @@os
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# import os
# #
# os.system("df -h") #无法保存命令的执行结果；
# os.popen("df -h ") #可以保存命令的执行结果；
# os.mkdir('yourdir')


# @@自己写个模块
# python tab补全模块 for linux:
# #!/usr/bin/env python
# # python startup file
# import sys
# import readline
# import rlcompleter
# import atexit
# import os
# # tab completion
# readline.parse_and_bind('tab: complete')
# # history file
# histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
# try:
#     readline.read_history_file(histfile)
# except IOError:
#     pass
# atexit.register(readline.write_history_file, histfile)
# del os, histfile, readline, rlcompleter
#
# 写完保存后就可以使用了
#
# 调用命令：
# import tab

# 备注：每一个脚本都可以当成一个模块来使用；
#
# 你会发现，上面自己写的tab.py模块只能在当前目录下导入，如果想在系统的何何一个地方都使用怎么办呢？ 此时你就要把这个tab.py放到python全局环境变量目录里啦，
# 基本一般都放在一个叫 Python/2.7/site-packages 目录下，这个目录在不同的OS里放的位置不一样，用 print(sys.path) 可以查看python环境变量列表。

# C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study>python3
# Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import sys
# >>> print (sys.path)
# ['', 'C:\\python3\\python36.zip', 'C:\\python3\\DLLs', 'C:\\python3\\lib', 'C:\\python3', 'C:\\python3\\lib\\site-packages']



# .pyc是个什么
#
# 解释型语言和编译型语言
#
# 计算机是不能够识别高级语言的，所以当我们运行一个高级语言程序的时候，就需要一个“翻译机”来从事把高级语言转变成计算机能读懂的机器语言的过程。这个过程分成两类，
# 第一种是编译，第二种是解释。
#
# 编译型语言在程序执行之前，先会通过编译器对程序执行一个编译的过程，把程序转变成机器语言。运行时就不需要翻译，而直接执行就可以了。最典型的例子就是C语言。
#
# 解释型语言就没有这个编译的过程，而是在程序运行的时候，通过解释器对程序逐行作出解释，然后直接运行，最典型的例子是Ruby。
#
# 通过以上的例子，我们可以来总结一下解释型语言和编译型语言的优缺点，因为编译型语言在程序运行之前就已经对程序做出了“翻译”，所以在运行时就少掉了“翻译”的过程，
# 所以效率比较高。但是我们也不能一概而论，一些解释型语言也可以通过解释器的优化来在对程序做出翻译时对整个程序做出优化，从而在效率上超过编译型语言。
#
# 此外，随着Java等基于虚拟机的语言的兴起，我们又不能把语言纯粹地分成解释型和编译型这两种。
#
# 用Java来举例，Java首先是通过编译器编译成字节码文件，然后在运行时通过解释器给解释成机器文件。所以我们说Java是一种先编译后解释的语言。
#
#
# Python到底是什么
#
# 其实Python和Java/C#一样，也是一门基于虚拟机的语言，我们先来从表面上简单地了解一下Python程序的运行过程吧。
#
# 当我们在命令行中输入python hello.py时，其实是激活了Python的“解释器”，告诉“解释器”：你要开始工作了。可是在“解释”之前，其实执行的第一项工作和Java一样，是编译。
#
# 熟悉Java的同学可以想一下我们在命令行中如何执行一个Java的程序：
#
# javac hello.java
#
# java hello
#
#
# 只是我们在用Eclipse之类的IDE时，将这两部给融合成了一部而已。其实Python也一样，当我们执行python hello.py时，他也一样执行了这么一个过程，
# 所以我们应该这样来描述Python，Python是一门先编译后解释的语言。
#
# 简述Python的运行过程
#
# 在说这个问题之前，我们先来说两个概念，PyCodeObject和pyc文件(字节码文件，只有python的解释器可以读懂)。
#
# 我们在硬盘上看到的pyc自然不必多说，而其实PyCodeObject则是Python编译器真正编译成的结果。我们先简单知道就可以了，继续向下看。
#
# 当python程序运行时，编译的结果则是保存在位于内存中的PyCodeObject中，当Python程序运行结束时，Python解释器则将PyCodeObject写回到pyc文件中。
#
# 当python程序第二次运行时，首先程序会在硬盘中寻找pyc文件，如果找到，则直接载入，否则就重复上面的过程。
#
# 所以我们应该这样来定位PyCodeObject和pyc文件，我们说pyc文件其实是PyCodeObject的一种持久化保存方式。





