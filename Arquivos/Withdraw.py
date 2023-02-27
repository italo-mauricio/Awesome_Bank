
from Archive import *
from getpass import getpass
from datetime import datetime
from datetime import date
import pickle
import os
import pwinput
from time import sleep
from Validations import *
from Screens import *







# --------------------------------------- Bem vindos às funções financeiras ------------------------------------------#
# Nesta parte estão as funções de depósito em conta já cadastrada, saque, as vantagens de ser cliente BB, e o seu saldo!
# Explicarei passo a passo como eu pensei o cóigo por completo

def menusaque():
    clean_window()

    while True:
        screen_withdraw_main()
        usuario = ' '
        usuario = input("Choose your option: ") 
        if usuario == "1": 
            deposit_account()
        elif usuario == "2":
            withdraw_account()
        elif usuario == "3": 
            transfer_account()
        elif usuario == "4": 
            benefits_bank()
        elif usuario == "5": 
            balance_account()
        elif usuario == "6":
            bank_statement()
        elif usuario == "0":
            clean_window()
            break
        else: 
            print('Invalid Option!')
      



# ---------------------------------------------- Funções do módulo -------------------------------------------------- #

# =================================================================================================================== #


def deposit_account(): # Função para o saque em conta.
    screen_withdraw_deposit()
    while True:
        token = int(input("Please, type your password: "))
        if token not in dici:
            print("User not found!")
            sleep(1)
            break
        else:
            if token == dici:
                print("Try another password")
            else:
                print("Customer Found") 
                print(dici[token][0])
                valor = int(input('What amount do you want to withdraw from your account?: '))
                if valor >= 0 : 
                    novo = dici[token][5] + valor 
                    dici[token][5] = novo
                    print('Amount redeemed successfully!')
                    print(f"New value: {dici[token][5]}")
                    print(f"You deposited: R${valor:.2f}")
                    gravdeposito(dici2)
                    gravclientes(dici)
                    input("Press ENTER for continue;;;")
                    break
                else:
                    print("You don't have enough balance!")
            
            


def withdraw_account(): 
    screen_withdraw_subtration()
    while True:
        token = int(input("Informe sua ID cadastrada no sistema: "))
        if token not in dici:
            print("Usuário não encontrado!")
            sleep(1)
            break
        else:
            if token == dici:
                print("Tente outra id!")
            else:
                print("Cliente encontrado!") 
                print(dici[token][0])
                valor = int(input('Qual o valor você quer sacar da sua conta: '))
                if dici[token][5] > 0 : 
                    novo = dici[token][5] - valor 
                    dici[token][5] = novo
                    print('Valor resgatado com sucesso!')
                    print(f"valor novo {dici[token][5]}")
                    print(f"Você sacou R${valor:.2f}")
                    gravdeposito(dici2)
                    gravclientes(dici)
                    conti = input("Aperta ENTER para continuar...")
                    break
                else:
                    print("Você não tem saldo suficiente!")
            
                        

      
def balance_account(): 
    clean_window()
    screen_withdraw_balance()
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





def benefits_bank(): 
    clean_window()
    while True:
        screen_withdraw_benefits()
        input("Press ENTER for continue... ")
        break



def bank_statement():
    current_time = datetime.now()
    hour = current_time.strftime('%H:%M')
    date_time = date.today()
    screen_withdraw_statement()
    while True:
        token = int(pwinput.pwinput("Digite sua senha de acesso: "))
    
        if token not in dici:
                print("User not found!")
                break
        else:
            os.system("cls")
            print("User found!")
            print(f'''
                ========================================================================================= 
                ---------------------------------- Bank Statement --------------------------------------- 
                Verification Date: {date_time}
                Verification Time: {hour}
                Name: {dici[token][0]}                                                                   
                Email: {dici[token][1]}                                                                  
                Address: {dici[token][2]}                                                               
                Complement: {dici[token][3]}                                                            
                CPF: {dici[token][4]}                                                         
                Account Balance: {dici[token][5]}                                                                    
                                                                                                            
                ========================================================================================= 
                Hello {dici[token][0]}, you have R${dici[token][5]} in your bank account!                     
                -------> Your account is secure and you can make any type of transaction ----------------- 
                ========================================================================================= 
            ''')
            input("Press ENTER to continue... ")
            break

            
            
def transfer_account():
    clean_window()
    while True:
        screen_withdraw_transfer()
        opcao = ' '
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            screen_withdraw_transfer_option_one()
            while True:
                transf = input("Please, type your password: ")

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
                    
                            
                        
                