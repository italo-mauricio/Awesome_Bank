from validacoes import *
import pickle
import os


def regcliente():
    while True:
            print("=="*39)
            print('''=======================================
            ============ Menu Cadastro =====================
            ========= Cadastro cliente         [1] ===========
            ========= Visualizar seus dados!   [2] ===========
            ========= Alterar seus dados!      [3] ===========
            ========= Deletar seus dados!      [4] ===========
            ========= Voltar ao menu principal [5] ===========
            ================================================

            ''')
            cliente = ' '
            cliente = input("Escolha uma das opções: ")

            if cliente == "1":
                cadastrobanco()
            elif cliente == "2":
                visucada()
            elif cliente == "3":
                print("oi")
            elif cliente == "4":
                print("oi")
            elif cliente == "5":
                break
            else:
                print('Opção inválida!')            






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


diciclientes = listclient()

def cadastrobanco():
    os.system("cls")
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
    listaclientes.append(endereco)
    complemento = input("Informe um complemento (opcional): ")
    listaclientes.append(complemento)
    while True:
        cpf = input('Informe um CPF válido: ')
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
    input('Aperte alguma tecla para continuar!')


def visucada():
    os.system("cls")
    print("=="*30)
    print(''' =======================================================
    | ---------------- Vamos visualizar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá consultar seus dados! -------- |
    | ==================================================================================== |
    
    ''')
    while True:
        cpf = ' '
        cpf = input("Digite o seu CPF: ")
        if cadastrocpf(cpf):
            if cpf in diciclientes:
                print("Usuário encontrado!")
                print(diciclientes[cpf])
                break
            else:
                print("Usuário não encontrado!")
                continuar = ' '
                continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
                if continuar == "S":
                    visucada()
                elif continuar == "N":
                    break
                else:
                    print("Opção inválida!")
        else:
            print("CPF inválido!")

        

     