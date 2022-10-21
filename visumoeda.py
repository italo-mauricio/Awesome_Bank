import requests
import os
from datetime import datetime
from datetime import date



# Cotação do Dólar Americano

def dolar():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/USD-BRL'  # Url para verificar em tempo real a cotação do Dólar

    response = requests.get(url) # Comando .get para pegar essa URL e adicionar a biblioteca

    if response.status_code == 200:
        dolar_value = float(response.json()['USD']['low']) # Utilizando o float para o cálculo de conversão
        print(f'''
              
            | ============================================================= |
            |                          Neo Bank                             |
            \                                                              /
                                                                           
                    The dollar value in Brazilian reais is R${dolar_value:.2f}    
            
            /                                                               \ 
            |
            | ------------------------------------------------------------- |
            | ======================== since 2022 ========================= |
              
              ''')
        while True:
            convert = input("Do you want to convert your currency to dollar: [Y/N] ").strip().lower()
            if convert == 'Y'.lower():
                real = float(input("Enter how much you want to convert real R$: "))
                conv = real / dolar_value
                print(f"Their R${real} converted stay USD$ {conv:.2f}")
                conti = input(("Press START for continue..."))
                break
                 
            elif convert == 'N'.lower():
                print("Thank you!")
                break
            
            else:
                print("Choose a valid option!")
    
    else:
        print("Error fetching dollar value") 
         
               
         
         
# Cotação do Euro         
         
def euro():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/EUR-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        euro_value = float(response.json()['EUR']['low'])
        print(f'''
              
            | ============================================================= |
            |                          Neo Bank                             |
            \                                                              /
                                                                           
                    The dollar value in Brazilian reais is R${euro_value:.2f}    
            
            /                                                               \ 
            |
            | ------------------------------------------------------------- |
            | ======================== since 2022 ========================= |
              
              ''')
        while True:
            convert = input("Do you want to convert your currency to Euro: [Y/N] ").strip().lower()
            if convert == 'Y'.lower():
                real = float(input("Enter how much you want to convert real R$: "))
                conv = real / euro_value
                print(f"Their R${real} converted stay ficam EUR{conv:.2f}")
                conti = input(("Press START for continue..."))
                break
                 
            if convert == 'N'.lower():
                print("Thank You!")
                break
            
            
            else:
                print("Escolha uma opção válida!")
                
    else:
        print("Erro ao buscar o valor do euro")
    
    
    
# Cotação do Bitcoin    
        
def bitcoin():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/BTC-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        bitcoin_value = float(response.json()['BTC']['low'])
        print(f'O valor do bitcoin é R${bitcoin_value:.5f}')
        while True:
            converte = input("Deseja converter sua moeda em Bitcoin: [Y/N] ").strip().lower()
            if converte == 'Y'.lower():
                real = float(input("Digite quanto você quer converter em R$: "))
                conv = real / bitcoin_value
                print(f"Seus R${real} convertidos ficam Bitcoin: {conv:.2f}")
                conti = input(("Press START for continue..."))
                break
                 
            if converte == 'N'.lower():
                print("Obrigado!")
                break
            
            
            else:
                print("Escolha uma opção válida!")
        
    else:
        print("Erro ao buscar o valor do bitcoin")
        
       
# Cotação do Franco       
        
def franco():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/CHF-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        franco_value = float(response.json()['CHF']['low'])
        print(f'O valor do franco suiço é R${franco_value:.2f}')
        while True:
            converte = input("Deseja converter sua moeda em Franco: [Y/N] ").strip().lower()
            if converte == 'Y'.lower():
                real = float(input("Digite quanto você quer converter em R$: "))
                conv = real / franco_value
                print(f"Seus R${real} convertidos ficam CHF: {conv:.2f}")
                conti = input(("Press START for continue..."))
                break
                 
            if converte == 'N'.lower():
                print("Obrigado!")
                break
            
            
            else:
                print("Escolha uma opção válida!")
        
    else:
        print("Erro ao buscar o valor do franco suiço")
        
       
# Cotação do Iene 
        
def iene():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/JPY-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        iene_value = float(response.json()['JPY']['low'])
        print(f'O valor do iene é R${iene_value:.2f}')
        while True:
            converte = input("Deseja converter sua moeda em Iene: [Y/N] ").strip().lower()
            if converte == 'Y'.lower():
                real = float(input("Digite quanto você quer converter em R$: "))
                conv = real / iene_value
                print(f"Seus R${real} convertidos ficam JPY: {conv:.2f}")
                conti = input(("Press START for continue..."))
                break
                 
            if converte == 'N'.lower():
                print("Obrigado!")
                break
            
            
            else:
                print("Escolha uma opção válida!")
        
    else:
        print("Erro ao buscar o valor do iene")
        
        
        
# Cotação do Dólar Canadense        
        
def dolarcanadense():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/CAD-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        cad_value = float(response.json()['CAD']['low'])
        print(f'O valor do dólar canadense é R${cad_value:.2f}')
        while True:
            converte = input("Deseja converter sua moeda em CAD: [Y/N] ").strip().lower()
            if converte == 'Y'.lower():
                real = float(input("Digite quanto você quer converter em R$: "))
                conv = real / cad_value
                print(f"Seus R${real} convertidos ficam CAD: {conv:.2f}")
                conti = input(("Press START for continue..."))
                break
                 
            if converte == 'N'.lower():
                print("Obrigado!")
                break
            
            
            else:
                print("Escolha uma opção válida!")
        
    else:
        print("Erro ao buscar o valor do dólar canadense")
        
        
# Menu principal        
        
def menucot():
    while True:
        os.system('cls')
        print(f'''
        | =================== Menu Cotações ==================== |
        | ------------------------------------------------------ |
        | -                 Consultar Dólar    1               - |
        | -                 Consultar Euro     2               - | 
        | -                 Consultar Franco   3               - |
        | -                 Consultar Bitcoin  4               - |
        | -                 Consultar Iene     5               - |
        | -                 Consultar CAD      6               - |
        | -                 Voltar pro Menu    0               - |
        | ------------------------------------------------------ |
        | ====================================================== |
        ''')

        opcao = ' '
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            dolar()
        elif opcao == '2':
            euro()
        elif opcao == '3':
            franco()
        elif opcao == '4':
            bitcoin()
        elif opcao == '5':
            iene()
        elif opcao == '6':
            dolarcanadense()
        elif opcao == '0':
            os.system("cls")
            break
        else:
            print("Opção inválida!")






def __init__(self):
    menucot()