from cadacliente import *
import saque
import deletar
import relatorio


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
        |----- [Deletar conta =        (3)]  [Sobre nós! =       (4)] ----- |    
        |===================================================================|
        | ---------------     [Sair do sistema =    (5)] ------------------ |
        |===================================================================|
        ''')
        opcao = input("Escolha a sua opção: ")

        if opcao == "1":
            regcliente()
        elif opcao == "2":
            saque.menusaque()
        elif opcao == "3":
            deletar()
        elif opcao == "4":
            relatorio()
        elif opcao == "5":
            break
        else:
            print('Opção inválida!')


menu()
    




