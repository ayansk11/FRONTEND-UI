import socket

host = socket.gethostname()
port = 5000

server_socket = socket.socket()
server_socket.bind((host, port))

server_socket.listen(2)

conn, add = server_socket.accept()
print("Connect from: ", add)

while True:

    data = conn.recv(1024).decode()

    if not data:
        break

    print("from connected user: ", data)
    data = input(" -> ")
    conn.send(data.encode())

conn.close()
