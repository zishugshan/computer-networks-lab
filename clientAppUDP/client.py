import socket
#client program
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    ip ,port = input("Enter server ip address and port number :\n").split() 
    m = input("Enter data to send server: ")
    res = s.sendto(m.encode(),("10.80.1.42",2222))
    if res:
        print("\nsuccessfully send")