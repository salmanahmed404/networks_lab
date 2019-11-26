import socket

HOST = '127.0.0.1'
PORT = 8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen()
conn, addr = s.accept()
conn.send(b"Welcome Cient! ")
print(conn)
print("Connected to: ",addr)
while conn:
    client_msg = conn.recv(1024)
    print("Client says: ",client_msg)
    server_msg = input()
    conn.send(bytes(server_msg,"utf8"))