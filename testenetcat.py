#!/bin/python3
import socket

host = "localhost"
port = 8080

s = socket.socket()

# Corrigido "portai" para "port"
s.connect((host, port))

msg = "salve"

# Corrigido "endoce" para "encode"
s.send(msg.encode())

s.close()
