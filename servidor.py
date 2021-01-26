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
        while True:
            data = self.csocket.recv(2048)
            nivel = data.decode()

            life = 100
            life_monstro = 100
            ataque_especial = 4
            cura = 6
            ativo = 'sim'
            

            if nivel == '1':
                while life > 0 and life_monstro > 0:
                    if life <= 0:
                        mensagem = "Infelizmente você perdeu :("
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        ativo = 'nao'
                        servidor.sendall(bytes(ativo, 'UTF-8'))
                        break
                    if life_monstro <= 0:
                        mensagem = "Parabéns, você conseguiu :)"
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        ativo = 'nao'
                        servidor.sendall(bytes(ativo, 'UTF-8'))
                        break
                    else:
                        mensagem = "Sua vida: "
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        for life_now in range(0, life):
                            simbolo = '*'
                            servidor.sendall(bytes(simbolo, 'UTF-8'))

                        mensagem = "Vida do monstro: "
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        for life_now_monstro in range(0, life_monstro):
                            simbolo = '-'
                            servidor.sendall(bytes(simbolo, 'UTF-8'))

                        data = self.csocket.recv(2048)
                        comando = data.decode()

                        if comando == '?':
                            mensagem = "A - Ataque\nAE - Ataque Especial\nC - Cura\nD - Desistir\n? - Caso tenha dúvidas sobre os comandos."
                            servidor.sendall(bytes(mensagem, 'UTF-8'))
                        else: 
                            if comando == 'A':
                                ataque = random.randint(5,10)
                                life_monstro -= ataque
                            elif comando == 'AE':
                                ataque_especial -= 1
                                life_monstro -= 12
                            elif comando == 'C':
                                cura -= 1
                                forca_cura = random.randint(3,10)
                                life += forca_cura
                            elif comando == 'D':
                                mensagem = "Que pena, você desistiu..."
                                servidor.sendall(bytes(mensagem, 'UTF-8'))
                                break
                            aleatorio = random.randint(1,100)
                            if aleatorio < 30:
                                life -= 12
                            else:
                                ataque_monstro = random.randint(5,10)
                                life -= ataque_monstro

            if nivel == '2':
                while life > 0 and life_monstro > 0:
                    if life <= 0:
                        mensagem = "Infelizmente você perdeu :("
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        break
                    if life_monstro <= 0:
                        mensagem = "Parabéns, você conseguiu :)"
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        break
                    else:
                        mensagem = "Sua vida: "
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        for life_now in range(0, life):
                            simbolo = '*'
                            servidor.sendall(bytes(simbolo, 'UTF-8'))

                        mensagem = "Vida do monstro: "
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        for life_now_monstro in range(0, life_monstro):
                            simbolo = '-'
                            servidor.sendall(bytes(simbolo, 'UTF-8'))

                        data = self.csocket.recv(2048)
                        comando = data.decode()

                        if comando == '?':
                            mensagem = "A - Ataque\nAE - Ataque Especial\nC - Cura\nD - Desistir\n? - Caso tenha dúvidas sobre os comandos."
                            servidor.sendall(bytes(mensagem, 'UTF-8'))
                        else: 
                            if comando == 'A':
                                ataque = random.randint(5,10)
                                life_monstro -= ataque
                            elif comando == 'AE':
                                ataque_especial -= 1
                                life_monstro -= 12
                            elif comando == 'C':
                                cura -= 1
                                forca_cura = random.randint(3,10)
                                life += forca_cura
                            elif comando == 'D':
                                mensagem = "Que pena, você desistiu..."
                                servidor.sendall(bytes(mensagem, 'UTF-8'))
                                break
                            ataque_especial_monstro = random.randint(1,100)
                            if ataque_especial_monstro < 37:
                                life -= 14
                            else:
                                ataque_monstro = random.randint(6,12)
                                life -= ataque_monstro
            
            if nivel == '3':
                while life > 0 and life_monstro > 0:
                    if life <= 0:
                        mensagem = "Infelizmente você perdeu :("
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        break
                    if life_monstro <= 0:
                        mensagem = "Parabéns, você conseguiu :)"
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        break
                    else:
                        mensagem = "Sua vida: "
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        for life_now in range(0, life):
                            simbolo = '*'
                            servidor.sendall(bytes(simbolo, 'UTF-8'))

                        mensagem = "Vida do monstro: "
                        servidor.sendall(bytes(mensagem, 'UTF-8'))
                        for life_now_monstro in range(0, life_monstro):
                            simbolo = '-'
                            servidor.sendall(bytes(simbolo, 'UTF-8'))

                        data = self.csocket.recv(2048)
                        comando = data.decode()

                        if comando == '?':
                            mensagem = "A - Ataque\nAE - Ataque Especial\nC - Cura\nD - Desistir\n? - Caso tenha dúvidas sobre os comandos."
                            servidor.sendall(bytes(mensagem, 'UTF-8'))
                        else: 
                            if comando == 'A':
                                ataque = random.randint(6,12)
                                life_monstro -= ataque
                            elif comando == 'AE':
                                ataque_especial -= 1
                                life_monstro -= 14
                            elif comando == 'C':
                                cura -= 1
                                forca_cura = random.randint(3,10)
                                life += forca_cura
                            elif comando == 'D':
                                mensagem = "Que pena, você desistiu..."
                                servidor.sendall(bytes(mensagem, 'UTF-8'))
                                break
                            ataque_especial_monstro = random.randint(1,100)
                            if ataque_especial_monstro < 45:
                                life -= 16
                            else:
                                ataque_monstro = random.randint(7,14)
                                life -= ataque_monstro
            data = self.csocket.recv(2048)
            mensagem = data.decode()
            if mensagem == 'n':
                break
                self.csocket.send(bytes(mensagem, 'UTF-8'))
                print("Client at ", endereco, " disconnected...")

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
