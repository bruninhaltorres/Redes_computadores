# coding: utf-8

import socket

PORT = 20000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Pedir a conexão:
cliente.connect( ('127.0.0.1', PORT) )

while True:
    # in_data = client.recv(1024)
    # print("From Server :", in_data.decode())
    print("Olá, seja bem-vindx. Vou te explicar como funciona o jogo... \nSua missão é derrotar um monstro e essas são suas opções: \nA - Ataque\nAE - Ataque Especial\nC - Cura\nD - Desistir\n? - Caso tenha dúvidas sobre os comandos.\n")

    nivel = input("Qual nivel você deseja jogar?\n1 - Facil\n2 - Medio\n3 - Dificil\n")
    cliente.sendall(bytes(nivel, 'UTF-8'))
    
    ativo = 'sim'

    while ativo == 'sim':
        comando = input("O que você deseja fazer? (A/AE/C/D)")
        cliente.sendall(bytes(comando, 'UTF-8'))

        data = cliente.recv(2048)
        mensagem = data.decode()
        print(mensagem)

        data = cliente.recv(2048)
        ativo = data.decode()
    mensagem = input("Jogo encerrado, quer jogar novamente? (s/n) ")
    cliente.sendall(bytes(mensagem, 'UTF-8'))
    if mensagem == 'n':
        break

cliente.close()