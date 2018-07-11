#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl
import pygame,time

class Music:
    def __init__(self,path):
        self.path=path
        ##初始化：
        pygame.mixer.init()
        ##加载音乐
        track=pygame.mixer.music.load(self.path)

    def play(self):
            pygame.mixer.music.play()
            time.sleep(3600)

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()