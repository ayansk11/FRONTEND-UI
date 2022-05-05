import socket

host = "127.0.0.1"
port = 500

client_socket = socket.socket()
client_socket.connect((host, port))

message = input(" -> ")

while message.lower().strip() != "bye":

    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()


    print("recieved from server: ", data)
    message = input(" -> ")
    
client_socket.close()