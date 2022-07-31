from cadacliente import *



def menusaque():
    os.system("cls")
    print("=="*39)
            
    print('''    | ------------- Bem vindos ao financeiro -------- |
    | ------------- Depositar!          [1] --------- |
    | ------------- Saque!              [2] --------- |
    | ------------- Vantagens!          [3] --------- |
    | ------------- Visualizar saldo    [4] --------- |
    | ------------- Back main menu      [5] --------- |
    | =============================================== |
            ''')
    print("=="*39)
    usuario = ' '
    usuario = input("Escolha uma opção: ")
    if usuario == "1":
        deposibanco()
    elif usuario == "2":
        saquebanco()
    elif usuario == "3":
        pass
    elif usuario == "4":
        saldo()

dici = diciclientes






def deposibanco():
    os.system("cls")
    print("=="*50)
    print(''' 
    | ---------------------  Bem vindos ao depósito! -------------------------- |
    | ------- Se você está cadastrado no nosso sistema, poderá realizar seu depósito! ----------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        senha = input("Digite a senha já cadastrada em nosso sistema: ")
        if senha not in dici:
                print("Usuário não cadastrado!")
                break
        else:
            print("Usuário encontrado!")
            print(dici[senha])
            cliente = int(input("Digite o quanto você quer depositar: "))
            soma = dici[senha][4]
            soma1 = soma + cliente
            dici[senha][4] = soma1
            print('Valor depositado com sucesso!')
            
            print(f"Você depositou R${cliente} em sua conta!")
            gravclientes(diciclientes)
            break
        
            
   





def saquebanco():
    os.system("cls")
    print("=="*50)
    print(''' 
    | ---------------------  Bem vindos ao saque! -------------------------- |
    | ------- Se você está cadastrado no nosso sistema, poderá realizar seu saque! ----------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        cadastro = input("Digite a sua senha: ")
        if cadastro not in dici:
            print("Usuário não encontrado!")
            break
        else:
            print("Cliente encontrado!")
            print(dici[cadastro])
            valor = int(input('Qual o valor você quer sacar da sua conta: '))
            sub = dici[cadastro][4]
            sub1 = sub - valor 
            dici[cadastro][4] = sub1
            print('Valor sacado com sucesso!')
            print(f"Você sacou R${valor:.2f}")
            gravclientes(diciclientes)
            break
            

      
def saldo():
    os.system("cls")
    print("=="*50)
    print(''' 
    | ---------------------  Bem vindos às vantagens! -------------------------- |
    | ------- Se você está cadastrado no nosso sistema, poderá ver suas vantagens! ----------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        senha = input("Digite a senha de acesso: ")
        if senha not in dici:
            print('Usuário não encontrado!')
            break
        else:
            print("Usuário encontrado!")
            nome = dici[senha][0]
            saldo = dici[senha][4]
            print(f"Nome do usuário: {nome}")
            print(f"seu saldo é de R${saldo}")



def vantagens():
    while True:
        print('''
        
        
        '')