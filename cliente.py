# coding: utf-8

import socket

cliente = socket.socket()
#Pedir a conexão:
cliente.connect( ('127.0.0.1', 50000) )
#Enviar dados:
cliente.sendall(str.encode('Bom dia'))
#                   ^ pra garantir que a mensagem vai chegar em string
dados = cliente.recv(8192)

print('Mensagem ecoada:', dados.decode())


