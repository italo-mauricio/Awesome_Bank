from cadaclientes import *
import saque
import dele
from visumoeda import menucot
from datetime import datetime
from datetime import date
from emprestimo import *



#=========================== Simulador de Caixa Eletrônico ===============================#
def menu():
    os.system("cls")
    while True:
        opcao = ' '
        hora_atual = datetime.now()
        hora = hora_atual.strftime('%H:%M')
        data = date.today()
        print(f'''                                           
        | ================================================================== |
        |                         Banco Do Brasil                            |
        | ================================================================== |
                           Data: {data} / Hora: {hora}
        | ================================================================== |
        |                   Cadastrar clientes:    1                         |
        |                   Saque em conta:        2                         |
        |                   Deletar conta:         3                         |
        |                   Consultar Cotação:     4                         |
        |                   Empréstimos            5                         |
        |                   Sair do Sistema:       0                         |    
        | ================================================================== |
        | ---------------   Obrigado pela preferência!   ------------------- |
        |                          since 2022                                |
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
            emprest()
        elif opcao == "0":
            print("Obrigado pela preferência!")
            break
        else:
            print('Opção inválida!')


menu()

 
