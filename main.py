from cadaclientes import *
import saque
import dele
from visumoeda import menucot



#=========================== Simulador de Caixa Eletrônico ===============================#
def menu():
    os.system("cls")
    while True:
        opcao = ' '
        print(''' 
        |===================================================================|
        |------------------------ Banco Do Brasil --------------------------|
        |===================================================================|
        | ---- [Cadastrar clientes =   (1)]  [Saque em conta =   (2)] ----- |
        | ----                                                        ----- |
        | ---- [Deletar conta =        (3)]  [Consultar Cotação =  (4)] --- |
        | ------------------- [ Sair do Sistema = (5) --------------------- |    
        | ================================================================= |
        | ---------------   Obrigado pela preferência!   ------------------ |
        | ================================================================= |
        ''')
        opcao = input("Escolha a sua opção: ")

        if opcao == "1":
            regcliente()
        elif opcao == "2":
            saque.menusaque()
        elif opcao == "3":
            dele.delusu()
        elif opcao == "4":
            menucot()
        elif opcao == "5":
            print("Obrigado pela preferência!")
            break
        else:
            print('Opção inválida!')


menu()
    


def __init__(self):
    menu()



 