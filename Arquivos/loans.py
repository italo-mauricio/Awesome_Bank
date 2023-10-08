from costumer_base import *
import os
from time import sleep
from validations import *
from archive import *


dicitotal = dici


def request():
    clean_window()
    while True:
        time_now = datetime.now()
        hour = time_now.strftime("%H:%M")
        date1 = date.today()
        print(
            f"""
        |---------------------------------------------------------------|
        |                      Apply for Loan                           |
        |---------------------------------------------------------------|
                          Date: {date1} / Time: {hour}
        | ------------------------------------------------------------- |
        |                                                               |
        |                  1 - I'm already a customer                   |
        |                  2 - I'm not a customer                       |
        |                  3 - Benefits                                 |
        |                  0 - Back to main menu                        |
        |                                                               |
        |                                                               |
        | ======================= Since 2022 ========================== |       
        """
        )
        option = input("Escolha uma opção: ")

        if option == "1":
            apply_for_costumer_loan()
        elif option == "2":
            apply_for_not_costumer_loan()
        elif option == "3":
            pass
        elif option == "0":
            clean_window()
            break

        else:
            print("Escolha uma opção válida!")


def apply_for_costumer_loan():
    clean_window()
    hora_atual = datetime.now()
    hora = hora_atual.strftime("%H:%M")
    data = date.today()
    while True:
        cliente = int(input("Por favor, digite a senha cadastrada: "))
        if cliente not in dicitotal:
            print("Seu registro não foi encontrado!")
            break
        else:
            print(
                f"""
            ======================= Área do Cliente ====================
        
                Bem vindo {dicitotal[cliente][0]}
                                
                Seu atual saldo é de: {dicitotal[cliente][5]}
                
                """
            )

            emp = int(input("Quanto você deseja solicitar: "))

            print(
                f"""
            | ================= Extrato da Solicitação ==================== |
            |                                                               |
                Cliente {dicitotal[cliente][0]}
                ID da solicitação {dicitotal[cliente][6]}
                Valor do pedido {emp}
                Horário e data do pedido {hora} / {data}
                
                    
            |   Pedido realizado com sucesso!                               |
                    
                    """
            )
            emprestimo_box[cliente] = [emp, dicitotal[cliente][0], dicitotal[cliente][6], data]
            gravemprestimos(emprestimo_box)
            input("Aperte ENTER para continuar...")
            break


def validaemp():
    clean_window()
    print("Vamos verificar se você está apto")
    while True:
        cliente = int(input("Digite sua senha: "))
        if cliente not in dicitotal:
            print("Cliente não está no sistema")
        else:
            print(f"Cliente encontrado: {dicitotal[cliente][0]}")
            salario = float(input("Informe o seu salário em R$: "))
            print(
                f"O seu pedido de empréstimo foi no valor de: R${emprestimo_box[cliente][0]}"
            )
            ano = int(input("Em quantos anos você pretende pagar?: "))
            parcelas = (emprestimo_box[cliente][0] / ano) / 12
            while True:
                if parcelas > salario + (30 / 100):
                    print("Empréstimo negado!")
                    input("Aperte ENTER para continuar")
                    break
                else:
                    print("Empréstimo concedido!")
                    print(f"A parcela do seu empréstimo é de {parcelas:.2f} ao mês!")
                    dici[cliente][5] += emprestimo_box[cliente][0]
                    print(
                        f"O valor {emprestimo_box[cliente][0]} foi adicionado em sua conta!"
                    )
                    print(f"Seu novo saldo é: {dicitotal[cliente][5]}")
                    gravemprestimos(dicitotal)
                    gravemprestimos(emprestimo_box)
                    input("Aperte ENTER para sair!")
                    break
            break

