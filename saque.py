from cadaclientes import *
from getpass import getpass
from datetime import datetime
from datetime import date






# --------------------------------------- Bem vindos às funções financeiras ------------------------------------------#
# Nesta parte estão as funções de depósito em conta já cadastrada, saque, as vantagens de ser cliente BB, e o seu saldo!
# Explicarei passo a passo como eu pensei o cóigo por completo


def menusaque():
    os.system("cls")
    while True:

                os.system("cls")
                print("Você é nosso cliente, seja bem vindo!")
                print(''' 
                | ================================================== |
                |              Bem vindos ao financeiro              |
                | -------------------------------------------------- |
                |                                                    |
                |             Depositar            [1]               |
                |             Saque                [2]               |
                |             Transferências       [3]               |
                |             Vantagens            [4]               |
                |             Visualizar saldo     [5]               |
                |             Extrato              [6]               |
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
                    transfer()
                elif usuario == "4": 
                    vantagens()
                elif usuario == "5": 
                    saldo()
                elif usuario == "6":
                    extrato()
                elif usuario == "0":
                    os.system("cls")
                    break
                else: 
                    print('Opção inválida!')
      
def listdeposito(): # Gravando em arquivos.dat
    try:
        clientesa = open("deposito.dat", "rb")
        dici2 = pickle.load(clientesa)
        clientesa.close()
    except:
        clientesa = open("deposito.dat", "wb")
        clientesa.close()
    return dici2

def gravdeposito(dici2):
    clientesa = open("deposito.dat", "wb")
    pickle.dump(dici2, clientesa)
    clientesa.close()


dici2 = {}

dici = diciclientes


# ---------------------------------------------- Funções do módulo -------------------------------------------------- #

# =================================================================================================================== #


def deposibanco(): # Função para o depósito bancário!
    dici = diciclientes
    os.system("cls")
    print(''' 
    | ----------------------------- Bem vindos ao depósito! ----------------------------- |
    | ----- Se você está cadastrado no nosso sistema, poderá realizar seu depósito! ----- |
    | =================================================================================== |
            ''')
 
    while True:
        
        senha = pwinput.pwinput("Digite o CPF já cadastrado em nosso sistema: ") # usando o getpass ele não mostra a senha que está sendo digitada
        if senha not in dici: # Faço a verificação se ele consta ou não no sistema.
                print("Usuário não cadastrado!")
                break 
        else:
            print("Usuário encontrado!") # Se o usuário for encontrado, ele exibe o usuário vinculado ao CPF.
            print(dici[senha][0]) # Mando printar a posição nome do cliente
            valor = int(input("Digite o quanto você quer depositar: ")) # Peço a quantia que ele quer depositar!
            dici[senha][4] += valor # Faço a soma
            print("valor novo " + str(dici[senha][4])) # Coloco o novo valor no dicionário
            print('Valor depositado com sucesso!')
            print(f"Você depositou R${valor} em sua conta!")
            dici = dici2[senha][0][4]# Mostro na tela quanto foi depositado.
            gravclientes(dici)
            gravdeposito(dici2)
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
        id = int(input("Informe sua ID cadastrada no sistema: "))

        if id not in dici:
            print("Usuário não encontrado!")
            sleep(1)
            break
        else:
            if id == dici:
                print("Tente outra id!")
            else:
                print("Cliente encontrado!") 
                print(dici[id][0])
                valor = int(input('Qual o valor você quer sacar da sua conta: ')) 
                if valor > 0 : 
                    dici[id][4] -= valor 
                    print('Valor resgatado com sucesso!')
                    print("valor novo " + str(dici[id][4]))
                    print(f"Você sacou R${valor:.2f}")
                    gravdeposito(dici2)
                    gravclientes(dici)
                    conti = input("Aperta ENTER para continuar...")
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
        senha = getpass("Digite a senha cadastrada!: ") # Peço para o cliente digitar o CPF cadastrado
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
    token = ' '
    while True:
        token = pwinput.pwinput("Digite seu token cadastrado: ")
   
        if token not in dici:
            print("Usuário não encontrado!")
            break
        else:
            print("Uusário encontrado!")
            print(f'''
                ========================================================================================= 
                ---------------------------------- Extrato Bancário ------------------------------------- 
                Nome: {dici[token][0]}                                                                   
                Email: {dici[token][1]}                                                                  
                Endereço: {dici[token][2]}                                                               
                Complemento: {dici[token][3]}                                                            
                Saldo em conta: {dici[token][4]}                                                         
                CPF: {dici[token][6]}                                                                    
                                                                                                        
                ========================================================================================= 
                Olá {dici[token][0]} você tem R${dici[token][4]} em sua conta bancária!                     
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

        
        
        
            
            
            
def transfer():
    os.system("cls")
    while True:
        print(f'''
        | ================= Transferências ================== |
        |                                                     |
        |                                                     |
        |               1 - Para clientes BB                  |
        |               2 - Para não clientes                 |
        |               3 - Voltar ao Menu                    |
        |                                                     |
        |                                                     |
        | ------------------ since 2022 --------------------- |
        | =================================================== |
              
        ''')
        
        opcao = ' '
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            os.system("cls")
       
            print(f'''

            Bem vindo ao nosso sistema de transferência, você optou pela opção
            de tranferir para um cliente já cadastrado em nosso sistema!
            
            Nós solicitamos o CPF da pessoa cadastrada, por tanto, esteja com o 
            CPF em mãos na hora da transferência.
                    
            ''')
            while True:
                transf = input("Digite CPF da pessoa que você quer enviar: ")

                if transf not in dici:
                    print("Usuário não cadastrado no nosso sistema!")
                    break
                else:
                    print(f'''.
                                    Usuário encontrado!
                        
                        
                        Nome: {dici[transf][0]}
                        Email: {dici[transf][1]}
                        ID: {dici[transf][6]}
                            
                        ''')
                
                    quant = float(input("Digite quanto você quer transferir: "))
                    dici[transf][4] += quant
                    print("Transferência realizada com sucesso")
                    print("Novo valor: "+ str(dici[transf][4]))
                    conti = input("Aperto ENTER para continuar... ")
                    break
                    
                            
                        
                