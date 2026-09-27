import socket

#Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Assign IP address and port
server_socket.bind(("127.0.0.1", 5000))

#Wait for client
server_socket.listen(1)

print("Server is waiting for connection...")

#Accept client connection
client_socket, address = server_socket.accept()

print("Connected to:", address)

#Receive data
data = client_socket.recv(1024).decode()

print("Client says:", data)

#Send response
client_socket.send("Hello from TCP Server".encode())

#Close connection
client_socket.close()
server_socket.close()