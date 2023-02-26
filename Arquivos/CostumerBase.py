
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
    os.system("cls")
    while True:
            print('''   
            | ==================================================================== |
            |                     Welcome to User Registration                     |
            | -------------------------------------------------------------------- |
            |                                                                      |
            |                Register new users                 [1]                |
            |                Bank Statement                     [2]                |
            |                Change user data                   [3]                |
            |                Back to main menu                  [0]                |
            |                                                                      |
            | ==================================================================== |
            ''')
            client = ' '
            client = input("Choose your option: ")

            if client == "1":
                create_account()
            elif client == "2":
                extract_account()
            elif client == "3":
                edit_account()
            elif client == "0":
                os.system("cls")
                break           
            else:
                print('Invalid Option!')
                input("Enter a valid option")
                os.system("cls")            



# ------------------------------------------------------------------------------------------------------- #
# ============================= Funções da parte de cadastro de clientes ================================ #




# ------------------------------------------------------------------------------------------------------- #

def create_account():
    current_time = datetime.now()
    hour = current_time.strftime('%H:%M')
    date_time = date.today()
    os.system("cls")               
    print(''' 
          | ================================================== |
          |                     Neo Bank                       |
          |                                                    |
          |                Wellcome to Register                |
          |       Come be our Neo client, let's register!      |
          |                                                    |
          | ------------------ since 2022 -------------------- |
     ''')

    while True:
        name = input("Type your Name: ").strip() 
        if validemail(name):
            break
        else:
            print('Invalid email')
    while True:
        email = input("Type your Email: ").strip() 
        if validemail(email):
            break
        else:
            print('Invalid email')
    address = input("Inform your address: ").strip() 
    complement = input("Inform the complement(optional): ").strip() 
    password = int(input("Digite sua senha: "))     
    balance = int(input("Quanto você deseja depositar: "))
    id = gerandid.gera_id()
    print(f"Sua ID de registro é: {id}")
    
    while True:
        cpf = input("Digite um CPF válido: ").strip() # Peço um CPF + verificação.
        if cadastrocpf(cpf):
            if cpf not in dici:
                dici[password] = [name, email, address, complement, cpf, balance, id]
                print(f'''
                      Bem vindo(a) {dici[password][0]} ao time, estamos muito felizes em ver você por aqui!
                      Você foi cadastrado no dia {date_time} e no horário {hour}
                      ''')
               
                gravclientes(dici)
                break
        else:
            print("CPF inválido!")

    input('Aperte alguma tecla para continuar!')
    os.system("cls")
    


# ------------------------------------------------------------------------------------------------------- #




# ------------------------------------------------------------------------------------------------------- #

def edit_account(): # Função para alterar os dados.
    os.system("cls")
    print(''' 
          | ================================================== |
          |                     Neo Bank                       |
          |                                                    |
          |                Wellcome to Editing                 |
          |       Come be our Neo client, let's Editing        |
          |                                                    |
          | ------------------ since 2022 -------------------- |
     ''')
    while True:
        token = input("Digite o seu token de acesso: ")
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
            if alterar == "email".strip().upper():
                novo_email = input("Digite seu novo email: ").strip()
                if validemail(novo_email):
                    dici[token][1] = novo_email # Adiciono o novo email ao dicionário posição email
                    print("Email alterado com sucesso!")
                    gravclientes(dici)
                    break
                else:
                    print("Email inválido!")
            if alterar == "endereco".strip().upper():
                novo_endereco = input("Digite seu novo endereço: ").strip()
                dici[token][2] = novo_endereco # Adiciono o novo endereço ao dicionário posição endereço
                print("Endereço atualizado com sucesso!")
                gravclientes(dici)
                break
            if alterar == "opicional".strip().upper():
                novo_opcional = input("Digite seu novo endereço opcional: ").strip()
                dici[token][3] = novo_opcional # Adiciono o novo complementoao dicionário posição complemento
                print("Endereço opcional atualizado com sucesso!")
                gravclientes(dici)
                break
        
            if alterar == "senha".strip().upper():
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

    
    

def extract_account():
    hora_atual = datetime.now()
    hora = hora_atual.strftime('%H:%M')
    data = date.today()# Função de visualizar clientes cadastrados.
    os.system("cls")
    print(''' 
          | ================================================== |
          |                     Neo Bank                       |
          |                                                    |
          |                Wellcome to Extrato                 |
          |       Come be our Neo client, let's Extrato        |
          |                                                    |
          | ------------------ since 2022 -------------------- |
     ''')
 
    while True:
        token = ' '
        token = pwinput.pwinput("Digite o seu token: ") # Peço o cpf do cliente
        if token in dici:
                os.system("cls") # Faço a verificação.
                print("Usuário encontrado!")
                print(f'''
                | =========================== Extrato ======================== |
                | ------------------------------------------------------------ |
                | Data da verificação: {data}
                | Horário da verificação: {hora}
                | Nome: {dici[token][0]}                                    
                | Email: {dici[token][1]}                                              
                | Endereço: {dici[token][2]}                                 
                | Complemento: {dici[token][3]}                             
                | CPF: {dici[token][4]}   
                | Saldo: {dici2[0]}                                                                    
                | ------------------------------------------------------------ |
                | ============================================================ |      
                      
                ''')
                conti = input('Press ENTER for continue...')
                os.system("cls")
                break
        else:
            print("Usuário não encontrado!")
            continuar = ' '
            continuar = str(input('Deseja continuar [S/N]: ')).strip().upper() # Pergunto se ele quer continuar caso não for encontrado
            if continuar == "S".upper():
                continue
            elif continuar == "N".upper():
                print('Saindo...')
                sleep(2)
                break
            else:
                print("Opção inválida!")
      
# ------------------------------------------------------------------------------------------------------- #

def delete_account():
    hora_atual = datetime.now()
    hora = hora_atual.strftime('%H:%M')
    data = date.today()# Função para deletar usuário
    os.system("cls")
    print(''' 
    | -------------------  Vamos deletar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá deletar os seus dados! -------- |
    | ===================================================================================== |
            ''')

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











