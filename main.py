from cadaclientes import *
import saque, dele
from visumoeda import menucot
from datetime import datetime
from datetime import date
from emprestimo import *



#=========================== Simulador de Caixa Eletrônico ===============================#
def menu():
    os.system("cls")
    while True:
        option = ' '
        time_now = datetime.now()
        hour = time_now.strftime('%H:%M')
        date1 = date.today()
        print(f'''                                           
        | ================================================================== |
        |                           Neo Bank                                 |
        | ================================================================== |
                           Date: {date1} / Time: {hour}
        | ================================================================== |
        |                   Register Users:        1                         |
        |                   Account Withdrawal:    2                         |
        |                   Delete Account:        3                         |
        |                   Consult Quote:         4                         |
        |                   Loans                  5                         |
        |                   Exit:                  0                         |    
        | ================================================================== |
        | --------------   Thank you for your preference   ----------------- |
        |                          since 2022                                |
        ''')
        option = input("Choose your option: ")

        if option == "1":
            regcliente()
        elif option == "2":
            saque.menusaque()
        elif option == "3":
            dele.delusu()
        elif option == "4":
            menucot()
        elif option == "5":
            emprest()
        elif option == "0":
            print("Thank you for your preference!")
            break
        else:
            print('Opção inválida!')



def __init__(menu):
    menu();
    return menu

 

__init__(menu);