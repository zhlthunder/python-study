参考blog:
http://www.cnblogs.com/alex3714/articles/6662365.html

需求：
生成随机验证码


问题1： from PIL import Image,ImageDraw,ImageFont,ImageFilter
PIL 模块安装

方法如下：
从 http://www.pythonware.com/products/pil/    下载源码包： Python Imaging Library 1.1.7 Source Kit ： Imaging-1.1.7.tar.gz
后，通过源码的方式进行安装，（python setup.py install）
remark: 源码的安装方式，适用于所有的平台 （linux or windows,  python 不同的版本）

安装完成后确认可以导入：
[root@localhost module_tiaoshi]# python
Python 2.6.6 (r266:84292, Sep  4 2013, 07:46:00) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from PIL import Image
>>> 


问题2：linux 系统下字体库创建相关：

在linux下执行如下操作：  
mkdir  /usr/share/fonts/arial
从windows系统目前下c:/windows/fonts下拷贝arial或直接用附件中arial文件夹的所有文件上传到 /usr/share/fonts/arial/下。
执行： mkfontscale 即可 （如果有问题，可以参考：https://www.cnblogs.com/sqmlinux/archive/2012/08/20/2646993.html）
直接在代码中配置：
font_path = '/usr/share/fonts/arial/arial.ttf' 即可；

直接执行脚本即可：
生成的图片在 会把生成的图片存成/tmp/test.png 下。