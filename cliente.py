# coding: utf-8

import socket

PORT = 60000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Pedir a conexão:
cliente.connect( ('127.0.0.1', PORT) )

while True:
    # in_data = client.recv(1024)
    # print("From Server :", in_data.decode())
    mensagem = input("Informe o texto ou digite 'sair' para desconectar: ")
    cliente.sendall(bytes(mensagem, 'UTF-8'))
    if mensagem == 'sair':
        break

cliente.close()