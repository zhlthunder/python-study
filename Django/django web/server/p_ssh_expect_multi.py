#!/usr/bin/python 
import paramiko
import threading
import time

def ssh2(ip,username,passwd,cmd,li):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            out = stdout.read()
	    #print type(out)
            #for o in out:
            #    li.append(o)
            #print(out)
            li.append(out)
        print '%s\tOK\n'%(ip)
        ssh.close()
    except :
        print '%s\tError\n'%(ip)

if __name__=='__main__':
# comman list
    result=[]
    cmd = ['lsblk','ifconfig','route| grep -i 128']
    username = "root"  
    passwd = "123456"   
    threads = [6] 
    print "Begin......"
    ip="128.1.2.188"
    a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd,result))
    a.start()
    time.sleep(1)
    for i in result:
        print i,
  
