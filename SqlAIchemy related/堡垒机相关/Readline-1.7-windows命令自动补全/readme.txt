注意:此只适合python2.7

安装使用方法:
1.将以下所有文件复制到Python\Lib\site-packages\下
Readline-1.7-py2.7.egg-info
readline.py
readline.pyc
_rlsetup.pyd

2.将.startup.py放到%USERPROFILE%
添加环境变量PYTHONSTARTUP,
值为%USERPROFILE%\.startup.py

这样python启动时就可以自动开启补全功能了