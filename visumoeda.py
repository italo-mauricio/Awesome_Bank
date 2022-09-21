import requests
import os




def dolar():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        dolar_value = response.json()['USD']['low']
        print(f'O valor do dólar é R${dolar_value}')
        conti = input("Press START for continue...")
        
    else:
        print("Erro ao buscar o valor do dólar") 
         
         
def euro():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/EUR-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        euro_value = response.json()['EUR']['low']
        print(f'O valor do euro é R${euro_value}')
        conti = input("Press START for continue...")
        
    else:
        print("Erro ao buscar o valor do euro")
    
        
def bitcoin():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/BTC-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        bitcoin_value = response.json()['BTC']['low']
        print(f'O valor do bitcoin é R${bitcoin_value}')
        conti = input("Press START for continue...")
        
    else:
        print("Erro ao buscar o valor do bitcoin")
        
        
        
        
def menucot():
    while True:
        os.system('cls')
        print(f'''
        | =================== Menu Cotações ==================== |
        | ------------------------------------------------------ |
        | -                  Consultar Dólar    1              - |
        | -                  Consultar Euro     2              - | 
        | -                  Consultar Libra    3              - |
        | -                  Consultar Bitcoin  4              - |
        | -                  Voltar pro Menu    5              - |
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
            break
        elif opcao == '4':
            bitcoin()
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")







