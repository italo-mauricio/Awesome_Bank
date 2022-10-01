from cadaclientes import *
from getpass import getpass
from datetime import datetime
from datetime import date

# ----------------------------------------- Bem vindos às funções financeiras ------------------------------------------#
# Nesta parte estão as funções de depósito em conta já cadastrada, saque, as vantagens de ser cliente BB, e o seu saldo!
# Explicarei passo a passo como eu pensei o cóigo por completo


def menusaque(): # De começo criei essa função para trazer o menu de opções
    while True:
        os.system("cls")

                # Neste menu estão linkadas todas as funções deste módulo
        print(''' 
        | ================================================== |
        |              Bem vindos ao financeiro              |
        | -------------------------------------------------- |
        |                                                    |
        |             Depositar            [1]               |
        |             Saque                [2]               |
        |             Vantagens            [3]               |
        |             Visualizar saldo     [4]               |
        |             Extrato              [5]               |
        |             Back main menu       [0]               |
        |                                                    |
        | ================================================== |
            ''')

        usuario = ' '
        usuario = input("Escolha uma opção: ") # aqui eu peço para o usuário escolher algumas das opções!
        if usuario == "1": 
            deposibanco()
        elif usuario == "2":
            saquebanco()
        elif usuario == "3": 
            vantagens()
        elif usuario == "4": 
            saldo()
        elif usuario == "5": 
            extrato()
        elif usuario == "0":
            os.system("cls")
            break
        else: 
            print('Opção inválida!')

dici = diciclientes # Criei essa variável para somente facilitar o manuseio do dicionário que está em outro módulo.

dici2 = {}


# ---------------------------------------------- Funções do módulo -------------------------------------------------- #

# =================================================================================================================== #


def deposibanco(): # Função para o depósito bancário!
    os.system("cls")
    print("=="*50)
    print(''' 
    | ----------------------------- Bem vindos ao depósito! ----------------------------- |
    | ----- Se você está cadastrado no nosso sistema, poderá realizar seu depósito! ----- |
    | =================================================================================== |
            ''')
    print("=="*50)
    while True:
        
        senha = getpass("Digite o CPF já cadastrado em nosso sistema: ") # usando o getpass ele não mostra a senha que está sendo digitada
        if senha not in dici: # Faço a verificação se ele consta ou não no sistema.
                print("Usuário não cadastrado!")
                break 
        else:
            print("Usuário encontrado!") # Se o usuário for encontrado, ele exibe o usuário vinculado ao CPF.
            print(dici[senha][0]) # Mando printar a posição nome do cliente
            valor = float(input("Digite o quanto você quer depositar: ")) # Peço a quantia que ele quer depositar!
            dici[senha][4] += valor # Faço a soma
            print("valor novo " + str(dici[senha][4])) # Coloco o novo valor no dicionário
            print('Valor depositado com sucesso!')
            print(f"Você depositou R${valor} em sua conta!") # Mostro na tela quanto foi depositado.
            gravclientes(dici) # Salvo no dicionário
            break
        
            

# =================================================================================================================== #


def saquebanco(): # Função para o saque em conta.
    os.system("cls")
    print("=="*50)
    print(''' 
    | ----------------------------- Bem vindos ao saque! -------------------------------- |
    | ------- Se você está cadastrado no nosso sistema, poderá realizar seu saque! ------ |
    | =================================================================================== |
            ''')
    print("=="*50)
    while True:
        cpf = getpass("Digite o CPF já cadastrado em nosso sistema: ") # Peço para o cliente inserir o CPF já cadastrado na conta.
        if cpf not in dici: # Faço a verificação se ele realmente está cadastrado
            print("Usuário não encontrado!")
            break
        else:
            print("Cliente encontrado!") # Se sim, exibo o cliente.
            print(dici[cpf][0])
            valor = float(input('Qual o valor você quer sacar da sua conta: ')) # Peço para ele adicionar o valor desejado para o saque
            if valor > 0: 
                dici[cpf][4]-= valor # Faço a subtração
                print('Valor resgatado com sucesso!')
                print("valor novo " + str(dici[cpf][4]))
                print(f"Você sacou R${valor:.2f}")
                gravclientes(diciclientes)
                break
            else:
                print("Você não tem saldo suficiente!")
            

