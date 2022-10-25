
from validacoes import *
import pickle, os, pwinput
from time import sleep
from random import randint
from passwordcheck import passw
from getpass import getpass
from datetime import datetime
from datetime import date
#from saque import dici2



def regcliente():
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
                cadastrobanco()
            elif client == "2":
                extratoconta()
            elif client == "3":
                editadados()
            elif client == "0":
                os.system("cls")
                break
                
            
            else:
                print('Invalid Option!')
                conti = input("dsadsadas")
                os.system("cls")            



# ------------------------------------------------------------------------------------------------------- #
# ============================= Funções da parte de cadastro de clientes ================================ #


def listclient(): # Gravando em arquivos.dat
    try:
        clientesb = open("clientesbanco.dat", "rb")
        diciclientes = pickle.load(clientesb)
        clientesb.close()
    except:
        clientesb = open("clientesbanco.dat", "wb")
        clientesb.close()
    return diciclientes

def gravclientes(diciclientes):
    clientesb = open("clientesbanco.dat", "wb")
    pickle.dump(diciclientes, clientesb)
    clientesb.close()


diciclientes = listclient() # Dicionário com os dados dos clientes


# ------------------------------------------------------------------------------------------------------- #

def cadastrobanco():
    hora_atual = datetime.now()
    hora = hora_atual.strftime('%H:%M')
    data = date.today()# Função de cadastramento
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
        name = input('Type your Name: ').strip() # Nome do cliente + verificação de string.
        if validstring(name):
            break
        else:
            print("Invalid Name!")
    while True:
        email = input("Type your Email: ").strip() # Email + verificação de email.
        if validemail(email):
            break
        else:
            print('Invalid email')
    address = input("Inform your address: ").strip() # Endereço livre.
    complement = input("Inform the complement(optional): ").strip() # Complemento livre
    senha = passw(password=passw)
    print("Por favor, copie sua senha aleatória")   
    id = gerandid.gera_id()                         
    print(f"Sua ID é {id}")
    
    while True:
        cpf = input("Digite um CPF válido: ").strip() # Peço um CPF + verificação.
        if cadastrocpf(cpf):
            if cpf not in diciclientes:
                diciclientes[id] = [name, email, address, complement, [], senha, cpf]
                print(f'''
                      Bem vindo(a) {diciclientes[id][0]} ao time, estamos muito felizes em ver você por aqui!
                      Você foi cadastrado no dia {data} e no horário {hora}
                      ''')
               
                gravclientes(diciclientes)
                break
        else:
            print("CPF inválido!")
    input('Aperte alguma tecla para continuar!')
    os.system("clear")
    


# ------------------------------------------------------------------------------------------------------- #




# ------------------------------------------------------------------------------------------------------- #

def editadados(): # Função para alterar os dados.
    os.system("cls")
    print("=="*50)
    print(''' 
    | -------------------  Vamos alterar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá alterar os seus dados! -------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        id = input("Digite o seu token de acesso: ")
        if id not in diciclientes:
            print('Usuário não encontrado!')
            break
        else:
            print("Usuário encontrado no sistema!")
            alterar = ' '
            alterar = input("Qual dado você quer alterar do seu cadastro: ").upper().strip() # Peço as novas informações
            if alterar == "nome".strip().upper():
                novo_nome = input("Digite seu novo nome: ").strip()
                diciclientes[id][0] = novo_nome # Adiciono o novo nome ao dicionário posição nome
                print('Nome alterado com sucesso!')
                gravclientes(diciclientes)
                break
            if alterar == "email".strip().upper():
                novo_email = input("Digite seu novo email: ").strip()
                if validemail(novo_email):
                    diciclientes[id][1] = novo_email # Adiciono o novo email ao dicionário posição email
                    print("Email alterado com sucesso!")
                    gravclientes(diciclientes)
                    break
                else:
                    print("Email inválido!")
            if alterar == "endereco".strip().upper():
                novo_endereco = input("Digite seu novo endereço: ").strip()
                diciclientes[id][2] = novo_endereco # Adiciono o novo endereço ao dicionário posição endereço
                print("Endereço atualizado com sucesso!")
                gravclientes(diciclientes)
                break
            if alterar == "opicional".strip().upper():
                novo_opcional = input("Digite seu novo endereço opcional: ").strip()
                diciclientes[id][3] = novo_opcional # Adiciono o novo complementoao dicionário posição complemento
                print("Endereço opcional atualizado com sucesso!")
                gravclientes(diciclientes)
                break
        
            if alterar == "senha".strip().upper():
                nova_senha = pwinput.pwinput("Digite sua nova senha: ").strip()
                if validnum(nova_senha):
                    diciclientes[id][5] = nova_senha # Adiciono a nova senha ao dicionário posição senha
                    print('Senha atualizada com sucesso!')
                    gravclientes(diciclientes)
                    break
                else:
                    print("Senha inválida!")
            else:
                print("Opção inválida!")

    
    

def extratoconta():
    hora_atual = datetime.now()
    hora = hora_atual.strftime('%H:%M')
    data = date.today()# Função de visualizar clientes cadastrados.
    os.system("cls")
    print("=="*50)
    print(''' 
    | ---------------- Vamos visualizar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá consultar seus dados! -------- |
    | ==================================================================================== |
            ''')
    print("=="*50)
    while True:
        id = ' '
        id = getpass("Digite o seu token: ") # Peço o cpf do cliente
        if id in diciclientes:
                os.system("cls") # Faço a verificação.
                print("Usuário encontrado!")
                print(f'''
                | =========================== Extrato ======================== |
                | ------------------------------------------------------------ |
                | Data da verificação: {data}
                | Horário da verificação: {hora}
                | Nome: {diciclientes[id][0]}                                    
                | Email: {diciclientes[id][1]}                                              
                | Endereço: {diciclientes[id][2]}                                 
                | Complemento: {diciclientes[id][3]}                             
                | Saldo: {diciclientes[id][4]}                                   
                | Senha: {diciclientes[id][5]}                                     
                | ID: {diciclientes[id][6]}                                       
                |                                                              |
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
                extratoconta()
            elif continuar == "N".upper():
                print('Saindo...')
                sleep(2)
                break
            else:
                print("Opção inválida!")
      
# ------------------------------------------------------------------------------------------------------- #


class gerandid():  # gera uma ID para o cliente
    @staticmethod
    def gera_id():
        rand = randint(100000, 999999)
        return rand

                







