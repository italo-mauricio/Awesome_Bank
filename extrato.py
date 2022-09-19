import os
from validacoes import *
from cadacliente import *





def extratoconta(): # Função de visualizar clientes cadastrados.
    os.system("cls")
    print("=="*50)
    print(''' 
    | ---------------- Vamos visualizar os seus dados cadastrados! ----------------------- |
    | ------- Se você estiver cadastrado no sistema, poderá consultar seus dados! -------- |
    | ==================================================================================== |
            ''')
    print("=="*50)
    while True:
        cpf = ' '
        cpf = input("Digite o seu CPF: ") # Peço o cpf do cliente
        if cadastrocpf(cpf):
            if cpf in diciclientes: # Faço a verificação.
                print("Usuário encontrado!")
                print(f'''
                | =========================== Extrato ======================== |
                | ------------------------------------------------------------ |
                | Nome: {diciclientes[cpf][0]}                                 |
                | Email: {diciclientes[cpf][1]}                                |             
                      
                      
                      
                      
                      
                      
                      ''')
                print(diciclientes[cpf]) # Mostro o usuário na posição pedida.
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
        else:
            print("CPF inválido!")