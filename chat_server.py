import socket
import select 
from _thread import *

HOST = ''
PORT = 8080

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind((HOST,PORT))

server.listen(100)

clients = []

def connection(conn,addr):
    conn.send(bytes("Welcome",'utf8'))
    while True:
        try:
            message = conn.recv(1024)
            if message:
                print(f'{addr[0]} says {message}')
                broadcast(messsage,conn)
            else:
                remove(conn)
        except Exception as e:
            print(e)
            
def remove(connection):
    if connection in clients:
        clients.remove(connection)

def broadcast(data,connection):
    for client in clients:
        if (client!=connection):
            try:
                client.send(bytes(data,'utf8'))
            except:
                client.close()
                remove(clients)

while True:
    conn, addr = server.accept()
    clients.append(conn)
    print(addr[0],"Connected ")
    start_new_thread(connection,(conn,addr))
conn.close()
server.close()
