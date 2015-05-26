# -*- coding: utf-8 -*-


import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',1990))
server.listen(5)

while 1:
    sock,addr = server.accept()
    print("got connection form ", sock.getpeername())
    while 1:
        data = sock.recv(1024)
        if not data:
            break
        else:
            print(data)

