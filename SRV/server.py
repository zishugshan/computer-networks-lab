# To write a Socket Program to implement ECHO

import socket
HOST = '127.0.0.1'
PORT = 4588
with socket.socket() as s:
    s.bind((HOST,PORT))
    s.listen()
    con,add = s.accept()
    print(f"server running on address {add}")
    data = con.recv(1024)
    con.sendall(data)
