# coding: utf-8
# ^ vai permitir que utilizemos acentos

import socket, threading, random
# Socket: modulo principal
# Threading: vai atender os clientes

PORT = 20000

class client_thread(threading.Thread):
    def __init__(self, endereco, cliente):
        threading.Thread.__init__(self)
        self.csocket = cliente # Recebe o socket cliente
        print("Endereço da nova conexão: ", endereco)
 
    def run(self):
        print("Conexão de: ", endereco)
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        nivel = ''
        data = self.csocket.recv(2048)
        nivel = data.decode()

        #ativo = 's'

        #while ativo == 's':

        data = self.csocket.recv(2048)
        ataque_especial = data.decode()
        ataque_especial = int(ataque_especial)

        data = self.csocket.recv(2048)
        cura = data.decode()
        cura = int(cura)

        data = self.csocket.recv(2048)
        comando = data.decode()

        data = self.csocket.recv(2048)
        life_jogador = data.decode()
        life_jogador = int(life_jogador)

        data = self.csocket.recv(2048)
        life_monstro = data.decode()
        life_monstro = int(life_monstro)
        
        if nivel == '1':
            # Vez do jogador:
            if comando == 'A':
                ataque = random.randint(5,10)
                life_monstro -= ataque
            elif comando == 'AE':
                ataque_especial -= 1
                life_monstro -= 12
                print(f"Vida jogador: {life_jogador}")
                print(f"Vida monstro: {life_monstro}")
            elif comando == 'C':
                cura -= 1
                forca_cura = random.randint(3,10)
                life_jogador += forca_cura

            # Vez do monstro:
            aleatorio = random.randint(1,100)
            if aleatorio < 30:
                life_jogador -= 12
            else:
                ataque_monstro = random.randint(5,10)
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

            ataque_especial_monstro = random.randint(1,100)
            if ataque_especial_monstro < 37:
                life_jogador -= 14
            else:
                ataque_monstro = random.randint(6,12)
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

            ataque_especial_monstro = random.randint(1,100)
            if ataque_especial_monstro < 45:
                life_jogador -= 16
            else:
                ataque_monstro = random.randint(7,14)
                life_jogador -= ataque_monstro

        life_jogador = str(life_jogador)
        life_monstro = str(life_monstro)
        ataque_especial = str(ataque_especial)
        cura = str(cura)

        self.csocket.sendall(bytes(life_jogador, 'UTF-8'))
        self.csocket.sendall(bytes(life_monstro, 'UTF-8'))
        self.csocket.sendall(bytes(ataque_especial, 'UTF-8'))
        self.csocket.sendall(bytes(cura, 'UTF-8'))
        
            #data = self.csocket.recv(2048)
            #ativo = data.decode()
            # print(ativo)
            #if ativo == 'n':
                #break

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
