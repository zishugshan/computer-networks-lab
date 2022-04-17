import socket

server_add=('localhost',9999)
FORMAT = "utf-8"

server=socket.socket()
server.bind(server_add)

server.listen()
print("Waiting for the connection to be established .....")

client,client_add=server.accept()

print("Connection established successfully")

file_name=client.recv(1000).decode(FORMAT)
file=open(file_name,"w")
client.send("Filename received.".encode(FORMAT))
print("Filename recieved successfully!")

file_data=client.recv(1000).decode(FORMAT)
file.write(file_data)
client.send("File data received".encode(FORMAT))
print("File Data recieved successfully!")

file.close()
client.close()