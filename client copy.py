# echo-client.py

import socket

#HOST = "127.0.0.1"  # The server's hostname or IP address
#HOST = '172.20.43.162'
HOST = '172.20.43.230'
PORT = 443  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input()
        s.sendall(bytes(message, 'utf-8'))
        data = s.recv(1024)
        print("recieved", data)