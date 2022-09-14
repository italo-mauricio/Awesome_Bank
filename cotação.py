import requests
import os
from main import *


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
        
        if opcao == '1':
            dolar()
        elif opcao == '2':
            break
        elif opcao == '3':
            break
        elif opcao == '4':
            break
        elif opcao == '5':
            menu()
        else:
            print("Opção inválida!")











def dolar():
    os.system('cls')
    url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

    response = requests.get(url)


    if response.status_code == 200:
        dolar_value = response.json()['USD']['low']
        print(f'O valor do dólar é R${dolar_value}')
    else:
        print("Erro ao buscar o valor do dólar")