# coding: utf-8
# ^ vai permitir que utilizemos acentos

import socket, threading, random
# Socket: modulo principal
# Threading: vai atender os clientes

PORT = 20003

class client_thread(threading.Thread):
    def __init__(self, endereco, cliente):
        threading.Thread.__init__(self)
        self.csocket = cliente 

    def run(self):
        print(f"Conexão {endereco} inicializada!")
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        

        ativo = 's'

        while ativo == 's':
            # Recebendo:
            nivel = ''
            data = cliente.recv(2048).decode()
            i = 0
            dado_linha = ''
            dados_cliente = []
            while(i < len(data)):
                if(data[i] != '\n'):
                    dado_linha += data[i]
                else:
                    dados_cliente.append(dado_linha) # adiciona no final do array
                    dado_linha = ''
                i += 1

            print(dados_cliente)
            if(len(dados_cliente) == 0):
                print(f"Conexão {endereco} encerrada...\n")
                break
            nivel = dados_cliente[0]
            life_jogador = int(dados_cliente[1])
            life_monstro = int(dados_cliente[2])
            ataque_especial = int(dados_cliente[3])
            cura = int(dados_cliente[4])
            comando = dados_cliente[5]
            ativo = dados_cliente[6]

            forca_cura = 0
            forca_monstro = 0

            if nivel == '1':
                # Vez do jogador:
                if comando == 'A':
                    ataque = random.randint(5,10)
                    life_monstro -= ataque
                elif comando == 'AE':
                    ataque_especial -= 1
                    life_monstro -= 12
                elif comando == 'C':
                    cura -= 1
                    forca_cura = random.randint(3,10)
                    life_jogador += forca_cura
                # Vez do monstro:
                aleatorio = random.randint(1,1000000)
                if aleatorio < 100000:
                    life_jogador -= 12
                    forca_monstro = 12
                else:
                    ataque_monstro = random.randint(5,10)
                    forca_monstro = ataque_monstro
                    life_jogador -= ataque_monstro

            if nivel == '2':

                if comando == 'A':
                    ataque = random.randint(5,10)
                    life_monstro -= ataque
                elif comando == 'AE':
                    ataque_especial -= 1
                    life_monstro -= 12
                elif comando == 'C':
                    cura -= 1
                    forca_cura = random.randint(3,10)
                    life_jogador += forca_cura

                ataque_especial_monstro = random.randint(1,1000000)
                if ataque_especial_monstro < 300000:
                    life_jogador -= 14
                    forca_monstro = 14
                else:
                    ataque_monstro = random.randint(6,12)
                    forca_monstro = ataque_monstro
                    life_jogador -= ataque_monstro
            
            if nivel == '3':

                if comando == 'A':
                    ataque = random.randint(6,12)
                    life_monstro -= ataque
                elif comando == 'AE':
                    ataque_especial -= 1
                    life_monstro -= 14
                elif comando == 'C':
                    cura -= 1
                    forca_cura = random.randint(3,10)
                    life_jogador += forca_cura

                ataque_especial_monstro = random.randint(1,1000000)
                if ataque_especial_monstro < 450000:
                    life_jogador -= 16
                    forca_monstro = 16
                else:
                    ataque_monstro = random.randint(7,14)
                    forca_monstro = ataque_monstro
                    life_jogador -= ataque_monstro

            if(life_jogador < 0):
                life_jogador = 0
            if(life_monstro < 0):
                life_monstro = 0

            msg = str(life_jogador) + '\n' + str(life_monstro) + '\n' + str(ataque_especial) + '\n' + str(cura) + '\n' + str(forca_cura) + '\n' + str(forca_monstro) + '\n'
            cliente.sendall(bytes(msg, 'UTF-8'))

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind: amarra o ip e a porta. Envia uma tupla contendo uma string(host local) e um inteiro(porta local)
servidor.bind(('localhost', PORT))
# Objeto criado!

# Fique em laço de repetição e aceite todos os clientes que queiram se conectar
while True:
    # Listen: Deixa o servidor no modo ouvinte esperando a conexão:
    servidor.listen(1)

    # Accept: Aceita a conexão
    cliente, endereco = servidor.accept()

    # Modo de tarefa paralela, pois enquanto aceito novos clientes outra tarefa esta atendendo os clientes já aceitos:
    newthread = client_thread(endereco, cliente)
    newthread.start()





