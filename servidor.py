# coding: utf-8

import socket

servidor = socket.socket()
servidor.bind( ('localhost', 50000) )
servidor.listen()

print('Aguardando conexão de um cliente')

conexao, endereco = servidor.accept() # Aceita a conexão
print('Conectado em', endereco) # Só usa o endereço pra mostrar onde está conectado

while True:
    dados = conexao.recv(8192) # A quantidade de dados que pode ser recebida
    if not dados:
        print('Fechando a conexão')
        conexao.close()
        break
    conexao.sendall(dados) # Além de enviar os dados pro servidor, envia os dados de volta pro cliente. Só pra saber se está enviando certo.