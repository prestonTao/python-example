# -*- coding: utf-8 -*-


import socket,time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1",1990))
client.send("hello")
time.sleep(1)
client.send("Im client")
client.close()




