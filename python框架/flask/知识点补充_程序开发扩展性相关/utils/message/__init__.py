#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import settings
import importlib

def send_msgs(msg):
    for path in settings.MSG_LIST:
        m,c=path.rsplit('.',maxsplit=1)   ##从右边开始分割1次，就把模块路径和 类或函数分割开了
        md=importlib.import_module(m) ##动态导入模块
        cls=getattr(md,c)   ##基于类的字符串从模块中找到对应的类
        # print(md,cls)
        obj=cls()   ##类的实例化
        obj.send(msg) ##执行类的方法
        # print(path)
    # print("it is tesinggasdfafd")

##此处非常重要，根据字符串导入模块，然后使用反射获取类名


"""
##补充，rsplit 方法：
参考：https://www.cnblogs.com/zhangzengqiang/p/7525175.html

python中的split、rsplit、splitlines

split()从左向右寻找，以某个元素为中心将左右分割成两个元素并放入列表中

rsplit()从右向左寻找，以某个元素为中心将左右分割成两个元素并放入列表中

splitlines()根据换行符（\n）分割并将元素放入列表中

sample:
1 a = "dlrblist"
2 a1 = a.split("l", 1)
3 print(a1)
输出： ['d', 'rblist']
从左向右寻找，以寻找到的第一个"l"为中心将左右分割成两个元素并放入列表中

1 b = "dlrblist"
2 b1 = b.rsplit("l", 1)
3 print(b1)
输出： ['dlrb', 'ist']
从右向左寻找，以寻找到的第一个"l"为中心将左右分割成两个元素并放入列表中

1 c = "hello\nworld\ndlrb"
2 c1 = c.splitlines()
3 print(c1)

输出： ['hello', 'world', 'dlrb']
根据换行符切割成了三个元素并放入列表中

如果指定maxsplit则最多返回的列表长度不大于maxsplit,即分割多少次的意思

>>> u = "www.doiido.com.cn"

#分割一次

>>>print u.split('.',1)

['www','doiido.com.cn']

#分割两次

>>>print u.split('.',2)

['www','doiido', 'com.cn']



importlib：python importlib动态导入模块
参考： https://www.cnblogs.com/Hi-blog/p/8529297.html

一般而言，当我们需要某些功能的模块时（无论是内置模块或自定义功能的模块），可以通过import module 或者
from * import module的方式导入，这属于静态导入，很容易理解。

　　而如果当我们需要在程序的运行过程时才能决定导入某个文件中的模块时，并且这些文件提供了同样的接口名字，
上面说的方式就不适用了，这时候需要使用python 的动态导入。

importlib使用

如在scripts目录中保存着一些功能模块，向外提供类似的接口poc()和脚本描述信息description，
需要传入一个参数target，当然脚本执行的功能是不一样的，以下只是举例：

starnight:EXP-M starnight$ ls scripts/
__init__.py     __pycache__     test1.py        test2.py        test3.py
starnight:EXP-M starnight$ cat scripts/test1.py
#!/usr/bin/env python
# -*- coding:utf-8 -*-

description = 'it is a test1'


def poc(target):
    print('it is a test1')

    return True


而我们需要动态传入脚本名，来选用此时要执行的功能：

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import importlib

script_name = input('please input script_name : ')　　　　　# 手动输入脚本名　　　　　　　　　　　　　　　
module = importlib.import_module('scripts.{}'.format(script_name))　　　　# 动态导入相应模块，本质上就是从一串字符串中导入模块
func = module.poc('')　　　　　　# 执行脚本功能
print(module.description)　　　 # 获取脚本描述信息

执行信息：
please input script_name : test1
it is a test1
it is a test1

...

please input script_name : test3
it is a test3
it is a test3





"""

