# IMPLEMENT REMOTE CODE EXECUTION  (COMMANDS)
import socket

server_add=('localhost',9999)
server=socket.socket()
server.bind(server_add)

server.listen()
print("waiting for connections")
client,client_add=server.accept()

while True:
    command=input("Enter any command to execute on client")
    client.sendall(bytes(command.encode()))
    confirm=client.recv(1000).decode()
    if confirm:
        print("Command executed successfully!")
    else:
        print("Command failed to execute!")

server.close()
