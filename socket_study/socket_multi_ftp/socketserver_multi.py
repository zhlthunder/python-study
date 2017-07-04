#!/usr/bin/python

import SocketServer,commands,time

class MyTCPHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        while True:
            self.data=self.request.recv(1024).strip()
            print "%s write:"% self.client_address[0]
            if not self.data:
                print "%s is dead" % (self.client_address[0])
                break

            cmd=self.data.split()
            ## for get file from ftp server
            if cmd[0]=='get':
                with open(cmd[1],'rb') as f:
                    self.request.sendall(f.read())
                time.sleep(0.5)
                self.request.sendall("FiletransferDone")
                continue        

            ##for upload file to ftp server
            if cmd[0]=='put':
                with open(cmd[1],'wb') as f:
                    while True:
                        data=self.request.recv(1024)
                        if data=="uploaded":break
                        f.write(data)
                continue
            status,result=commands.getstatusoutput(self.data)
            if len(result)==0:
                self.request.sendall("Done")
            else:
                self.request.sendall(result)

if __name__=="__main__":
    HOST="localhost"
    PORT=9999
    server=SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()
