
# To write a Socket Program to implement ECHO

import socket
HOST ="127.0.0.1"
PORT = 4588
with socket.socket() as c:
    c.connect((HOST,PORT))
    c.sendall(b"I am sending message ")
    data = c.recv(1024)
    print(f"Message received : {data}")
