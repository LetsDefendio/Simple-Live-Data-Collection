import sys
import socket
import select
import os
import subprocess
from data import *

 
def chat_client():
    if(len(sys.argv) < 3) :
        print('Usage : python chat_client.py hostname port')
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()
     
    print 'Connected to remote host. You can start sending messages'
#    sys.stdout.write('[Me] '); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data :
                    print('\nDisconnected from  server')
                    sys.exit()
                else:
                    #print data
#                    sys.stdout.write(data)
                    try:
                        if data.split()[2][0] == "!":
                            command = data.split()[2][1:]
                            value = getValue(command)
                            s.send(str(value))
                        #print(str(value))
#                    sys.stdout.write('[Me] '); sys.stdout.flush()     
                    except:
                        pass            
            else :
                # user entered a message
                msg = sys.stdin.readline()
                #veri=subprocess.check_output(['date'])
                msg += str(msg)
                s.send(msg)
                sys.stdout.write('[Me] ');  sys.stdout.flush()

if __name__ == "__main__":

    sys.exit(chat_client())
