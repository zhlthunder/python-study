http://www.cnblogs.com/yufeihlf/p/5945102.html

Robot Framework的环境搭建
1.Robot framework的安装
作用：web自动化测试框架。
RF框架是基于python 的，所以一定要有python环境。网上可以自行查找。
下载地址：https://pypi.python.org/pypi/robotframework/2.8.5#downloads
robotframework-2.8.5.win-amd64.exe
直接双击下一步即可。
 
2.wxPython 的安装
作用：Wxpython 是python 非常有名的一个GUI库，因为RIDE 是基于这个库开发的，所以这个必须安装。
下载地址：http://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/
wxPython2.8-win64-unicode-2.8.12.1-py27.exe
直接双击下一步即可。
 
3.Robot framework-ride
作用：RIDE就是一个图形界面的用于创建、组织、运行测试的软件。
下载地址：https://pypi.python.org/pypi/robotframework-ride
robotframework-ride-1.5.1.tar.gz
将其解压到C盘，以后的话最好建个目录，好多python都要解压。C:\Python27\Scripts上可以查看到。
cd C:\robotframework-ride-1.5.1
python  setup.py install
 
4.Robot framework-selenium2library
作用：RF-seleniumlibrary 可以看做RF版的selenium 库，selenium （webdriver）可以认为是一套基于web的规范（API），所以，RF 、appium 等测试工具都可以基于这套API进行页面的定位与操作。
下载地址：https://github.com/robotframework/Selenium2Library#readme
Selenium2Library-master.zip
将其解压到C盘，以后的话最好建个目录，好多python插件都要解压。C:\Python27\Scripts上可以查看到。
cd C:\Selenium2Library-master
python setup.py install
 
以上安装完成之后，如何启动RIDE：
1.通过文件启动（双击[dirPath]\python\Lib\site-packages\robotide下的__init__.py文件）
2.通过命令启动（运行->ride.py回车/确认）
cd C:\Python27\Scripts\
python ride.py
3.将C:\Python27\Scripts\ride.py创建快捷键，
打开ride.py文件之后（以python方式打开），点击“运行（start）”按钮。
 
查看pybot版本
cd C:\Python27\Scripts
pybot --version