from cadacliente import *
import saque
import deletar
import dele


#=========================== Simulador de Caixa Eletrônico ===============================#
def menu():
    os.system("cls")
    while True:
        opcao = ' '
        print(''' 
        |===================================================================|
        |------------------------ Banco Do Brasil --------------------------|
        |===================================================================|
        |----- [Cadastrar clientes =   (1)]  [Saque em conta =   (2)] ----- |
        |-----                                                        ------|
        |----- [Deletar conta =        (3)]  [Soir do sistema =  (4)] ----- |    
        |===================================================================|
        | ---------------   Obrigado pela preferência!   ------------------ |
        |===================================================================|
        ''')
        opcao = input("Escolha a sua opção: ")

        if opcao == "1":
            regcliente()
        elif opcao == "2":
            saque.menusaque()
        elif opcao == "3":
            dele.delusu()
        elif opcao == "4":
            print("Obrigado pela preferência!")
            break
        else:
            print('Opção inválida!')


menu()
    




