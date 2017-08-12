#!/usr/bin/python 
import paramiko
import threading

def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
            
        stdin, stdout, stderr = ssh.exec_command(cmd)
	out=stdout.readlines()
	print type(out)
	print out
        #for o in out:
        #    print o,
        print '%s\tOK\n'%(ip)
        ssh.close()
	return out
    except:
        print '%s\tError\n'%(ip)

if __name__=='__main__':
    ssh2("128.1.2.188","root","123456","ifconfig")

