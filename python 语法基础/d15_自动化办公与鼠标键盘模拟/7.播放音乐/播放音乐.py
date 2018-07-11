#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

# pip3 install pygame  安装模块

import time
import pygame


##音乐路径：
filepath=r'C:\Users\lin\PycharmProjects\python_study_1s\python_study\git-zhl\python-study\python 语法基础\d15_自动化办公与鼠标键盘模拟\7.播放音乐\我喜欢上你时的内心活动.mp3'


##初始化：
pygame.mixer.init()

##加载音乐
track=pygame.mixer.music.load(filepath)

##播放
pygame.mixer.music.play()
time.sleep(600)

##暂停
# pygame.mixer.music.pause()


##结束
pygame.mixer.music.stop()