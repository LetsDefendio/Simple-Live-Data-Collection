import sys
import socket
import select
 
def main():

    host = "192.168.131.129"
    port = int(4444)
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()
     
    print('Connected to remote host')
    sys.stdout.write('>> '); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]

        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:

                data = sock.recv(4096)
                if not data :
                    print('\nDisconnected from server')
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    sys.stdout.write('>> '); sys.stdout.flush()     
            
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('>> '); sys.stdout.flush() 

if __name__ == "__main__":

    sys.exit(main())