# =================================================================================================================== #

      
def saldo(): # Função para ver o saldo
    os.system("cls")
    print("=="*50)
    print(''' 
    | ----------------------------- Bem vindos ao saldo! -------------------------------- |
    | ------- Se você está cadastrado no nosso sistema, poderá ver o seu saldo! --------- |
    | =================================================================================== |
            ''')
    print("=="*50)
    while True:
        senha = getpass("Digite o CPF cadastrado!: ") # Peço para o cliente digitar o CPF cadastrado
        if senha not in dici:
            print('Usuário não encontrado!')
            break
        else:
            print("Usuário encontrado!")
            nome = dici[senha][0] # Peço o nome
            saldo = dici[senha][4] # Peço o saldo
            print(f"Nome do usuário: {nome}")
            print(f"seu saldo é de R${saldo}")
            break


# =================================================================================================================== #


def vantagens(): # Função extra somente de print 
    os.system("cls")
    while True:
        print(''' 
        |======================================================================================|
        |----------------------- Bem vindos às vantagens do BB --------------------------------|
        |--------------------------------------------------------------------------------------|
        |------- 1 - Nós temos as melhores taxas anuais para para empréstimos -----------------|
        |------- 2 - Nós temos as melhores facilidades para você financiar a sua casa, --------|
        |o seu carro, ou qualquer tipo de imóvel! ---------------------------------------------|
        |------- 3 - Temos as melhores linhas de crédito para micro e pequeno empreendedor ----|
        |------- 4 - Somente aqui no Banco do Brasil você consegue ter uma home broker, -------|
        |totalmente personalizada para você que quer começar os seus investimentos! -----------|
        |------- 5 - Então o que está esperando? venha logo fazer parte da família BB! --------|
        |======================================================================================|
        ''')
        input("Aperte qualquer tecla para sair: ")
        break



def extrato(): # Função para o extrato
    os.system("cls")
    print("=="*50)
    print(''' 
    | ----------------------------- Bem vindos ao seu extrato! ------------------------------------- |
    | ------- Se você está cadastrado no nosso sistema, poderá ver o seu extrato bancário! --------- |
    | ============================================================================================== |
            ''')
    print("=="*50)
    cpf = ' '
    while True:
        cpf = getpass("Digite o CPF cadastrado!: ")
        if cadastrocpf(cpf):
            if cpf not in dici2:
                print("Usuário não encontrado!")
                break
            else:
                print("Uusário encontrado!")
                print(dici2[cpf][0][1][2][3])
                print(f'''
                 ========================================================================================= 
                 ---------------------------------- Extrato Bancário ------------------------------------- 
                   Nome: {dici2[cpf][0]}                                                                   
                   Email: {dici2[cpf][1]}                                                                  
                   Endereço: {dici2[cpf][2]}                                                               
                   Complemento: {dici2[cpf][3]}                                                            
                   Saldo em conta: {dici2[cpf][4]}                                                         
                   CPF: {dici2[cpf][6]}                                                                    
                                                                                                          
                 ========================================================================================= 
                 Olá {dici2[cpf][0]} você tem R${dici2[cpf][4]} em sua conta bancária!                     
                 -------> Sua conta está segura e você pode fazer qualquer tipo de movimentação ---------- 
                 ========================================================================================= 
                ''')
                conti = input("Deseja continuar visualizando o seu extrato: [S/N]").strip().upper()
                if conti == 'S'.upper():
                    extrato()
                if conti == 'N'.upper():
                    menusaque()
                else:
                    print("Opção inválida!")

        else:
            print("CPF não cadastrado!") 
            
            
            
            
            
            
def transfer():
    os.system("cls")
    while True:
        print(f'''
        | ================= Transferências ================== |
        |                                                     |
        |                                                     |
        |               1 - Para clientes BB                  |
        |               2 - Para outros                       |
        |               3 - Voltar ao Menu                    |
        |                                                     |
        |                                                     |
        | ------------------ since 2022 --------------------- |
        | =================================================== |
              
        ''')
        
        
        
        