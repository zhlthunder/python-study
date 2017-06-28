#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import logging

##第一个打印日志的例子
# logging.warning("user [alex] attempted wrong password more than 3 times")
# logging.critical("server is down")
# 输出：
# WARNING:root:user [alex] attempted wrong password more than 3 times
# CRITICAL:root:server is down

#日志级别
# Level	When it’s used
# DEBUG 	Detailed information, typically of interest only when diagnosing problems.
# INFO 	Confirmation that things are working as expected.
# WARNING 	An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR 	Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL 	A serious error, indicating that the program itself may be unable to continue running.


##将日志写到文件中

# logging.basicConfig(filename='example.log',level=logging.INFO)  ##只有info及以上级别的日志才会写入文件中
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
#
# 文件中日志：
# INFO:root:So should this
# WARNING:root:And this, too

# 其中下面这句中的level=loggin.INFO意思是，把日志纪录级别设置为INFO，也就是说，只有比日志是INFO或比INFO级别更高的日志才会被纪录到文件里，
# 在这个例子， 第一条日志是不会被纪录的，如果希望纪录debug的日志，那把日志级别改成DEBUG就行了。


#为日志加上时间：
# import logging
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning('is when this event was logged.')
# 输出：
# 06/28/2017 10:17:22 PM is when this event was logged.


# logging.basicConfig(filename='example.log',level=logging.INFO,
#                     format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')  ##配置日志时间格式
#  logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
#
# 写入文件的内容：
# 06/28/2017 10:18:32 PM So should this
# 06/28/2017 10:18:32 PM And this, too


# 日志格式
# %(name)s
#
# Logger的名字
#
# %(levelno)s
# 数字形式的日志级别
# %(levelname)s
# 文本形式的日志级别
#
# %(pathname)s
# 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s @@重要
# 调用日志输出函数的模块的文件名
# %(module)s  @@重要
# 调用日志输出函数的模块名
# %(funcName)s  @@重要
# 调用日志输出函数的函数名
# %(lineno)d  @@重要
# 调用日志输出函数的语句所在的代码行
# %(created)f
# 当前时间，用UNIX标准的表示时间的浮 点数表示
#
# %(relativeCreated)d
# 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s
# 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d  @@重要
# 线程ID。可能没有
# %(threadName)s  @@重要
# 线程名。可能没有
# %(process)d  @@重要
# 进程ID。可能没有
# %(message)s
# 用户输出的消息




# @@@如果想同时把log打印在屏幕和文件日志里，就需要了解一点复杂的知识 了

# Python 使用logging模块记录日志涉及四个主要类，使用官方文档中的概括最为合适：
#
# logger提供了应用程序可以直接使用的接口；  ##应用程序直接调用的方法
#
# handler将(logger创建的)日志记录发送到合适的目的输出； ##定义日志输出到哪里
#
# filter提供了细度设备来决定输出哪条日志记录；
#
# formatter决定日志记录的最终输出格式。 ##日志格式化



##代码实例
import logging

#create logger
logger = logging.getLogger('TEST-LOG')  ##获取logging对象；test-log 为指定的日志的标记
logger.setLevel(logging.DEBUG) #设置全局日志级别


# create console handler and set level to debug
ch = logging.StreamHandler()  ##输出到屏幕，
ch.setLevel(logging.DEBUG)  #输出到屏幕的日志级别

# create file handler and set level to warning
fh = logging.FileHandler("access.log") ##输出到文件
fh.setLevel(logging.WARNING) #文件输出的日志级别
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter_for_file = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')

# add formatter to ch and fh
ch.setFormatter(formatter)  ##把formatter 应用到handler上
fh.setFormatter(formatter_for_file)  ##把formatter 应用到handler上

# add ch and fh to logger
logger.addHandler(ch)  #将handler注册到logger
logger.addHandler(fh) #将handler注册到logger

# 'application' code  ##打印日志
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

# 屏幕输出：
# 2017-06-28 22:29:53,040 - TEST-LOG - DEBUG - debug message
# 2017-06-28 22:29:53,040 - TEST-LOG - INFO - info message
# 2017-06-28 22:29:53,040 - TEST-LOG - WARNING - warn message
# 2017-06-28 22:29:53,040 - TEST-LOG - ERROR - error message
# 2017-06-28 22:29:53,040 - TEST-LOG - CRITICAL - critical message
#
# 文件输出：
# 2017-06-28 22:29:53,040  - WARNING - warn message
# 2017-06-28 22:29:53,040  - ERROR - error message
# 2017-06-28 22:29:53,040  - CRITICAL - critical message

#说明，全局和局部日志级别： 全局的优先级高，即局部的基本只能高于或等于全局的级别，如果比全局的低，就不记录了那个日志了；


# #总结：
# 主要用到 logger, handler, formatter 三个方法，
# 配置的步骤：
# 先创建一个logger对象
# 创建handler
# 设定formatter格式
#
# 将formatter应用到handler，
# 再将handler注册到logger，
# 然后就可以打印了