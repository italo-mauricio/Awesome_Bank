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

emprestimobox = listemprestimo()



def solicitar():
    while True:
        os.system("cls")
        print(f'''
        | ==================== Área de Empréstimos ======================= |
        | ---------------------------------------------------------------- |
        |                                                                  |
        |                     1 - Já sou cliente                           |
        |                     2 - Não sou cliente                          |
        |                     3 - Vantagens                                |
        |                     4 - Voltar ao Menu                           |
        |                                                                  |
        |                                                                  |
        |                                                                  |
        | ======================= Since 2022 ============================= |
                
        ''')
        
        option = input("Escolha uma opção: ")
        
        if option == "1":
            solicitarcliente()
        elif option == "2":
            solicitarnaocliente()
        elif option == "3":
            pass
        elif option == "4":
            emprest()
        else:
            print("Escolha uma opção válida!")
    
    
    
            
def solicitarcliente():
     pass           

def solicitarnaocliente():
    os.system("cls")
    hora_atual = datetime.now()
    hora = hora_atual.strftime('%H:%M')
    data = date.today()
    
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
        email = input("Digite o seu email: ")
        if validemail(email):
            break
        else:
            print("Digite um email válido!")
    endereco = input("Digite seu endereço: ")
    id = gerandid.gera_id()                         
    print(f"Sua ID é {id}")
    while True:
        valor = input("Quanto você deseja solicitar: ")
        if validnum(valor):
            break
        else:
            print("Digite um número!")
    while True:
        cpf = input("Digite o seu CPF: ")
        if cadastrocpf(cpf):
            if cpf not in emprestimobox:
                emprestimobox[cpf] = [nome, email, endereco, id]
                print(f'''
                | ========================================================== |
                |                 Enviar Dados para Análise                  |
                |                                                            |
                | ---------------------------------------------------------- |
                
                            Solicitação Realizada com Sucesso!
                
                Nome: {nome}
                CPF: {cpf}
                Email: {email}
                Endereço: {endereco}
                ID: {id}
                Valor da solicitação: {valor}
                Data e Hora do registro: {data} {hora}
                
                
                
                | ===================== Since 2022 ======================== |''')
                gravemprestimos(emprestimobox)
                conti = input("Aperte ENTER para continuar...")
                emprest()
            else:
                print("Empréstimo já foi solicitado por este usuário!")
                print("Tente outro cadastro!")
                
                
        else:
            print("Digite um CPF válido")
       
        
        
        
        
        
        
class gerandid():  # gera uma ID para o cliente
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand




def emprest():
    os.system("cls")
    while True:
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
        opcao = ' '
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            solicitar()
        elif opcao == '2':
            pass
        elif opcao == '3':
            pass
        elif opcao == '4':
            print("Saindo...")
            sleep(1)
            os.system("cls")
            break
        else:
            print("Escolha uma opção válida")
            