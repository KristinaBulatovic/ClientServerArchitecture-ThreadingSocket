import socket

s = socket.socket()
host = 'localhost'
port = 1234

s.connect((host,port))
s.send(str(100).encode())

print(s.recv(1024).decode())

s.close()