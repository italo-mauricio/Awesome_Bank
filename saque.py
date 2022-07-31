from cadacliente import *



def menusaque():
    os.system("cls")
    print("=="*39)
            
    print('''    | ------------- Bem vindos ao gerencimanto financeiro! ------------------- |
    | ------------- Depositar!          [1] --------- |
    | ------------- Saque!    [2] --------- |
    | ------------- Alterar dados dos clientes!        [3] --------- |
    | ------------- Deletar dados dos clientes!        [4] --------- |
    | ------------- Voltar ao menu principal           [5] --------- |
    | ============================================================== |
            ''')
    print("=="*39)
    usuario = ' '
    usuario = input("Escolha uma opção: ")
    if usuario == "1":
        deposibanco()
    elif usuario == "2":
        saquebanco()

dici = diciclientes

dicicaixa = {}




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
        cont = 0
        senha = input("Digite a senha já cadastrada em nosso sistema: ")
        if senha not in dici:
            print("Usuário não cadastrado!")
            break
        else:
            print("Usuário encontrado!")
            print(dici[senha])
            cliente = int(input("Digite o quanto você quer depositar: "))
            
            soma = dici[senha][4] + cliente
            dici[senha][4] = soma
            print('Valor depositado com sucesso!')
            
            print(f"Você depositou R${cliente:.2f} em sua conta!")
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
            valor = int(input('Qual o valor você quer sacar da sua conta: '))
            cedula = 50
            total = valor
            cedt = 0
            while True:
                if total >= cedula:
                    total -= cedula
                    cedt +=1
                else:
                    print(f'Total de {cedt} céduas de R${cedula}')
                    if cedula == 50:
                        cedula = 20
                    elif cedula == 20:
                        cedula = 10
                    elif cedula == 10:
                        cedula = 1
                    cedt = 0
                    if total == 0:
                        break
      
