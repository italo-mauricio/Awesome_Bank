from cadaclientes import *
import os
from time import sleep
from validacoes import *

def listemprestimo(): # Gravando em arquivos.dat
    try:
        empresti = open("emprestimos.dat", "rb")
        emprestimobox = pickle.load(empresti)
        empresti.close()
    except:
        empresti = open("emprestimos.dat", "wb")
        empresti.close()
    return emprestimobox

def gravemprestimos(emprestimobox):
    empresti = open("emprestimos.dat", "wb")
    pickle.dump(emprestimobox, empresti)
    empresti.close()


dicitotal = diciclientes

emprestimobox = {}

def emprest():
    while True:
        os.system("cls")
        hora_atual = datetime.now()
        hora = hora_atual.strftime('%H:%M')
        data = date.today()
        print(f'''
        ========================================================
                        data {data} / hora {hora}                   

                        1 - Solicitar Empréstimo
                        2 - Verificar as nossas taxas 
                        3 - Politicas da mpresa
                        4 - Voltar ao Menu Principal
                        
            
            
            
        =================== Since 2022 ========================
        
        ''')
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            solicitar()
        elif opcao == '2':
            pass
        elif opcao == '3':
            pass
        elif opcao == '4':
            print("Saindo...")
            sleep(2)
            break
        else:
            print("Escolha uma opção válida")
            
            
            

def solicitar():
    os.system("cls")
        
    print(f'''
    | ========================================================== |
    |                 Enviar Dados para Análise                  |
    |                                                            |
    | ---------------------------------------------------------- |
    
                        ~ FICHA EXEMPLO ~ 
    
    Nome: seu nome
    CPF: seu cpf
    Email: seu melhor email
    Endereço: seu endereço
    ID: seu registro gerado automaticamente
    Valor da solicitação: quanto você deseja
    Data e Hora do registro: a data que foi realizado o pedido
    
    
    
                                            
    
    | ===================== Since 2022 ======================== |''')
    
    while True:
        nome = input("Digite o seu nome: ")
        if validstring(nome):
            break
        else:
            print("Digite um nome válido")
    while True:
        cpf = input("Digite o seu CPF: ")
        if cadastrocpf(cpf):
            break
        else:
            print("Digite um CPF válido")
    while True:
        email = input("Digite o seu email: ")
        if validemail(email):
            break
        else:
            print("Digite um email válido!")
        endereco 




