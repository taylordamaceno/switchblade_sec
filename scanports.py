#!/bin/python3

import socket
import threading

# Define o alvo
target = '127.0.0.1'
# Pode ser um endereço IP ou um nome de domínio
# target = 'example.com'

# Função para escanear uma única porta
def scan_port(port):
    try:
        # Cria um socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define um tempo limite para a tentativa de conexão
        s.settimeout(1)
        # Tenta se conectar ao alvo e porta especificados
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except:
        pass

# Função principal
def main():
    # Intervalo de portas a serem escaneadas
    for port in range(1, 1025):
        # Cria uma nova thread para

