import socket
#AF_INET used for IPv4
#SOCK_DGRAM used for UDP protocol
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM ) #binding IP and port
s.bind(("10.80.1.42",2222))
print("Server started ...10.80.1.42:2222") 
print("Waiting for Client response...") #recieving data from client
while True:
    print(s.recvfrom(1024))