import socket


client=socket.socket()
server_add=('localhost',9999)
client.connect(server_add)
FORMAT = "utf-8"

""" Opening and reading the file data. """
file = open("data/dummy.txt", "r")
data = file.read()

""" Sending the filename to the server. """
client.send("data/dummy.txt".encode(FORMAT))
msg = client.recv(1000).decode(FORMAT)
print(f"[SERVER]: {msg}")

""" Sending the file data to the server. """
client.send("dummy.txt".encode(FORMAT))
msg = client.recv(1000).decode(FORMAT)
print(f"[SERVER]: {msg}")

""" Sending the file data to the server. """
client.send(data.encode(FORMAT))
msg = client.recv(1000).decode(FORMAT)
print(f"[SERVER]: {msg}")

""" Closing the file. """
file.close()

""" Closing the connection from the server. """
client.close()