def situpedido():
    clean_window()
    while True:
        try:
            codigo = int(input("Digite o seu código de acesso: "))
            if codigo in dicitotal:
                print(
                    f"""
                    | --------------------------------------------------- |
                    | -                  Awesome Bank                   - |
                    | --------------------------------------------------- |
                        Seu Pedido de Empréstimo!
                        
                        Nome: {dicitotal[codigo][0]}
                        Valor do pedido: {emprestimo_box[codigo][0]}
                        Data da solicitação: {emprestimo_box[codigo][3]}
                        Código do pedido: {emprestimo_box[codigo][2]}
                        
                    """
                )
                input("Pressione ENTER para sair...")
                break
            else:
                print("Empréstimo não encontrado!")
        except ValueError:
            print("Senha inválida. Digite apenas números inteiros.")
    clean_window()


def apply_for_not_costumer_loan():
    clean_window()
    hora_atual = datetime.now()
    hora = hora_atual.strftime("%H:%M")
    data_atual = date.today()
    data_texto = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)
    datatotal = [data_texto, hora]

    print(
        f"""
    | =========================================================== |
    |                  Enviar Dados para Análise                  |
    |                                                             |
    | ----------------------------------------------------------- |
    
                        ~ FICHA EXEMPLO ~ 
    
        Nome: seu nome
        CPF: seu cpf
        Email: seu melhor email
        Endereço: seu endereço
        ID: seu registro gerado automaticamente
        Valor da solicitação: quanto você deseja
        Data e Hora do registro: a data que foi realizado o pedido
    
    
    
                                            
    
    | ======================= Since 2022 ======================== |"""
    )

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
    token = gerandid.gera_id()
    print(f"Seu Token de acesso é {token}")
    while True:
        valor = input("Quanto você deseja solicitar: ")
        if validnum(valor):
            break
        else:
            print("Digite um número!")
    rastreio = gerabarra.gera_barra()
    print(f"Seu código de rastreio é {rastreio}")
    while True:
        cpf = input("Digite o seu CPF: ")
        if cadastrocpf(cpf):
            if id not in emprestimo_box:
                emprestimo_box[token] = [
                    nome,
                    email,
                    endereco,
                    cpf,
                    datatotal,
                    valor,
                    rastreio,
                ]
                print(
                    f"""
                | ========================================================== |
                |                 Enviar Dados para Análise                  |
                |                                                            |
                | ---------------------------------------------------------- |
                
                            Solicitação Realizada com Sucesso!
                
                Nome: {nome}
                CPF: {cpf}
                Email: {email}
                Endereço: {endereco}
                Token: {token}
                Valor da solicitação: {valor}
                Data e Hora do registro: {datatotal}
                Código de Rastreio: {rastreio}
                
                
                
                | ===================== Since 2022 ======================== |"""
                )
                gravemprestimos(emprestimo_box)
                input("Agora vamos vaerificar se você está apto para o empréstimo...")
                validaemp()
                break
            else:
                print("Empréstimo já foi solicitado por este usuário!")
                print("Tente outro cadastro!")

        else:
            print("Digite um CPF válido")


class gerandid:  # gera uma ID para o cliente
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


class gerabarra:
    @staticmethod
    def gera_barra():
        codigo = randint(500000, 9000000)
        return codigo


def emprest():
    clean_window()
    while True:
        hora_atual = datetime.now()
        hora = hora_atual.strftime("%H:%M")
        data = date.today()
        print(
            f"""
        |------------------------------------------------------|
        |                     Loan Area                        |
        |------------------------------------------------------|
                       data {data} / hora {hora}                   
        |------------------------------------------------------|
        |                                                      |
        |               1 - Apply For Loan                     | 
        |               2 - Check Loan Validity                | 
        |               3 - Check Our Rates                    | 
        |               4 - Company Policies                   | 
        |               0 - Back To Main Menu                  | 
        |                                                      | 
        |                                                      |
        |================== Since 2022 ========================|
        
        """
        )
        opcao = " "
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            request()
        elif opcao == "2":
            validaemp()
        elif opcao == "3":
            situpedido()
        elif opcao == "4":
            pass
        elif opcao == "0":
            print("Saindo...")
            sleep(1)
            clean_window()
            break
        else:
            print("Escolha uma opção válida")
