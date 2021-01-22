# coding: utf-8
# ^ vai permitir que utilizemos acentos

import socket, threading, select
# Socket: modul principal
# Threading: vai atender os clientes
# Select: entrada e saida de dados

HOST = 'localhost' # Poderia ser também o numero '127.0.0.1'
PORT = 8088

# Função responsavel por 
def conecta(cliente, endereco):
    print('Cliente {} recebido!'.format(endereco))
    servidor = socket.socket()

    # Conectar o servidor a um IP e Porta remota:
    servidor.connect( (' ') )

# Listen: É a porta onde bit vaice http injector o cliente se conecta pelo ip porta
listen = socket.socket()
listen.bind( (HOST, PORT) )
# .bind: amarra o ip e a porta. Envia uma tupla contendo uma string(host local) e um inteiro(porta local)
# Objeto criado!

# Colocar em modo de escuta:
listen.listen(0)

print('Esperando o Cliente no IP e Porta: 127.0.0.1:8088')

# Fique em laço de repetição e aceitar todos os clientes que queiram se conectar

while True:

    # accept: retorna uma tupla contendo dois valores. Um objeto socket do cliente e uma segunda tupla contendo o IP e a Porta do cliente.
    cliente, endereco = listen.accept()
    print('Conectado em', endereco)

    # Modo de tarefa paralela, pois enquanto recebo clientes outra tarefa esta atendendo clientes:
    threading.Thread( target = conect, args = (cliente, endereco) ).start()
    # target: parametro da função Thread.
    # não pode fazer conecta(), pois não estamos chamando, só passando seus argumentos.



    print('Teste')
# parei em 30 minutos da maior video aula.