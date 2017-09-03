#!/usr/bin/python   
#-*- encoding:utf-8 -*-
# python startup file   

#添加python自动补全功能           
import sys   
import readline   
import rlcompleter   
import atexit   
import os    
# tab completion   
readline.parse_and_bind('tab: complete')   
# history file   
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')   
try:   
    readline.read_history_file(histfile)   
except IOError:   
    pass   
atexit.register(readline.write_history_file, histfile)   
           
del os, histfile, readline, rlcompleter  