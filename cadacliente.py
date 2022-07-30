from validacoes import *
import pickle
import os
from time import sleep


def regcliente():
    os.system("cls")
    while True:
            print("=="*39)
            
            print('''    | ------------- Bem vindos ao menu cadastro! ------------------- |
    | ------------- Cadastrar novos clientes!          [1] --------- |
    | ------------- Visualizar dados dos clientes!     [2] --------- |
    | ------------- Alterar dados dos clientes!        [3] --------- |
    | ------------- Deletar dados dos clientes!        [4] --------- |
    | ------------- Voltar ao menu principal           [5] --------- |
    | ============================================================== |
            ''')
            print("=="*39)
            cliente = ' '
            cliente = input("Escolha uma das opções: ")

            if cliente == "1":
                cadastrobanco()
            elif cliente == "2":
                visucada()
            elif cliente == "3":
                altedado()
            elif cliente == "4":
                delusu()
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
    print("=="*50)
    print(''' 
    | ---------------------  Bem vindos ao cadastro de clientes! -------------------------- |
    | ------- Se você ainda não estiver cadastrado, vamos fazer o seu cadastro! ----------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
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
        cpf = input("Digite um CPF válido: ")
        if cadastrocpf(cpf):
            if cpf not in diciclientes:
                listaclientes.append(cpf)
                break
            else:
                print('CPF já cadastrado!')
        else:
            print("CPF inválido!")
    while True:
        senha = input('Escolha um senha numérica de qualquer tamanho: ')
        if validnum(senha):
            if senha not in diciclientes:
                diciclientes[senha] = listaclientes
                print("Parabéns, agora você faz parte do time!")
                gravclientes(diciclientes)
                break
            else:
                print("Senha já cadastrada!")
        else:
            print("Senha inválida!")
    input('Aperte alguma tecla para continuar!')


def visucada():
    os.system("cls")
    print("=="*50)
    print(''' 
    | ---------------- Vamos visualizar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá consultar seus dados! -------- |
    | ==================================================================================== |
            ''')
    print("=="*50)
    while True:
        senha = ' '
        senha = input("Digite sua senha: ")
        if validnum(senha):
            if senha in diciclientes:
                print("Usuário encontrado!")
                print(diciclientes[senha])
                break
            else:
                print("Usuário não encontrado!")
                continuar = ' '
                continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
                if continuar == "S".upper():
                    visucada()
                elif continuar == "N".upper():
                    print('Saindo...')
                    sleep(2)
                    break
                else:
                    print("Opção inválida!")
        else:
            print("CPF inválido!")


def altedado():
    os.system("cls")
    print("=="*50)
    print(''' 
    | -------------------  Vamos alterar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá alterar os seus dados! -------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        senha = input("Digite a senha cadastrado no sistema: ")
        if validnum(senha):
            print("Usuário encontrado no sistema!")
            alterar = ' '
            alterar = input("Qual dado você quer alterar do seu cadastro: ").upper().strip()
            if alterar == "nome".strip().upper():
                novo_nome = input("Digite seu novo nome: ")
                diciclientes[senha][0] = novo_nome
                print('Nome alterado com sucesso!')
                gravclientes(diciclientes)
                break
            if alterar == "email".strip().upper():
                novo_email = input("Digite seu novo email: ")
                if validemail(novo_email):
                    diciclientes[senha][1] = novo_email
                    print("Email alterado com sucesso!")
                    gravclientes(diciclientes)
                    break
                else:
                    print("Email inválido!")
            if alterar == "endereco".strip().upper():
                novo_endereco = input("Digite seu novo endereço: ")
                diciclientes[senha][2] = novo_endereco
                print("Endereço atualizado com sucesso!")
                gravclientes(diciclientes)
                break
            if alterar == "opicional".strip().upper():
                novo_opcional = input("Digite seu novo endereço opcional: ")
                diciclientes[senha][3] = novo_opcional
                print("Endereço opcional atualizado com sucesso!")
                gravclientes(diciclientes)
                break
            if alterar == "cpf".strip().upper():
                novo_cpf = input("Digite seu novo CPF: ")
                if cadastrocpf(novo_cpf):
                    diciclientes[senha][4] = novo_cpf
                    print("CPF atualizado com sucesso!")
                    gravclientes(diciclientes)
                    break
                else:
                    print("CPF inválido!")
            if alterar == "senha".strip().upper():
                nova_senha = input("Digite sua nova senha: ")
                if validnum(nova_senha):
                    diciclientes[senha] = nova_senha
                    print('Senha atualizada com sucesso!')
                    gravclientes(diciclientes)
                    break
                else:
                    print("Senha inválida!")
            else:
                print("Opção inválida!")

def delusu():
    os.system("cls")
    print("=="*50)
    print(''' 
    | -------------------  Vamos deletar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá deletar os seus dados! -------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        print("Vamos deletar o seu usuário!")
        cliente = input("Digite a senha cadastrada: ")
        if cliente not in diciclientes:
            print("Usuário não encontrado!")
            continuar = input("Deseja continuar: [S/N] ")
            if continuar == 'S':
                delusu()
            elif continuar == 'N':
                regcliente()
            else:
                print('Opção inválida!')
        else:
            print("Usuário encontrado!")
            del diciclientes[cliente]
            print("Usuário deletado com sucesso!")
            gravclientes(diciclientes)
            break

                
           

        

     