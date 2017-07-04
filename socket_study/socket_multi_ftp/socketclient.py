#!/usr/bin/python

import socket,time,commands
HOST="localhost"
PORT=9999
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    cmd=raw_input("input your command:").strip()
    if len(cmd)==0:break
    if cmd=='h' or cmd=='help':
        print """
            h:print help info
            get file_name:download file from ftp server
            put file_name:upload file to ftp server
            lls: execute "ls" command at local directory
            del file_name:execute "rm -rf file_name" at local directory
            q:exit ftp client program
            other linux inbox command: excute command at ftp server side
            """
        continue 
    if cmd=='q':
        exit("byebye")
    if cmd=='lls':
        status,result=commands.getstatusoutput('ls')
        print result
        continue
    if 'del' in cmd:
        rr="rm -rf "+cmd.split()[1]
        print cmd
        print rr
        status,result=commands.getstatusoutput(rr)
        print result
        continue
    s.sendall(cmd)
    ret=cmd.split()
    if ret[0]=='get':
        with open(ret[1],'wb') as f:
            while True:
                data=s.recv(1024)
                if data=="FiletransferDone":break
                f.write(data)
        continue

    if ret[0]=='put':
        with open(ret[1],'rb') as f:
            s.sendall(f.read())
        time.sleep(0.5)
        s.send("uploaded")
        continue


    data=s.recv(8192)
    print(data)
