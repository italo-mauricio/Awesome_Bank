from Screens import *
from Validations import *
import pickle, os, pwinput
from time import sleep
from random import randint
from PasswordCheck import passw
from getpass import getpass
from datetime import datetime
from datetime import date
from Archive import *




def register_client():
    clean_window
    while True:
            screen_costumer_initial()
            client = ' '
            client = input("Choose your option: ")
            if client == "1":
                create_account()
            elif client == "2":
                edit_account()
            elif client == "0":
                clean_window()
                break           
            else:
                print('Invalid Option!')
                input("Enter a valid option")
                os.system("cls")            


# ------------------------------------------------------------------------------------- #

def create_account():
    current_time = datetime.now()
    hour = current_time.strftime('%H:%M')
    date_time = date.today()
    screen_costumer_register_client()
    while True:
        name = input("Type your Name: ").strip() 
        if validstring(name):
            break
        else:
            print('Invalid name')
    while True:
        email = input("Type your Email: ").strip() 
        if validemail(email):
            break
        else:
            print('Invalid email')
    address = input("Inform your address: ").strip() 
    complement = input("Inform the complement(optional): ").strip() 
    password = int(input("Type your password: "))     
    balance = int(input("How much do you intend to deposit: "))
    id = gerandid.gera_id()
    print(f"Your registration ID is: {id}")    
    while True:
        cpf = input("Enter your CPF: ").strip() # Peço um CPF + verificação.
        if cadastrocpf(cpf):
            if cpf not in dici:
                dici[password] = [name, email, address, complement, cpf, balance, id]
                print(f'''
                      Welcome(a){dici[password][0]} to the team, we are very happy to see you here!
                      | You were registered on the day {date_time} and on time {hour} |
                      ''')
               
                gravclientes(dici)
                break
        else:
            print("Invalid CPF")

    input("Press ENTER to continue...")
    clean_window()
    

# ------------------------------------------------------------------------------------------------------- #

def edit_account(): # Função para alterar os dados.
    screen_costumer_editing_client()
    while True:
        token = int(input("Digite o seu token de acesso: "))
        if token not in dici:
            print('Usuário não encontrado!')
            break
        else:
            print("Usuário encontrado no sistema!")
            alterar = ' '
            alterar = input("Qual dado você quer alterar do seu cadastro: ").upper().strip() # Peço as novas informações
            if alterar == "nome".strip().upper():
                novo_nome = input("Digite seu novo nome: ").strip()
                dici[token][0] = novo_nome # Adiciono o novo nome ao dicionário posição nome
                print('Nome alterado com sucesso!')
                gravclientes(dici)
                break
            elif alterar == "email".strip().upper():
                novo_email = input("Digite seu novo email: ").strip()
                if validemail(novo_email):
                    dici[token][1] = novo_email # Adiciono o novo email ao dicionário posição email
                    print("Email alterado com sucesso!")
                    gravclientes(dici)
                    break
                else:
                    print("Email inválido!")
            elif alterar == "endereco".strip().upper():
                novo_endereco = input("Digite seu novo endereço: ").strip()
                dici[token][2] = novo_endereco # Adiciono o novo endereço ao dicionário posição endereço
                print("Endereço atualizado com sucesso!")
                gravclientes(dici)
                break
            elif alterar == "opicional".strip().upper():
                novo_opcional = input("Digite seu novo endereço opcional: ").strip()
                dici[token][3] = novo_opcional # Adiciono o novo complementoao dicionário posição complemento
                print("Endereço opcional atualizado com sucesso!")
                gravclientes(dici)
                break
        
            elif alterar == "senha".strip().upper():
                nova_senha = pwinput.pwinput("Digite sua nova senha: ").strip()
                if validnum(nova_senha):
                    dici[token][5] = nova_senha # Adiciono a nova senha ao dicionário posição senha
                    print('Senha atualizada com sucesso!')
                    gravclientes(dici)
                    break
                else:
                    print("Senha inválida!")
            else:
                print("Opção inválida!")

    


def delete_account():
    hora_atual = datetime.now()
    hora = hora_atual.strftime('%H:%M')
    data = date.today()# Função para deletar usuário
    screen_costumer_delete_client()
    while True:
        print("Vamos deletar o seu usuário!")
        token = int(input("Digite o token cadastrado: ")) 

        if token not in dici: 
            print("Usuário não encontrado!")
            continuar = input("Deseja continuar: [S/N] ").strip().upper()
            if continuar == 'S'.upper():
                break
            elif continuar == 'N'.upper():
                os.system("cls")
                break
                
            else:
                print('Opção inválida!')
        else:
            print("Usuário encontrado!")
            del dici[token]
            print("Usuário deletado com sucesso!")
            print(f'''
                Usuário foi deletado dia: {data}
                Horário da exclusão: {hora_atual}
                    ''')
            gravclientes(dici)
            input("Press ENTER for continue... ")
            break
 

class gerandid():  # gera uma ID para o cliente
    @staticmethod
    def gera_id():
        rand = randint(100000, 999999)
        return rand











