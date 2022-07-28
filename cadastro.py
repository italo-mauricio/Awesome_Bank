from validacoes import *
import pickle
import os

def listclient():
    try:
        clientesb = open("clientesbanco.dat", "rb")
        diciclientes = pickle.load(clientesb)
        clientesb.close()
    except:
        clientesb = open("clientesbanco.dat", "wb")
        clientesb.close()
    return diciclientes

def gravclientes(diciclientes):
    clientesb = open("clientesbanco.dat", "wb")
    pickle.dump(diciclientes, clientesb)
    clientesb.close()


diciclientes = {}

def cadastrobanco():
    listaclientes = []
    print("=="*30)
    print('''==================================================================
    ==== Bem vindos ao cadastro de clientes na nossa agência de Caicó - RN ====
    ========== Vamos lhe pedir alguns dados, será um processo rápido ==========
    ===========================================================================
    ''')
    while True:
        nome = input('Digite o seu nome: ')
        if validstring(nome):
            listaclientes.append(nome)
            break
        else:
            print("Nome inválido!")
    while True:
        email = input("Digite um email válido: ")
        if validemail(email):
            listaclientes.append(email)
            break
        else:
            print('Email inválido!')
    endereco = input("Informe o seu endereço: ")
    endereco.append(endereco)
    complemento = input("Informe um complemento (opcional)")
    complemento.append(complemento)
    while True:
        cpf = input('Informe um CPF válido!')
        if cadastrocpf(cpf):
            if cpf not in diciclientes:
                diciclientes[cpf] = listaclientes
                print("Parabéns, agora você faz parte do time!")
                gravclientes(diciclientes)
                break
            else:
                print("CPF já cadastrado!")
        else:
            print("CPF inválido!")
        

