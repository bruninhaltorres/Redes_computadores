# coding: utf-8
# ^ vai permitir que utilizemos acentos

import socket, threading
# Socket: modulo principal
# Threading: vai atender os clientes

PORT = 60000

class client_thread(threading.Thread):
    def __init__(self, endereco, cliente):
        threading.Thread.__init__(self)
        self.csocket = cliente # Recebe o socket cliente
        print("Endereço da nova conexão: ", endereco)
 
    def run(self):
        print("Conexão de: ", endereco)
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        mensagem = ''
        while True:
            data = self.csocket.recv(2048)
            mensagem = data.decode()
            if mensagem == 'sair':
                break
            print("Mensagem do cliente: ", mensagem)
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
