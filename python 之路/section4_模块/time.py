#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# http://www.cnblogs.com/alex3714/articles/5161349.html

import  time
# print(time.time())  #输出： 1498655266.4812596 #从1970开始到现在以秒为单位的时间偏移
# print(time.ctime()) #返回当前系统时间的字符串格式 ， 输出：Wed Jun 28 21:08:56 2017
# print(time.ctime(time.time()-86400))#输出Tue Jun 27 21:10:00 2017  ,即ctime可以把时间戳转换成字符串

# print(time.gmtime())  #将时间拆分成年 月 日 。。。，且获取的是格林威治的标准时间
# 输出：time.struct_time(tm_year=2017, tm_mon=6, tm_mday=28, tm_hour=13, tm_min=11, tm_sec=6, tm_wday=2, tm_yday=179, tm_isdst=0)

# time_obj=time.gmtime()
# print(time_obj.tm_year,time_obj.tm_mon) #输出： 2017 6
# print("{year}--{month}".format(year=time_obj.tm_year,month=time_obj.tm_mon)) #输出 2017--6
# #即使用时间对象后，把时间拆分成一个个独立的元素，然后就可以根据需要进行随意的字符串格式化了

# print(time.gmtime()) #获取格林威治时间，即UTC时间
# print(time.localtime()) #获取本地时间：
# 输出：
# time.struct_time(tm_year=2017, tm_mon=6, tm_mday=28, tm_hour=13, tm_min=18, tm_sec=3, tm_wday=2, tm_yday=179, tm_isdst=0)
# time.struct_time(tm_year=2017, tm_mon=6, tm_mday=28, tm_hour=21, tm_min=18, tm_sec=3, tm_wday=2, tm_yday=179, tm_isdst=0)
#

# time_obj=time.gmtime() #获取时间对象
# print(time.mktime(time_obj))  #用于把时间对象转换成时间戳
# # 输出：1498627188.0


#延时
# time.sleep(4) #默认以秒为单位，用于来做程序阻塞

##用于把utc时间对象转换成指定的字符串格式＠＠最常用
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) ) #将utc struct_time格式转成指定的字符串格式
# 输出：2017-06-28 13:24:19

##和上面的方法想法，用于把字符串格式转换成时间对象；@@最常用
# print(time.strptime("2016-05-6 15:06","%Y-%m-%d %H:%M"))
# 输出： time.struct_time(tm_year=2016, tm_mon=5, tm_mday=6, tm_hour=15, tm_min=6, tm_sec=0, tm_wday=4, tm_yday=127, tm_isdst=-1)

#备注，上面的 tm_yday=127 指的是今年到现在过了多少天了


# 日期字符串 转成  时间戳
# string_2_struct = time.strptime("2016/05/22","%Y/%m/%d") #先将 日期字符串转成 struct时间对象格式
# print(string_2_struct)
# struct_2_stamp = time.mktime(string_2_struct) #再将struct时间对象转成时间戳
# print(struct_2_stamp)

# 输出：
# time.struct_time(tm_year=2016, tm_mon=5, tm_mday=22, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=143, tm_isdst=-1)
# 1463846400.0

##datetime  模块
import datetime
# print(datetime.date.today())  #输出2017-06-28
# print(datetime.date.fromtimestamp(time.time())) #将时间戳转换成日期格式，只保留日期

# print(datetime.datetime.now()) #输出当前时间  输出： 2017-06-28 21:38:11.218969

# current_time=datetime.datetime.now()  ##这是使用最多@@@
# print(current_time)
# print(current_time.timetuple())  #将字符串格式时间转换成时间对象
# 输出：
# 2017-06-28 21:39:46.551821
# time.struct_time(tm_year=2017, tm_mon=6, tm_mday=28, tm_hour=21, tm_min=39, tm_sec=46, tm_wday=2, tm_yday=179, tm_isdst=-1)


# print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
# print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
# print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
# print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
#
# c_time  = datetime.datetime.now()
# print(c_time.replace(minute=3,hour=2)) #时间替换
# print(c_time.replace(2015,6)) #时间替换,直接替换年 和 月份

c_time  = datetime.datetime.now()
time_obj=c_time.replace(2015,5)
print(c_time>time_obj)  ##返回true, 即可以直接信息比较；
print(c_time==time_obj)  ##返回false, 即可以直接信息比较；
