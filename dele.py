
from cadaclientes import *
import os
from validacoes import *
from datetime import datetime
from datetime import date


# ============================= Função para deletar conta =========================== #

def delusu():
    hora_atual = datetime.now()
    hora = hora_atual.strftime('%H:%M')
    data = date.today()# Função para deletar usuário
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
        token = input("Digite o token cadastrado: ") # Peço o CPF cadastrado no sistema

        if token not in diciclientes: # Verifico se o mesmo se encontra no dicionário.
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
            del diciclientes[token]
            print("Usuário deletado com sucesso!")
            print(f'''
                Usuário foi deletado dia: {data}
                Horário da exclusão: {hora_atual}
                    ''')
            gravclientes(diciclientes)
            conti = input("Press ENTER for continue... ")
            break
 