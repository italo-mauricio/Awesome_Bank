
from cadacliente import *
import os
from validacoes import *


# ============================= Função para deletar conta =========================== #

def delusu(): # Função para deletar usuário
    os.system("cls")
    print("=="*50)
    print(''' 
    | -------------------  Vamos deletar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá deletar os seus dados! -------- |
    | ===================================================================================== |
            ''')
    print("=="*50)
    while True:
        print("Vamos deletar o seu usuário!")
        cpf = input("Digite o CPF cadastrada: ") # Peço o CPF cadastrado no sistema
        if cadastrocpf(cpf): # Faço a validação
            if cpf not in diciclientes: # Verifico se o mesmo se encontra no dicionário.
                print("Usuário não encontrado!")
                continuar = input("Deseja continuar: [S/N] ").strip().upper()
                if continuar == 'S'.upper():
                    delusu()
                elif continuar == 'N'.upper():
                    regcliente()
                else:
                    print('Opção inválida!')
            else:
                print("Usuário encontrado!")
                del diciclientes[cpf]
                print("Usuário deletado com sucesso!")
                gravclientes(diciclientes)
                break
        else:
            print('CPF inválido! ')