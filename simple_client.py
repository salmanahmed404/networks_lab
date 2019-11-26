import socket

HOST = '127.0.0.1'
PORT = 8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((HOST,PORT))
except:
    print("Exception")

while True:
    server_msg = s.recv(1024)
    print("Server says: ",server_msg)
    client_msg = input()
    s.send(bytes(client_msg,"utf8"))