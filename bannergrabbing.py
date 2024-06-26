#!/bin/python3

import socket

def banner_grab(host, port):
    try:
        # Cria um socket
        s = socket.socket()
        # Define um tempo limite para a tentativa de conexão
        s.settimeout(5)
        # Conecta ao serviço no host e porta especificados
        s.connect((host, port))
        # Recebe a resposta (banner)
        banner = s.recv(1024)
        return banner.decode().strip()
    except Exception as e:
        return str(e)
    finally:
        s.close()

if __name__ == "__main__":
    # Define o alvo e a porta
    target = '127.0.0.1'
    port = 80
    
    # Pode aceitar entradas do usuário para o alvo e a porta
    target = input("Enter the target IP or hostname: ")
    port = int(input("Enter the target port: "))
    
    # Realiza o banner grabbing
    banner = banner_grab(target, port)
    print(f"Banner from {target}:{port} - {banner}")

