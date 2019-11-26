import socket

HOST = ''
PORT = 8081

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
conn, addr = s.accept()
# conn.send(b"Welcome Cient! ")
print("Connected to: ",addr)


f = open('playfair_client.txt','rb')
data = f.read(1024)
conn.send(data)
print("File Sent ")
f.close()

f = open('received.txt','wb')

data = conn.recv(1024)     
f.write(data)

f.close()
print("File Received ")    
    
    
