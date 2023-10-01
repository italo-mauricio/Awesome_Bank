from archive import *
from getpass import getpass
from datetime import datetime
from datetime import date
import pickle
import os
import pwinput
from time import sleep
from validations import *
from screens import *


def menusaque():
    clean_window()

    while True:
        screen_withdraw_main()
        usuario = input("Choose your option: ")
        match usuario:
            case "1":
                deposit_account()
            case "2":
                withdraw_account()
            case "3":
                transfer_account()
            case "4":
                benefits_bank()
            case "5":
                bank_statement()
            case "0":
                clean_window()
                break
            case _:
                print("Invalid Option!")


def deposit_account():
    screen_withdraw_deposit()

    while True:
        token = int(input("Please, type your password: "))
        if token not in dici:
            print("User not found!")
            sleep(1)
            break
        else:
            print("Customer Found")
            print(dici[token][0])
            valor = int(
                input("What amount do you want to deposit into your account?: ")
            )

            if valor > 0:
                dici[token][5] += valor
                print("Amount deposited successfully!")
                print(f"New balance: R${dici[token][5]:.2f}")
                print(f"You deposited: R${valor:.2f}")
                gravdeposito(dici2)
                gravclientes(dici)
                input("Press ENTER to continue...")
                break
            else:
                print("Invalid deposit amount. Please enter a positive value.")


def withdraw_account():
    screen_withdraw_subtration()

    while True:
        token = int(input("Please, type your password: "))

        if token not in dici:
            print("User not found!")
            sleep(1)
            break
        else:
            print("User found!")
            print(dici[token][0])

            valor = int(
                input("What amount do you want to withdraw from your account: ")
            )

            if valor <= 0:
                print("Invalid withdrawal amount. Please enter a positive value.")
            elif valor > dici[token][5]:
                print("Insufficient funds. You don't have enough balance.")
            else:
                novo = dici[token][5] - valor
                dici[token][5] = novo
                print("Amount withdrawn successfully!")
                print(f"New balance: R${dici[token][5]:.2f}")
                print(f"You withdrew: R${valor:.2f}")
                gravdeposito(dici2)
                gravclientes(dici)
                input("Press ENTER to continue... ")
                break


def benefits_bank():
    clean_window()
    while True:
        screen_withdraw_benefits()
        input("Press ENTER for continue... ")
        break


def bank_statement():
    current_time = datetime.now()
    hour = current_time.strftime("%H:%M")
    date_time = date.today()
    screen_withdraw_statement()
    while True:
        token = int(input("Please, type your password: "))
        if token not in dici:
            print("User not found!")
            break
        else:
            clean_window()
            print("User found!")
            print(
                f"""
                ========================================================================================= 
                ---------------------------------- Bank Statement --------------------------------------- 
                Verification Date: {date_time}
                Verification Time: {hour}
                Name: {dici[token][0]}                                                                   
                Email: {dici[token][1]}                                                                  
                Address: {dici[token][2]}                                                               
                Complement: {dici[token][3]}                                                            
                CPF: {dici[token][4]}                                                         
                Account Balance: R$ {dici[token][5]} 
                                                                                                            
                ========================================================================================= 
                Hello {dici[token][0]}, you have R${dici[token][5]} in your bank account!                     
                -------> Your account is secure and you can make any type of transaction ----------------- 
                ========================================================================================= 
            """
            )
            input("Press ENTER to continue... ")
            break


def transfer_account():
    clean_window()
    while True:
        screen_withdraw_transfer()
        option = " "
        option = input("Choose your option: ")
        if option == "1":
            screen_withdraw_transfer_option_one()
            while True:
                transf = int(input("Please, type your password: "))

                if transf not in dici:
                    print("User not found!")
                    break
                else:
                    print(
                        f""".
                            
                            User Found!
                        
                        Name: {dici[transf][0]}
                        Email: {dici[transf][1]}
                        Balance: {dici[transf][5]}
                        ID: {dici[transf][6]}
                            
                        """
                    )

                    quant = int(input("Enter how much you want to transfer: "))
                    dici[transf][5] += quant
                    print("Transfer performed successfully")
                    print("New Value: "(dici[transf][5]))
                    input("Press ENTER for continue... ")
                    gravclientes(dici)
                    gravdeposito(dici2)
                    break
