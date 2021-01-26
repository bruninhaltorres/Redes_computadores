# coding: utf-8

import socket

PORT = 20003

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Pedir a conexão:
cliente.connect( ('127.0.0.1', PORT) )

while True:
    # in_data = client.recv(1024)
    # print("From Server :", in_data.decode())
    print("Olá, seja bem-vindx. Vou te explicar como funciona o jogo... \nSua missão é derrotar um monstro e essas são suas opções: \nA - Ataque\nAE - Ataque Especial\nC - Cura\nD - Desistir\n? - Caso tenha dúvidas sobre os comandos.\n")

    life_jogador = 100
    life_monstro = 100
    ataque_especial = 4
    cura = 6

    ativo = 's'

    nivel = input("Qual nivel você deseja jogar?\n1 - Facil\n2 - Medio\n3 - Dificil\n")
    # cliente.sendall(bytes(nivel, 'UTF-8'))

    # cliente.sendall(bytes(ataque_especial, 'UTF-8'))
    # ataque_especial = int(ataque_especial)

    # cliente.sendall(bytes(cura, 'UTF-8'))
    # cura = int(cura)

    print("Okay, vamos começar...\n")

    while ativo == 's':
        comando = input("O que você deseja fazer? (A/AE/C/D/?)\n")
        if comando == '?':
            print("A - Ataque\nAE - Ataque Especial\nC - Cura\nD - Desistir\n? - Caso tenha dúvidas sobre os comandos.\n")
        if comando == 'D':
            print("Que pena, você desistiu...\n")
            # ativo = input("Quer jogar novamente?(s/n)")
        if comando == 'AE' and ataque_especial == 0:
            print("Essa opção não pode ser selecionada")
        if comando == 'C' and cura == 0:
            print("Essa opção não pode ser selecionada")
        else:
            msg = str(nivel) + '\n' + str(life_jogador) + '\n' + str(life_monstro) + '\n' + str(ataque_especial) + '\n' + str(cura) + '\n' + str(comando) + '\n' + str(ativo) + '\n';
            cliente.sendall(bytes(msg, 'UTF-8'))

            # life_jogador = str(life_jogador)
            # cliente.sendall(bytes(life_jogador, 'UTF-8'))

            # life_monstro = str(life_monstro)
            # cliente.sendall(bytes(life_monstro, 'UTF-8'))

            # Recebendo:
            data = cliente.recv(2048).decode()
            i = 0
            dado_linha = ''
            dados_servidor = []
            while(i < len(data)):
                if(data[i] != '\n'):
                    dado_linha += data[i]
                else:
                    dados_servidor.append(dado_linha)
                    dado_linha = ''
                i += 1
            life_jogador = int(dados_servidor[0])
            life_monstro = int(dados_servidor[1])
            ataque_especial = int(dados_servidor[2])
            cura = int(dados_servidor[3])

        if life_jogador <= 0:
            print("Infelizmente você perdeu :(\n")
            ativo = input("Quer jogar novamente?(s/n)")
        if life_monstro <= 0:
            print("Parabéns, você conseguiu :)\n")
            ativo = input("Quer jogar novamente?(s/n)")
        else:
            print(f"Sua vida: {life_jogador}\n")
            print(f"Vida do monstro: {life_monstro}\n")
        # cliente.sendall(bytes(ativo, 'UTF-8')) # não ta enviando?

    print("Jogo encerrado!")
    break;
cliente.close()