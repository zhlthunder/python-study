# -*- coding: utf-8 -*-
# Copyright (C) 2003-2007  Robey Pointer <robeypointer@gmail.com>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.


import socket
import sys
from paramiko.py3compat import u

# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(chan):
    if has_termios:
        posix_shell(chan)  #for unix shell
    else:
        windows_shell(chan)  # for windows shell


def posix_shell(chan):
    import select
    
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)  #设置永不超时

        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])   #chan:当前客户端的socket 句柄
            if chan in r:  #判断自己的句柄是否在可读里，如果在，就表示是活动的句柄
                try:
                    x = u(chan.recv(1024))  #u()  转换成unicode
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        break
                    sys.stdout.write(x)  ##接收到数据，打印到屏幕上
                    sys.stdout.flush()  ##立即打印到屏幕，不缓冲
                except socket.timeout:
                    pass
            if sys.stdin in r:  ##判断是否有键盘输入
                # x = sys.stdin.read(1)  ##如果有，获取输入的内容
                x = sys.stdin.read()  ##如果有，获取输入的内容,不太清楚为啥 read(1)和read()实现相同的功能,待后续继续排查？？？
                print("input key-->:",x)
                if len(x) == 0:
                    break
                chan.send(x)    ##通过句柄发送输入的内容

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

    
# thanks to Mike Looijmans for this code
def windows_shell(chan):
    import threading

    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")
        
    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(data)
            sys.stdout.flush()
        
    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()
        
    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass
