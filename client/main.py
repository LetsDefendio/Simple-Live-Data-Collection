import sys
import socket
import select
from data import *

 
def main():

    host = "192.168.131.129"
    port = int(9009)
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()
     
    print('Connected to remote host')

     
    while 1:
        socket_list = [sys.stdin, s]

        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print('\nDisconnected from  server')
                    sys.exit()
                else:
                    sys.stdout.write(data)
                    try:
                        if data.split()[2][0] == "!":
                            command = data.split()[2][1:]
                            value = getValue(command)
                            s.send(str(value))
                    except:
                        pass            

                     
if __name__ == "__main__":
    sys.exit(main())
