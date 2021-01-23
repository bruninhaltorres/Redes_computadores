# coding: utf-8

import socket

PORT = 8080

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Pedir a conexão:
cliente.connect( ('127.0.0.1', PORT) )

while True:
    text = input("Informe o texto ou digite 'sair' para desconectar: ")
    cliente.send(str.encode(text))
    if (text == "sair"):
        cliente.close()
        break