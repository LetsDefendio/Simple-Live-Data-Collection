import sys
import socket
import select

HOST = '192.168.131.129' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 4444

def server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    SOCKET_LIST.append(server_socket)
 
    print("Server started on port " + str(PORT))
 
    while 1:

        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print("(%s, %s) connected" % addr)
                 

            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)  
                    else:
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        
                        broadcast(server_socket, sock, "(%s, %s) is offline\n" % addr) 
 
                except:
                    broadcast(server_socket, sock, "(%s, %s) is offline\n" % addr)
                    continue

    server_socket.close()
    

def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
                print(message)
            except :
                socket.close()

                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
 
if __name__ == "__main__":
    sys.exit(server())   