#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# 相关的模块：
# json pickle

#序列化 本质上 就是把 python的基本数据类型 转换成字符串； 反序列化 是把字符串转换成pYthon基本数据类型；

# import json
# dic={'k1':'v1'}
# print(dic,type(dic))
#dumps: 用于把python的基本数据类型转换成字符串；
# rt=json.dumps(dic)
# print(rt,type(rt))
#
# 输出：
# {'k1': 'v1'} <class 'dict'>
# {"k1": "v1"} <class 'str'>

# import json
# s1='{"k1":123}'  #虽然它是个字符串，但它的形状必须和python的基本数据类型保持一致；@@@重要；
#loads是用来把字符串转换成python的基本数据类型的；
# ret=json.loads(s1)
# print(ret,type(ret))
# 输出：
# {'k1': 123} <class 'dict'>

##http请求，返回的就是字符串；
##url : http://wthrcdn.etouch.cn/weather_mini?city=%E5%8C%97%E4%BA%AC
##url : http://wthrcdn.etouch.cn/weather_mini?city=北京

##基于天气API获取天气相关JSON数据
#我们平常接触的各种API，都是以URL的方式提供的，如果访问成功的话，就会返回字符串；这种方式就是JSON方式；
#即我们发送一个http请求，然后拿到一个字符串；

# import requests
# import json
# r=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')  #r是http请求返回的对象
# r.encoding='utf-8' #对返回的数据进行编码
# print(r.text,type(r.text))  #r.text  获取对象中的文本内容
# dic=json.loads(r.text)
# print(type(dic))

# 输出：
# {"data":{"yesterday":{"date":"26日星期一","high":"高温 34℃","fx":"南风","low":"低温 21℃","fl":"微风","type":"多云"},"city":"北京","aqi":"184","forecast":[{"date":"27日星期二","high":"高温 34℃","fengli":"微风级","low":"低温 22℃","fengxiang":"南风","type":"多云"},{"date":"28日星期三","high":"高温 34℃","fengli":"微风级","low":"低温 23℃","fengxiang":"南风","type":"多云"},{"date":"29日星期四","high":"高温 33℃","fengli":"微风级","low":"低温 23℃","fengxiang":"南风","type":"雷阵雨"},{"date":"30日星期五","high":"高温 34℃","fengli":"微风级","low":"低温 24℃","fengxiang":"南风","type":"多云"},{"date":"1日星期六","high":"高温 32℃","fengli":"微风级","low":"低温 23℃","fengxiang":"南风","type":"多云"}],"ganmao":"各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。","wendu":"29"},"status":1000,"desc":"OK"} <class 'str'>
# <class 'dict'>

#字符串相当于各语言之间沟通的桥梁， 即 json最广泛的用途是用于跨语言的交互用的；


## json中两个方法：
# json.dumps: 把python的基本数据类型转换为字符串；
# json.loads: 把字符串形式的列表或字典转换为python的基本数据类型；

# import json
# r=json.dumps([11,22,33])


# li='["alex","tom"]'  #这种写法正确
# li="['alex','tom']" #这种写法错误，执行时会报错， 之所以错误的原因是： 在python中字符串可以用单引号括起来，
# 但在其它语言中，字符串必须用双引号，单引号只能用于字符，所有会报错；
#python中: 单引号--字符串； 双引号--字符串；
#其它语言中: 单引号--字符； 双引号--字符串；
#通过loads去反序列化时，一定要使用双引号；
# ret=json.loads(li)
# print(ret,type(ret))
# 输出：
# ['alex', 'tom'] <class 'list'>



##另外两个方法：
#dumps 和 loads 都是在内存中进行操作的；
#dump: 先进行序列化，再写到文件中
# import json
# li=[11,22,33]
# json.dump(li,open('xlh','w'))
#
# #load: 先从文件中读取字符串，再转换成基本的数据类型；
# li=json.load(open('xlh','r'))
# print(li,type(li))
# 输出：
# [11, 22, 33] <class 'list'>



##pickle 序列化， 区别是：pickle只为python使用的；而python却可以在不同语言中进行交互；

# import pickle
# li=[11,22,33]
# r=pickle.dumps(li)  #转换成只有python能认识的序列
# print(r,type(r))
#
# ret=pickle.loads(r)
# print(ret,type(ret))

# 输出：
# b'\x80\x03]q\x00(K\x0bK\x16K!e.' <class 'bytes'>
# [11, 22, 33] <class 'list'>


# import  pickle
# li=[11,22,33]
# pickle.dump(li,open('xlh','wb')) #只支持b的方式

# import pickle
# ret=pickle.load(open('xlh','rb'))  #只支持b的方式
# print(ret,type(ret))
# 输出：
# [11, 22, 33] <class 'list'>



#json vs pickle
#1.json只支持python的基本数据类型，比如字典。列表等；但不执行类等复杂数据类型；
# import json
# class Foo:
#     def __init__(self):
#         pass
# f=Foo()
# json.dumps(f)
# json._default_encoder
# 报错：
# TypeError: Object of type 'Foo' is not JSON serializable

#2.单pickle 支持python的全部数据类型；所有功能更强大；

# ==》总结：
# json: 适合于跨语言的场景，只能对基本数据类型进行操作；
# pickle: 只用于python内部的序列化，可以支持python的s所有数据类型； 且可能还有一个问题就是，不同python版本间可能也存在问题；