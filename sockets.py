# coding: utf-8
# ^ vai permitir que utilizemos acentos

import socket, threading
# Socket: modulo principal
# Threading: vai atender os clientes

PORT = 8080

def conecta(cliente, endereco):
    print('Cliente {} recebido!'.format(endereco))

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.connect(('localhost', PORT)) # Conectar o servidor a um IP e Porta remota:
    
    while True:
        cliente.recv(1024)
        cliente = cliente.rstrip()
        if (cliente != "sair"):
            print("Mensagem do cliente:", cliente)
        else:
            servidor.close()
        break
    print('Cliente desconectado!')

listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen.bind(('localhost', PORT))
# Bind: amarra o ip e a porta. Envia uma tupla contendo uma string(host local) e um inteiro(porta local)
# Objeto criado!

# Listen: Deixa o servidor no modo ouvinte esperando a conexão:
listen.listen(0)

print('Esperando o Cliente no IP e Porta: 127.0.0.1: ', PORT)

# Fique em laço de repetição e aceite todos os clientes que queiram se conectar
while True:
    # Accept: Aceita a conexão
    cliente, endereco = listen.accept()
    print('Conectado em', endereco)

    # Modo de tarefa paralela, pois enquanto aceito novos clientes outra tarefa esta atendendo os clientes já aceitos:
    threading.Thread( target = conecta, args = (cliente, endereco) ).start()

    # Target: parametro da função Thread.
    # Não pode fazer conecta(), pois não estamos chamando, só passando seus argumentos.
    print('Teste')